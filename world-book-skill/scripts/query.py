#!/usr/bin/env python3
"""
World Book query tool.
Output structure is compatible with world-book-create.py input format.
- Default mode: output summary of all entries (name, content preview, length, keys, position, etc.)
- --uid N: output full JSON for the selected entry (same format written by create.py, can be used for --batch-edit)
- --search: search entries by keyword
- --resolve: resolve nested @UID/@name references in entries
- --brief: minimal mode
"""

import argparse
import json
import os
import sys
import re

POSITION_LABELS = {
    0: "UpChar",
    1: "DownChar",
    2: "UpAT",
    3: "DownAT",
    4: "@D",
    5: "UpEM",
    6: "DownEM",
    7: "Outlet",
}


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_worldbook(path):
    if not os.path.exists(path):
        print(f"Error: file does not exist - {path}", file=sys.stderr)
        sys.exit(1)
    book = load_json(path)
    entries = book.get("entries", {})
    name = book.get("name", None)
    return book, entries, name


def build_summary(uid_str, entry):
    content = entry.get("content", "")
    return {
        "uid": int(uid_str),
        "comment": entry.get("comment", ""),
        "content_length": len(content),
        "content_preview": content[:80] + "..." if len(content) > 80 else content,
        "keys": entry.get("key", []),
        "position": entry.get("position", 0),
        "position_label": POSITION_LABELS.get(entry.get("position", 0), str(entry.get("position", "?"))),
        "constant": entry.get("constant", False),
        "order": entry.get("order", 0),
        "depth": entry.get("depth", 1),
        "scanDepth": entry.get("scanDepth"),
        "selective": entry.get("selective", False),
        "preventRecursion": entry.get("preventRecursion", False),
        "excludeRecursion": entry.get("excludeRecursion", False),
        "disable": entry.get("disable", False),
    }


def search_entries(entries, keyword):
    keyword_lower = keyword.lower()
    results = {}
    for uid_str, entry in entries.items():
        comment = entry.get("comment", "").lower()
        content = entry.get("content", "").lower()
        keys = [k.lower() for k in entry.get("key", [])]

        if keyword_lower in comment or keyword_lower in content or any(keyword_lower in k for k in keys):
            results[uid_str] = entry
    return results


def resolve_refs(entries):
    uid_map = {}
    name_map = {}
    for uid_str, entry in entries.items():
        uid_map[int(uid_str)] = entry
        comment = entry.get("comment", "")
        if comment:
            name_map[comment] = int(uid_str)

    refs = {}
    for uid_str, entry in entries.items():
        content = entry.get("content", "")
        comment = entry.get("comment", "")
        found_refs = []
        for match in re.finditer(r'@(\d+|[^\s\n,\uFF0C\u3002\uFF1B;\u3001\u3000\]\)]+)', content):
            ref = match.group(1)
            if ref.isdigit():
                ref_uid = int(ref)
                if ref_uid in uid_map:
                    found_refs.append({
                        "reference": f"@{ref}",
                        "resolved_uid": ref_uid,
                        "resolved_comment": uid_map[ref_uid].get("comment", ""),
                    })
                else:
                    found_refs.append({
                        "reference": f"@{ref}",
                        "resolved_uid": None,
                        "resolved_comment": None,
                        "valid": False,
                    })
            else:
                if ref in name_map:
                    found_refs.append({
                        "reference": f"@{ref}",
                        "resolved_uid": name_map[ref],
                        "resolved_comment": ref,
                    })
                else:
                    found_refs.append({
                        "reference": f"@{ref}",
                        "resolved_uid": None,
                        "resolved_comment": None,
                        "valid": False,
                    })

        if found_refs:
            refs[uid_str] = {
                "uid": int(uid_str),
                "comment": comment,
                "references": found_refs,
            }

    return refs


def main():
    parser = argparse.ArgumentParser(
        description="World Book query tool - output structure compatible with world-book-create.py input format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Show summary of all entries
  python query.py my_book.json

  # Show full details for one entry (output can be used directly for --batch-edit)
  python query.py my_book.json --uid 3

  # Search by keyword
  python query.py my_book.json --search "Lin Xiaoyu"

  # Resolve nested references
  python query.py my_book.json --resolve

  # Minimal overview (including key config fields)
  python query.py my_book.json --brief
        """,
    )

    parser.add_argument("worldbook", help="Path to World Book JSON file")
    parser.add_argument("--uid", type=int, help="Show complete information for a specific UID entry")
    parser.add_argument("--search", help="Search keyword (matches title/content/keys)")
    parser.add_argument("--resolve", action="store_true", help="Resolve nested @UID/@name references in entries")
    parser.add_argument("--brief", action="store_true", help="Minimal mode (includes config fields): outputs uid/comment/content_length/keys/constant/preventRecursion/excludeRecursion")

    args = parser.parse_args()

    book, entries, name = load_worldbook(args.worldbook)

    if not entries:
        print("[]")
        return

    # --uid mode: output full JSON for one entry
    if args.uid is not None:
        uid_str = str(args.uid)
        if uid_str not in entries:
            print(f"Error: entry with UID={args.uid} not found", file=sys.stderr)
            sys.exit(1)
        entry = dict(entries[uid_str])
        entry["uid"] = int(uid_str)
        print(json.dumps(entry, ensure_ascii=False, indent=2))
        return

    # --resolve mode: resolve nested references
    if args.resolve:
        refs = resolve_refs(entries)
        if not refs:
            print("No nested references found")
        else:
            result = {
                "worldbook": os.path.abspath(args.worldbook),
                "name": name,
                "references": list(refs.values()),
            }
            print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    # --search mode: search and output summary
    if args.search:
        target_entries = search_entries(entries, args.search)
        if not target_entries:
            print(f"No entries found matching '{args.search}'")
            return
        entries = target_entries

    # default / --search / --brief mode: output summary
    if args.brief:
        summary_list = []
        for uid_str in sorted(entries.keys(), key=int):
            e = entries[uid_str]
            summary_list.append({
                "uid": int(uid_str),
                "comment": e.get("comment", ""),
                "content_length": len(e.get("content", "")),
                "keys": e.get("key", []),
                "constant": e.get("constant", False),
                "preventRecursion": e.get("preventRecursion", False),
                "excludeRecursion": e.get("excludeRecursion", False),
            })
    else:
        summary_list = []
        for uid_str in sorted(entries.keys(), key=int):
            summary_list.append(build_summary(uid_str, entries[uid_str]))

    output = {
        "worldbook": os.path.abspath(args.worldbook),
        "name": name,
        "total_entries": len(summary_list),
        "entries": summary_list,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
