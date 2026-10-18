#!/usr/bin/env python3
"""
SillyTavern World Book command-line management tool
Supports creating, editing, deleting, and listing entries, and outputs JSON files importable into SillyTavern.
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


def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_existing(path):
    """Load an existing world book, supporting both with/without top-level name field."""
    if os.path.exists(path):
        book = load_json(path)
        entries = book.get("entries", {})
        name = book.get("name", None)
        return book, entries, name
    return None, {}, None


def get_next_uid(entries):
    """Get the next available UID."""
    if not entries:
        return 0
    existing = [int(k) for k in entries.keys()]
    return max(existing) + 1


def get_next_order(entries):
    """Get the next order value."""
    if not entries:
        return 100
    orders = [e.get("order", 0) for e in entries.values()]
    return max(orders) + 100 if orders else 100


def get_next_display_index(entries):
    """Get the next displayIndex value."""
    if not entries:
        return 0
    indices = [e.get("displayIndex", 0) for e in entries.values()]
    return max(indices) + 1


def read_content(value):
    """Read content: if value starts with @filepath, read from file; otherwise return the string."""
    if value.startswith("@"):
        filepath = value[1:]
        if not os.path.exists(filepath):
            print(f"Error: file does not exist - {filepath}", file=sys.stderr)
            sys.exit(1)
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    return value


def parse_key_list(value):
    """Parse keys from a comma-separated string or list format."""
    if not value:
        return []
    if isinstance(value, list):
        return [str(k).strip() for k in value if k and str(k).strip()]
    return [k.strip() for k in value.split(",") if k.strip()]


def _camel_to_snake(name):
    """camelCase -> snake_case, e.g. preventRecursion -> prevent_recursion."""
    s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


class _Args:
    """Wrap dict as argparse.Namespace so build_entry supports both CLI and batch input.
    It auto-generates both camelCase and snake_case attributes, so both batch JSON styles are supported.
    """
    def __init__(self, d):
        for k, v in d.items():
            setattr(self, k, v)
            snake = _camel_to_snake(k)
            if snake != k:
                setattr(self, snake, v)
    def __getattr__(self, name):
        return None


def build_entry(args, uid=None, display_index=None, existing_entry=None):
    """Build an entry from arguments. args can be argparse.Namespace or _Args(dict)."""
    if isinstance(args, dict):
        args = _Args(args)
    if existing_entry:
        entry = dict(existing_entry)
    else:
        entry = {
            "uid": uid,
            "key": [],
            "keysecondary": [],
            "comment": "",
            "content": "",
            "constant": False,
            "vectorized": False,
            "selective": False,
            "selectiveLogic": 0,
            "addMemo": True,
            "order": get_next_order({}),
            "position": 0,
            "disable": False,
            "ignoreBudget": False,
            "excludeRecursion": False,
            "preventRecursion": False,
            "matchPersonaDescription": False,
            "matchCharacterDescription": False,
            "matchCharacterPersonality": False,
            "matchCharacterDepthPrompt": False,
            "matchScenario": False,
            "matchCreatorNotes": False,
            "delayUntilRecursion": False,
            "probability": 100,
            "useProbability": True,
            "depth": 1,
            "outletName": "",
            "group": "",
            "groupOverride": False,
            "groupWeight": 100,
            "scanDepth": None,
            "caseSensitive": None,
            "matchWholeWords": None,
            "useGroupScoring": False,
            "automationId": "",
            "role": 0,
            "sticky": 0,
            "cooldown": 0,
            "delay": 0,
            "triggers": [],
            "displayIndex": display_index if display_index is not None else 0,
            "extensions": {},
            "characterFilter": {"isExclude": False, "names": [], "tags": []},
        }

    # ---------- Field-by-field updates ----------
    if args.comment is not None:
        entry["comment"] = args.comment
    if args.content is not None:
        entry["content"] = read_content(args.content)
    if args.keys is not None:
        entry["key"] = parse_key_list(args.keys)
    if args.keys2 is not None:
        entry["keysecondary"] = parse_key_list(args.keys2)
    if args.depth is not None:
        entry["depth"] = args.depth
    if args.constant:
        entry["constant"] = True
    if args.no_constant:
        entry["constant"] = False
    if args.order is not None:
        entry["order"] = args.order
    if args.position is not None:
        if not (0 <= args.position <= 7):
            print(f"Error: position value {args.position} is outside 0-7 range; SillyTavern will silently skip this entry", file=sys.stderr)
            sys.exit(1)
        entry["position"] = args.position
    if args.outlet_name is not None:
        entry["outletName"] = args.outlet_name
    if args.disable:
        entry["disable"] = True
    if args.enable:
        entry["disable"] = False
    if args.selective:
        entry["selective"] = True
    if args.no_selective:
        entry["selective"] = False
    if args.selective_logic is not None:
        entry["selectiveLogic"] = args.selective_logic
    if args.probability is not None:
        entry["probability"] = args.probability
        entry["useProbability"] = True
    if args.add_memo is not None:
        entry["addMemo"] = args.add_memo
    if args.group is not None:
        entry["group"] = args.group
    if args.group_weight is not None:
        entry["groupWeight"] = args.group_weight
    if args.group_override:
        entry["groupOverride"] = True
    if args.role is not None:
        entry["role"] = args.role
    if args.prevent_recursion:
        entry["preventRecursion"] = True
    if args.exclude_recursion:
        entry["excludeRecursion"] = True
    if args.scan_depth is not None:
        entry["scanDepth"] = args.scan_depth
    if args.case_sensitive is not None:
        entry["caseSensitive"] = args.case_sensitive
    if args.match_whole_words is not None:
        entry["matchWholeWords"] = args.match_whole_words
    if args.use_group_scoring:
        entry["useGroupScoring"] = True
    if args.sticky is not None:
        entry["sticky"] = args.sticky
    if args.cooldown is not None:
        entry["cooldown"] = args.cooldown
    if args.delay is not None:
        entry["delay"] = args.delay

    # ---------- Build extensions mirror ----------
    entry["extensions"] = {
        "position": entry["position"],
        "exclude_recursion": entry["excludeRecursion"],
        "display_index": entry["displayIndex"],
        "probability": entry["probability"],
        "useProbability": entry["useProbability"],
        "depth": entry["depth"],
        "selectiveLogic": entry["selectiveLogic"],
        "outlet_name": entry["outletName"],
        "group": entry["group"],
        "group_override": entry["groupOverride"],
        "group_weight": entry["groupWeight"],
        "prevent_recursion": entry["preventRecursion"],
        "delay_until_recursion": entry["delayUntilRecursion"],
        "scan_depth": entry["scanDepth"],
        "match_whole_words": entry["matchWholeWords"],
        "use_group_scoring": entry["useGroupScoring"],
        "case_sensitive": entry["caseSensitive"],
        "automation_id": entry["automationId"],
        "role": entry["role"],
        "vectorized": entry["vectorized"],
        "sticky": entry["sticky"],
        "cooldown": entry["cooldown"],
        "delay": entry["delay"],
        "match_persona_description": entry["matchPersonaDescription"],
        "match_character_description": entry["matchCharacterDescription"],
        "match_character_personality": entry["matchCharacterPersonality"],
        "match_character_depth_prompt": entry["matchCharacterDepthPrompt"],
        "match_scenario": entry["matchScenario"],
        "match_creator_notes": entry["matchCreatorNotes"],
        "triggers": entry["triggers"],
        "ignore_budget": entry["ignoreBudget"],
    }

    return entry


# ============== Main entry point ==============

def main():
    parser = argparse.ArgumentParser(
        description="SillyTavern World Book management tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create a new world book and add an entry
  python world-book-create.py my_book.json -n --name "my_worldbook" --add \\
    --comment "rule_1" --content "entry content goes here" --keys trigger1,trigger2 --depth 2 \\
    --prevent-recursion --exclude-recursion

  # Read entry content from file
  python world-book-create.py my_book.json -n --add \\
    --comment "long setup" --content @setup.txt --keys combat --constant \\
    --prevent-recursion --exclude-recursion

  # Append entries to an existing world book
  python world-book-create.py existing_book.json --add \\
    --comment "new entry" --content "new content" --keys keyword --depth 3 \\
    --prevent-recursion --exclude-recursion

  # Edit an existing entry (by UID)
  python world-book-create.py existing_book.json --edit 3 \\
    --content "updated content" --depth 4

  # Delete an entry
  python world-book-create.py existing_book.json --delete 3

  # List all entries
  python world-book-create.py existing_book.json --list

  # Batch operation: create entries from a JSON file
  python world-book-create.py existing_book.json --batch entries.json

  # Batch edit: modify existing entries from JSON (each object must include uid)
  python world-book-create.py existing_book.json --batch-edit edits.json
        """,
    )

    # ---- File and mode arguments ----
    parser.add_argument("output", help="Path to world book JSON file")
    parser.add_argument("-n", "--new", action="store_true",
                        help="Force create a new world book (overwrite if file already exists)")
    parser.add_argument("--name", help="World book name (only used when creating new)")
    parser.add_argument("--list", action="store_true",
                        help="List all entries in the world book (read-only)")
    parser.add_argument("--delete", type=int, metavar="UID",
                        help="Delete the entry with the given UID")
    parser.add_argument("--batch",
                        help="Batch add entries from a JSON file (file must contain an array of entry objects)")
    parser.add_argument("--batch-edit",
                        help="Batch edit entries from a JSON file (array, each object must contain uid)")

    # ---- Entry operation arguments ----
    parser.add_argument("--add", action="store_true",
                        help="Add a new entry")
    parser.add_argument("--edit", type=int, metavar="UID",
                        help="Edit the entry with the given UID")

    # ---- Entry field arguments ----
    parser.add_argument("--comment", help="Entry title/comment")
    parser.add_argument("--content", help="Entry body content, or @file_path to read from file")
    parser.add_argument("--keys", help="Primary trigger keys, comma-separated")
    parser.add_argument("--keys2", help="Secondary trigger keys, comma-separated")
    parser.add_argument("--depth", type=int, help="Depth level (1-999)")
    parser.add_argument("--constant", action="store_true",
                        help="Mark as constant entry (always active)")
    parser.add_argument("--no-constant", action="store_true",
                        help="Unset constant mode")
    parser.add_argument("--order", type=int, help="Sort order value (larger appears later)")
    parser.add_argument("--position", type=int, choices=[0, 1, 2, 3, 4, 5, 6, 7],
                        help="Injection position: 0=UpChar 1=DownChar 2=UpAT 3=DownAT 4=@D 5=UpEM 6=DownEM 7=Outlet")
    parser.add_argument("--outlet-name", dest="outlet_name",
                        help="Outlet name (used when position=7)")
    parser.add_argument("--disable", action="store_true",
                        help="Set as disabled")
    parser.add_argument("--enable", action="store_true",
                        help="Set as enabled")
    parser.add_argument("--selective", action="store_true",
                        help="Enable selective activation")
    parser.add_argument("--no-selective", action="store_true",
                        help="Disable selective activation")
    parser.add_argument("--selective-logic", type=int, choices=[0, 1],
                        help="Selective logic: 0=AND 1=OR")
    parser.add_argument("--probability", type=int,
                        help="Trigger probability (0-100, default 100)")
    parser.add_argument("--add-memo", type=lambda x: x.lower() in ("true", "1", "yes"),
                        help="Whether to add to memo (true/false)")
    parser.add_argument("--group", help="Group name")
    parser.add_argument("--group-weight", type=int,
                        help="Group weight")
    parser.add_argument("--group-override", action="store_true",
                        help="Override group settings")
    parser.add_argument("--role", type=int, choices=[0, 1, 2],
                        help="Role: 0=System 1=User 2=Assistant")
    parser.add_argument("--prevent-recursion", action="store_true",
                        help="Cannot recurse further (this entry will not trigger other entries)")
    parser.add_argument("--exclude-recursion", action="store_true",
                        help="Cannot be activated by other entries (other entries cannot trigger this entry)")
    parser.add_argument("--scan-depth", type=int,
                        help="Scan depth")
    parser.add_argument("--case-sensitive", type=lambda x: x.lower() in ("true", "1", "yes"),
                        help="Case-sensitive (true/false)")
    parser.add_argument("--match-whole-words", type=lambda x: x.lower() in ("true", "1", "yes"),
                        help="Match whole words (true/false)")
    parser.add_argument("--use-group-scoring", action="store_true",
                        help="Use group scoring")
    parser.add_argument("--sticky", type=int,
                        help="Sticky value")
    parser.add_argument("--cooldown", type=int,
                        help="Cooldown value")
    parser.add_argument("--delay", type=int,
                        help="Delay value")

    args = parser.parse_args()

    # ========== List mode ==========
    if args.list:
        if not os.path.exists(args.output):
            print(f"Error: file does not exist - {args.output}", file=sys.stderr)
            sys.exit(1)
        book, entries, name = load_existing(args.output)
        print(f"World book: {args.output}")
        if name:
            print(f"Name: {name}")
        print(f"Total {len(entries)} entries:\n")
        for k in sorted(entries.keys(), key=int):
            e = entries[k]
            pos_label = POSITION_LABELS.get(e.get("position"), str(e.get("position", "?")))
            print(
                f"  UID={e.get('uid', k)}  |  "
                f"pos={pos_label}  |  "
                f"depth={e['depth']}  |  "
                f"constant={'Y' if e.get('constant') else 'N'}  |  "
                f"disable={'Y' if e.get('disable') else 'N'}  |  "
                f"preventRec={'Y' if e.get('preventRecursion') else 'N'}  |  "
                f"excludeRec={'Y' if e.get('excludeRecursion') else 'N'}  |  "
                f"order={e.get('order')}  |  "
                f"keys={e.get('key', [])}"
            )
            print(f"    Title: {e.get('comment', '')[:80]}")
            print()
        return

    # ========== Load / Create ==========
    book, entries, book_name = load_existing(args.output)

    if args.new or not os.path.exists(args.output):
        # Create new
        book = {}
        entries = {}
        book_name = args.name
        print(f"Created new world book: {args.output}")

    is_modified = False

    # ========== Delete ==========
    if args.delete is not None:
        uid_str = str(args.delete)
        if uid_str not in entries:
            print(f"Error: UID={args.delete} entry not found", file=sys.stderr)
            sys.exit(1)
        comment = entries[uid_str].get("comment", "")
        del entries[uid_str]
        print(f"Deleted UID={args.delete}: {comment}")
        is_modified = True

    # ========== Edit ==========
    if args.edit is not None:
        uid_str = str(args.edit)
        if uid_str not in entries:
            print(f"Error: UID={args.edit} entry not found", file=sys.stderr)
            sys.exit(1)
        existing = entries[uid_str]
        new_entry = build_entry(args, uid=args.edit, display_index=existing.get("displayIndex"),
                                existing_entry=existing)
        entries[uid_str] = new_entry
        print(f"Edited UID={args.edit}: {new_entry.get('comment', '')}")
        is_modified = True

    # ========== Add ==========
    if args.add:
        uid = get_next_uid(entries)
        display_index = get_next_display_index(entries)
        if args.order is None:
            args.order = get_next_order(entries)
        new_entry = build_entry(args, uid=uid, display_index=display_index)
        entries[str(uid)] = new_entry
        print(f"Added UID={uid}: {new_entry.get('comment', '')}")
        is_modified = True

    # ========== Batch ==========
    if args.batch:
        batch_data = load_json(args.batch)
        if not isinstance(batch_data, list):
            print("Error: batch file content must be a JSON array", file=sys.stderr)
            sys.exit(1)
        for item in batch_data:
            uid = get_next_uid(entries)
            display_index = get_next_display_index(entries)
            if "order" not in item or item["order"] is None:
                item["order"] = get_next_order(entries)
            new_entry = build_entry(item, uid=uid, display_index=display_index)
            entries[str(uid)] = new_entry
            print(f"Added UID={uid}: {new_entry.get('comment', '')}")
            is_modified = True
        print(f"Batch complete: added {len(batch_data)} entries")

    # ========== Batch edit ==========
    if args.batch_edit:
        batch_data = load_json(args.batch_edit)
        if not isinstance(batch_data, list):
            print("Error: batch-edit file content must be a JSON array", file=sys.stderr)
            sys.exit(1)
        for item in batch_data:
            if "uid" not in item:
                print(f"Error: each object in batch-edit must include a uid field: {item}", file=sys.stderr)
                sys.exit(1)
            uid_str = str(item["uid"])
            if uid_str not in entries:
                print(f"Error: UID={item['uid']} entry not found", file=sys.stderr)
                sys.exit(1)
            existing = entries[uid_str]
            # remove uid from item dict so build_entry doesn't try to overwrite it
            edit_item = {k: v for k, v in item.items() if k != "uid"}
            new_entry = build_entry(edit_item, uid=item["uid"], display_index=existing.get("displayIndex"),
                                    existing_entry=existing)
            entries[uid_str] = new_entry
            print(f"Edited UID={item['uid']}: {new_entry.get('comment', '')}")
            is_modified = True
        print(f"Batch edit complete: modified {len(batch_data)} entries")

    # ========== Fallback check ==========
    if not is_modified and not args.list:
        print("Notice: no operation was executed. Use --add / --edit / --delete / --list to choose an action.", file=sys.stderr)
        parser.print_help()
        sys.exit(0)

    # ========== Save ==========
    book["entries"] = entries
    if book_name:
        book["name"] = book_name

    save_json(book, args.output)
    print(f"Saved to: {os.path.abspath(args.output)}")


if __name__ == "__main__":
    main()
