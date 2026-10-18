#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SillyTavern chara_card_v3 character card generator
========================================
Supports: generate from JSON config / interactive creation / extract template from existing card / validate card

Usage:
  python card-generator.py --config config.json --output card.json
  python card-generator.py --interactive
  python card-generator.py --extract existing.json --output template.json
  python card-generator.py --validate card.json
  python card-generator.py --help

Dependencies: Python 3.8+ (standard library only)
"""

import argparse
import json
import os
import sys
import uuid
from datetime import datetime, timezone

# ============================================================
# Utility functions
# ============================================================

def parse_key_list(value):
    """Split comma-separated trigger keyword strings into a list, while supporting already-split lists."""
    if not value:
        return []
    if isinstance(value, list):
        result = []
        for item in value:
            if isinstance(item, str) and ',' in item:
                result.extend([k.strip() for k in item.split(',') if k.strip()])
            elif item:
                result.append(item)
        return result
    if isinstance(value, str):
        return [k.strip() for k in value.split(',') if k.strip()]
    return []

def gen_uuid():
    """Generate UUID v4."""
    return str(uuid.uuid4())

def gen_id(prefix="id"):
    """Generate a timestamp-based ID with prefix."""
    return f"{prefix}_{int(datetime.now().timestamp() * 1000)}_{abs(hash(str(uuid.uuid4()))) % 100000}"

def now_iso():
    """Return current UTC time in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()

def escape_regex_body(text):
    """Escape / inside regex body. Refer to EasyVibeCard buildFindRegexString."""
    normalized = str(text).replace("\\/", "/")
    return normalized.replace("/", "\\/")

def build_find_regex(pattern, flags="gs"):
    """Build slash-style findRegex string."""
    return f"/{escape_regex_body(pattern)}/{flags}"

def clamp(value, min_val, max_val):
    """Clamp numeric value to range."""
    return max(min_val, min(value, max_val))

def first(*values):
    """Return the first non-empty value."""
    for v in values:
        if v is not None and v != "":
            return v
    return ""

# ============================================================
# Default templates
# ============================================================

DEFAULT_MVU_BUNDLE = (
    "import 'https://testingcf.jsdelivr.net/gh/MagicalAstrogy/MagVarUpdate/artifact/bundle.js';"
)

DEFAULT_MVU_BUTTONS = [
    {"name": "Reprocess variables", "visible": True},
    {"name": "Reload initial variables", "visible": True},
    {"name": "Clear old floor variables", "visible": False},
    {"name": "Snapshot floor", "visible": False},
    {"name": "Replay floor", "visible": False},
    {"name": "Retry extra model parsing", "visible": False},
]

# ============================================================
# CardBuilder: Core builder
# ============================================================

class CardBuilder:
    """SillyTavern chara_card_v3 character card builder."""

    def __init__(self):
        self._init_empty()

    def _init_empty(self):
        self.card = {
            "name": "",
            "description": "",
            "personality": "",
            "scenario": "",
            "first_mes": "",
            "mes_example": "",
            "creatorcomment": "",
            "avatar": "none",
            "talkativeness": "0.5",
            "fav": False,
            "tags": [],
            "spec": "chara_card_v3",
            "spec_version": "3.0",
            "data": {
                "name": "",
                "description": "",
                "personality": "",
                "scenario": "",
                "first_mes": "",
                "mes_example": "",
                "creator_notes": "",
                "system_prompt": "",
                "post_history_instructions": "",
                "tags": [],
                "creator": "",
                "character_version": "1.0",
                "alternate_greetings": [],
                "group_only_greetings": [],
                "extensions": {
                    "talkativeness": "0.5",
                    "fav": False,
                    "world": "",
                    "depth_prompt": {"prompt": "", "depth": 4, "role": "system"},
                },
                "character_book": {
                    "name": "",
                    "entries": [],
                },
            },
            "create_date": now_iso(),
        }

    # === Basic info ===
    def set_name(self, name):
        self.card["name"] = name
        self.card["data"]["name"] = name
        self.card["data"]["extensions"]["world"] = name
        return self

    def set_card_info(self, *, name=None, description="", personality="",
                      scenario="", creator_notes="", system_prompt="",
                      post_history_instructions="", creator="", version="1.0"):
        if name:
            self.set_name(name)
        d = self.card["data"]
        if description: d["description"] = description
        if personality: d["personality"] = personality
        if scenario: d["scenario"] = scenario
        if creator_notes: d["creator_notes"] = creator_notes
        if system_prompt: d["system_prompt"] = system_prompt
        if post_history_instructions: d["post_history_instructions"] = post_history_instructions
        if creator: d["creator"] = creator
        if version: d["character_version"] = version
        return self

    def set_talkativeness(self, value):
        v = str(value)
        self.card["talkativeness"] = v
        self.card["data"]["extensions"]["talkativeness"] = v
        return self

    # === Openings ===
    def set_first_message(self, text):
        self.card["first_mes"] = text
        self.card["data"]["first_mes"] = text
        return self

    def add_alternate_greeting(self, text):
        self.card["data"]["alternate_greetings"].append(text)
        return self

    # === World book ===
    def _make_extensions(self, *, position_num=1, depth=4, role=0,
                         prevent_recursion=True, exclude_recursion=True,
                         display_index=0, probability=100,
                         selective_logic=0, enabled=True):
        return {
            "position": position_num,
            "exclude_recursion": exclude_recursion,
            "display_index": display_index,
            "probability": probability,
            "useProbability": True,
            "depth": depth,
            "selectiveLogic": selective_logic,
            "outlet_name": "",
            "group": "",
            "group_override": False,
            "group_weight": 100,
            "prevent_recursion": prevent_recursion,
            "delay_until_recursion": False,
            "scan_depth": None,
            "match_whole_words": None,
            "use_group_scoring": False,
            "case_sensitive": None,
            "automation_id": "",
            "role": role,
            "vectorized": False,
            "sticky": 0,
            "cooldown": 0,
            "delay": 0,
            "match_persona_description": False,
            "match_character_description": False,
            "match_character_personality": False,
            "match_character_depth_prompt": False,
            "match_scenario": False,
            "match_creator_notes": False,
            "triggers": [],
            "ignore_budget": False,
        }

    def set_worldbook_name(self, name):
        self.card["data"]["character_book"]["name"] = name
        return self

    def add_worldbook_entry(self, *, comment, content, keys=None,
                            secondary_keys=None, constant=True, position="after_char",
                            position_num=1, order=100, enabled=True,
                            depth=4, use_regex=True, prevent_recursion=True,
                            exclude_recursion=True):
        keys = keys or []
        secondary_keys = secondary_keys or []
        selective = not constant
        ext = self._make_extensions(
            position_num=position_num, depth=depth,
            prevent_recursion=prevent_recursion,
            exclude_recursion=exclude_recursion,
            display_index=len(self.card["data"]["character_book"]["entries"]),
        )
        entry = {
            "id": len(self.card["data"]["character_book"]["entries"]),
            "keys": keys,
            "secondary_keys": secondary_keys,
            "comment": comment,
            "content": content,
            "constant": constant,
            "selective": selective,
            "insertion_order": order,
            "enabled": enabled,
            "position": position,
            "use_regex": use_regex,
            "extensions": ext,
        }
        self.card["data"]["character_book"]["entries"].append(entry)
        return self

    # === MVU variable components ===
    def add_initvar_entry(self, yaml_content, enabled=False):
        """Add [initvar] variable initialization entry (before_char, content wrapped in <initvar> tags)."""
        wrapped = f"<initvar>\n{yaml_content}\n</initvar>"
        return self.add_worldbook_entry(
            comment="[initvar]Variable initialization (do not enable)",
            content=wrapped,
            constant=True, position="before_char", position_num=0,
            order=14720, enabled=enabled,
        )

    def add_variable_list_entry(self, var_path="stat_data", depth=0):
        """Add variable list entry (@D depth=0)."""
        content = (
            "---\n"
            "<status_current_variable>\n"
            f"{{{{format_message_variable::{var_path}}}}}\n"
            "</status_current_variable>"
        )
        return self.add_worldbook_entry(
            comment="Variable list",
            content=content,
            constant=True, position="at_depth", position_num=4,
            order=14720, depth=depth,
        )

    def add_variable_update_rules(self, yaml_content):
        """Add [mvu_update] variable update rules entry (at_depth D0)."""
        return self.add_worldbook_entry(
            comment="[mvu_update]Variable update rules",
            content=yaml_content,
            constant=True, position="at_depth", position_num=4,
            order=14720, depth=0,
        )

    def add_variable_output_format(self, content=None):
        """Add variable output format entry (@D depth=0)."""
        if content is None:
            content = (
                "---\n"
                "Variable output format:\n"
                "  rule:\n"
                "    - You must output update analysis and the actual update command at the end of your reply\n"
                "    - Update commands must follow the JSON Patch (RFC 6902) standard\n"
                "    - Supported operations: replace/delta/insert/remove\n"
                "    - Do not update read-only variables that start with _\n"
                "  format: |-\n"
                "    <UpdateVariable>\n"
                "    <Analysis>$(Output in English, no more than 80 words)\n"
                "    - ${Compute elapsed time: ...}\n"
                "    - ${Determine whether dramatic changes are allowed: yes/no}\n"
                "    - ${Analyze each variable based on checks: ...}\n"
                "    </Analysis>\n"
                "    <JSONPatch>\n"
                "    [\n"
                "      { \"op\": \"replace\", \"path\": \"${path}\", \"value\": \"${new_value}\" },\n"
                "      { \"op\": \"delta\", \"path\": \"${numeric_path}\", \"value\": ${delta_value} },\n"
                "      { \"op\": \"insert\", \"path\": \"${object_path/new_key}\", \"value\": \"${new_value}\" },\n"
                "      { \"op\": \"remove\", \"path\": \"${object_path/key}\" }\n"
                "    ]\n"
                "    </JSONPatch>\n"
                "    </UpdateVariable>"
            )
        return self.add_worldbook_entry(
            comment="[mvu_update]Variable output format",
            content=content,
            constant=True, position="at_depth", position_num=4,
            order=14720, depth=0,
        )

    # === Regex scripts ===
    def _ensure_regex_scripts(self):
        d = self.card["data"]["extensions"]
        if "regex_scripts" not in d:
            d["regex_scripts"] = []

    def add_regex_script(self, *, name, find_regex=None, find_pattern=None,
                         find_flags="gs", replace_string="",
                         markdown_only=True, prompt_only=False,
                         placement=None, min_depth=None, max_depth=None,
                         run_on_edit=False, substitute_regex=0):
        self._ensure_regex_scripts()
        if find_regex is None and find_pattern is not None:
            find_regex = build_find_regex(find_pattern, find_flags)
        if find_regex is None:
            find_regex = "//"
        if placement is None:
            placement = [2]
        script = {
            "id": gen_uuid(),
            "scriptName": name,
            "findRegex": find_regex,
            "replaceString": replace_string,
            "trimStrings": [],
            "placement": placement,
            "disabled": False,
            "markdownOnly": markdown_only,
            "promptOnly": prompt_only,
            "runOnEdit": run_on_edit,
            "substituteRegex": substitute_regex,
            "minDepth": min_depth,
            "maxDepth": max_depth,
        }
        self.card["data"]["extensions"]["regex_scripts"].append(script)
        return self

    def add_statusbar_regex(self, html_template, name="[UI]Status bar"):
        """Add status bar beautification regex (HTML provided by caller)."""
        return self.add_regex_script(
            name=name,
            find_pattern="<StatusPlaceHolderImpl/>",
            replace_string=html_template,
            markdown_only=True, placement=[2],
            run_on_edit=True,
        )

    def add_statusbar_hide_regex(self):
        """Add status bar hide regex (not sent to AI)."""
        return self.add_regex_script(
            name="[NoSend]UI placeholder",
            find_pattern="<StatusPlaceHolderImpl/>",
            replace_string="",
            markdown_only=False, prompt_only=True,
            placement=[2], run_on_edit=True,
        )

    def add_mvu_hide_regex(self, name="[NoSend]Remove variable updates", min_depth=4):
        """Add variable update hide regex."""
        return self.add_regex_script(
            name=name,
            find_pattern="<UpdateVariable>(.*?)<\\/UpdateVariable>",
            find_flags="gis",
            replace_string="",
            markdown_only=False, prompt_only=True,
            placement=[1, 2], min_depth=min_depth,
        )

    def add_mvu_beautify_full_regex(self):
        """Add beautify regex for complete variable updates."""
        return self.add_regex_script(
            name="[Beautify]Complete variable update",
            find_pattern="<UpdateVariable>(.*?)<\\/UpdateVariable>",
            find_flags="gis",
            replace_string="<details><summary>Variable update complete</summary>\n$1\n</details>",
            markdown_only=True, placement=[2],
        )

    def add_mvu_beautify_partial_regex(self):
        """Add notice regex for incomplete variable updates."""
        return self.add_regex_script(
            name="[Beautify]Variable update in progress",
            find_pattern="<updatevariable>(?!.*<\\/updatevariable>)\\s*(.*)\\s*$",
            find_flags="gsi",
            replace_string="<details><summary>Variable update in progress...</summary>\n$1\n</details>",
            markdown_only=True, placement=[2],
        )

    # === Tavern helper scripts ===
    def _ensure_tavern_helper(self):
        d = self.card["data"]["extensions"]
        if "tavern_helper" not in d:
            d["tavern_helper"] = [["scripts", []], ["variables", {}]]
        return d["tavern_helper"]

    def add_tavern_script(self, *, name, content, enabled=True,
                          info="", buttons=None, data=None):
        th = self._ensure_tavern_helper()
        script = {
            "type": "script",
            "enabled": enabled,
            "name": name,
            "id": gen_uuid(),
            "content": content,
            "info": info,
            "button": {
                "enabled": True,
                "buttons": buttons or [],
            },
            "data": data or {},
        }
        th[0][1].append(script)
        return self

    def add_mvu_core_script(self):
        """Add MVU core script."""
        return self.add_tavern_script(
            name="MVU",
            content=DEFAULT_MVU_BUNDLE,
            buttons=DEFAULT_MVU_BUTTONS,
        )

    def add_mvu_schema_script(self, schema_js, name="Variable schema"):
        """Add MVU ZOD variable schema script."""
        return self.add_tavern_script(
            name=name,
            content=schema_js,
            buttons=[],
        )

    # === Output ===
    def build(self):
        """Build and return the full character card JSON dict."""
        self.card["create_date"] = now_iso()
        # Ensure top-level field mirrors
        data = self.card["data"]
        self.card["name"] = data["name"]
        self.card["description"] = data["description"]
        self.card["first_mes"] = data["first_mes"]
        return self.card

    def to_json_string(self, indent=2, ensure_ascii=False):
        return json.dumps(self.build(), indent=indent, ensure_ascii=ensure_ascii)

    def save(self, filepath, indent=2):
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.build(), f, indent=indent, ensure_ascii=False)
        return filepath


# ============================================================
# CardConfig: JSON config loading
# ============================================================

class CardConfig:
    """Load character card definition from JSON config and apply it to CardBuilder."""

    def __init__(self, config_dict):
        self.cfg = config_dict

    @classmethod
    def from_file(cls, filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return cls(json.load(f))

    def apply_to(self, builder: CardBuilder):
        """Apply config to CardBuilder."""
        c = self.cfg
        if not isinstance(c, dict):
            raise ValueError("Config must be a JSON object")

        # === Input validation ===
        card = c.get("card", {}) or {}
        if not card.get("name"):
            raise ValueError("Missing required field: card.name")

        # MVU style conflict detection
        mvu = c.get("mvu", {})
        if mvu.get("enabled"):
            schema = mvu.get("schema_script", "")
            has_zod_style = "registerMvuSchema" in schema
            has_beta_style = any(kw in schema for kw in ["_.add(", "_.set(", "getvar("])
            if has_zod_style and has_beta_style:
                raise ValueError(
                    "MVU style conflict: schema_script contains both MVU zod (registerMvuSchema) "
                    "and MVU beta (_.add/_.set/getvar) code. "
                    "The two styles are incompatible; please use only one."
                )

            first_mes = card.get("first_mes", "")
            if first_mes and "<StatusPlaceHolderImpl/>" not in first_mes:
                print("[WARN] MVU is enabled but default opening (first_mes) is missing <StatusPlaceHolderImpl/>")
            for i, g in enumerate(card.get("alternate_greetings", [])):
                if g and "<StatusPlaceHolderImpl/>" not in g:
                    print(f"[WARN] alternate_greeting #{i+2} missing <StatusPlaceHolderImpl/>")

        # === Basic info ===
        if card:
            builder.set_card_info(
                name=card.get("name"),
                description=card.get("description", ""),
                personality=card.get("personality", ""),
                scenario=card.get("scenario", ""),
                creator_notes=card.get("creator_notes", ""),
                system_prompt=card.get("system_prompt", ""),
                post_history_instructions=card.get("post_history_instructions", ""),
                creator=card.get("creator", ""),
                version=card.get("character_version", "1.0"),
            )

        # === Extensions ===
        ext = c.get("extensions", {})
        if ext.get("talkativeness"):
            builder.set_talkativeness(ext["talkativeness"])

        # === Openings ===
        if card.get("first_mes"):
            builder.set_first_message(card["first_mes"])
        for g in card.get("alternate_greetings", []):
            builder.add_alternate_greeting(g)

        # === World book ===
        wb = c.get("worldbook", {})
        if wb.get("name"):
            builder.set_worldbook_name(wb["name"])
        for entry in wb.get("entries", []):
            builder.add_worldbook_entry(
                comment=entry.get("comment", ""),
                content=entry.get("content", ""),
                keys=parse_key_list(entry.get("keys", [])),
                secondary_keys=parse_key_list(entry.get("secondary_keys", [])),
                constant=entry.get("constant", True),
                position=entry.get("position", "after_char"),
                position_num=entry.get("extensions", {}).get("position",
                    _position_str_to_num(entry.get("position", "after_char"))),
                order=entry.get("order", entry.get("insertion_order", 100)),
                enabled=entry.get("enabled", True),
                depth=entry.get("extensions", {}).get("depth", 4),
            )

        # === Regex scripts ===
        for rs in c.get("regex_scripts", []):
            builder.add_regex_script(
                name=rs.get("name", rs.get("scriptName", "")),
                find_regex=rs.get("findRegex"),
                replace_string=rs.get("replaceString", ""),
                markdown_only=rs.get("markdownOnly", True),
                prompt_only=rs.get("promptOnly", False),
                placement=rs.get("placement", [2]),
                min_depth=rs.get("minDepth"),
                max_depth=rs.get("maxDepth"),
                run_on_edit=rs.get("runOnEdit", False),
                substitute_regex=rs.get("substituteRegex", 0),
            )

        # === Tavern helper scripts ===
        th = c.get("tavern_helper", {})
        for script in th.get("scripts", []):
            builder.add_tavern_script(
                name=script.get("name", ""),
                content=script.get("content", ""),
                enabled=script.get("enabled", True),
                buttons=script.get("buttons", []),
            )

        # === MVU specific (quick config) ===
        mvu = c.get("mvu", {})
        if mvu.get("enabled"):
            if mvu.get("schema_script"):
                builder.add_mvu_schema_script(mvu["schema_script"])
            builder.add_mvu_core_script()
            if mvu.get("initvar"):
                builder.add_initvar_entry(mvu["initvar"])
            if mvu.get("variable_list_path") is not False:
                builder.add_variable_list_entry(
                    mvu.get("variable_list_path", "stat_data"))
            if mvu.get("update_rules"):
                builder.add_variable_update_rules(mvu["update_rules"])
            if mvu.get("output_format"):
                builder.add_variable_output_format(mvu["output_format"])
            else:
                builder.add_variable_output_format()
            if mvu.get("hide_regex", True):
                builder.add_mvu_hide_regex()
            if mvu.get("beautify_regex", True):
                builder.add_mvu_beautify_full_regex()
                builder.add_mvu_beautify_partial_regex()

        # === Status bar ===
        statusbar = c.get("statusbar", {})
        if statusbar.get("enabled"):
            html = statusbar.get("html", "")
            if not html:
                raise ValueError("statusbar.enabled=true but statusbar.html was not provided")
            builder.add_statusbar_regex(html)
            if statusbar.get("hide_regex", True):
                builder.add_statusbar_hide_regex()

        return builder


# ============================================================
# CardConfig: JSON config loading
# ============================================================

def _position_str_to_num(pos_str):
    """Convert position string to number."""
    mapping = {"before_char": 0, "after_char": 1, "at_depth": 4}
    return mapping.get(pos_str, 1)
# InteractiveCLI: Interactive creation
# ============================================================

class InteractiveCLI:
    """Interactive character card creation in CLI."""

    def __init__(self):
        self.builder = CardBuilder()

    def _input(self, prompt, default=None):
        if default:
            val = input(f"{prompt} [{default}]: ").strip()
            return val if val else default
        return input(f"{prompt}: ").strip()

    def _input_yn(self, prompt, default="n"):
        val = input(f"{prompt} (y/n) [{default}]: ").strip().lower()
        if not val:
            val = default
        return val == "y" or val == "yes"

    def _input_multiline(self, prompt):
        print(f"{prompt} (enter an empty line to finish):")
        lines = []
        while True:
            line = input()
            if line == "" and lines:
                break
            lines.append(line)
        return "\n".join(lines)

    def run(self):
        print("\n=== SillyTavern Character Card Generator (Interactive Mode) ===\n")

        # 1. Character name
        name = self._input("Character card name")
        self.builder.set_name(name)

        # 2. Author
        creator = self._input("Author name", "")
        if creator:
            self.builder.set_card_info(creator=creator)

        # 3. Character description
        desc = self._input_multiline("Character description (YAML format)")
        if desc:
            self.builder.set_card_info(description=desc)

        # 4. Personality
        personality = self._input("Personality summary (optional)", "")
        if personality:
            self.builder.set_card_info(personality=personality)

        # 5. World book
        if self._input_yn("Do you need a world book?"):
            wb_name = self._input("World book name", f"{name}_worldbook")
            self.builder.set_worldbook_name(wb_name)
            print("  (You can batch-add entries later in JSON config)")

        # 6. MVU
        if self._input_yn("Do you need the MVU ZOD variable system?"):
            print("  MVU complexity: (1) Simple affinity (2) Full game system")
            choice = self._input("  Select", "1")
            self._setup_mvu(choice)

        # 7. Beautification
        if self._input_yn("Do you need HTML beautification?"):
            self._setup_beautify()

        # 8. Openings
        self._setup_openings()

        # 9. Save
        out_name = self._input("Output filename", f"{name}.json")
        if not out_name.endswith(".json"):
            out_name += ".json"
        self.builder.save(out_name)
        print(f"\n Character card generated: {out_name}")

    def _setup_mvu(self, choice):
        # MVU core script
        self.builder.add_mvu_core_script()

        if choice == "1":
            schema = (
                "import { registerMvuSchema } from "
                "'https://testingcf.jsdelivr.net/gh/StageDog/tavern_resource/dist/util/mvu_zod.js';\n\n"
                "export const Schema = z.object({\n"
                "  Character: z.object({\n"
                "    Affinity: z.coerce.number().transform(v => _.clamp(v, 0, 100)).prefault(20),\n"
                "    Mood: z.string().prefault('Calm'),\n"
                "  }),\n"
                "});\n\n"
                "$(() => { registerMvuSchema(Schema); });"
            )
            self.builder.add_mvu_schema_script(schema)
            self.builder.add_initvar_entry(
                "Character:\n  Affinity: 20\n  Mood: Calm\n")
            self.builder.add_variable_list_entry()
            self.builder.add_variable_update_rules(
                "---\nVariable update rules:\n  Character:\n    Affinity:\n      type: number\n      range: 0~100\n      check:\n        - Adjust by +/- (3~6) based on interaction\n    Mood:\n      check:\n        - Update based on scene atmosphere\n")
            self.builder.add_variable_output_format()
        else:
            # Full game system provides a framework; user fills in details.
            print("  (Please edit the JSON config file yourself for full game system schema)")

        self.builder.add_mvu_hide_regex()
        self.builder.add_mvu_beautify_full_regex()
        self.builder.add_mvu_beautify_partial_regex()

    def _setup_beautify(self):
        # Interactive mode uses plain text to show variable values. Provide HTML beautification through JSON config.
        html = ("<style>body{margin:0;padding:8px;background:transparent;font-family:sans-serif;"
                "display:flex;justify-content:center;color:#ccc;font-size:13px}"
                ".s{background:rgba(26,26,46,.7);border-radius:10px;padding:10px 14px;"
                "border:1px solid rgba(255,182,193,.15)}"
                ".r{display:flex;justify-content:space-between;padding:3px 0}</style>"
                "<div class='s'>"
                "<div class='r'><span>Affinity</span><span>"
                "{{" + "format_message_variable::stat_data.Character.Affinity" + "}}</span></div>"
                "<div class='r'><span>Mood</span><span>"
                "{{" + "format_message_variable::stat_data.Character.Mood" + "}}</span></div>"
                "</div>")
        self.builder.add_statusbar_regex(html)
        self.builder.add_statusbar_hide_regex()

    def _setup_openings(self):
        n = int(self._input("Number of openings (1-5)", "3"))
        default_opening = (
            f"[2026][Morning]\n\n"
            f"A new day has begun.\n\n"
            f"<StatusPlaceHolderImpl/>"
        )
        opening = self._input_multiline("Default opening (can be edited later in JSON)")
        self.builder.set_first_message(opening if opening else default_opening)

        for i in range(n):
            print(f"\n  Opening {i+2}:")
            text = self._input_multiline(f"  Content (or press Enter to skip)")
            if text:
                text += "\n<StatusPlaceHolderImpl/>"
                self.builder.add_alternate_greeting(text)


# ============================================================
# Extract mode: extract config template from existing character card
# ============================================================

def extract_template(card_path, output_path):
    """Extract editable config template from an existing character card JSON."""
    with open(card_path, "r", encoding="utf-8") as f:
        card = json.load(f)

    data = card.get("data", {})
    ext = data.get("extensions", {})
    wb = data.get("character_book", {})

    template = {
        "card": {
            "name": data.get("name", ""),
            "description": data.get("description", ""),
            "personality": data.get("personality", ""),
            "scenario": data.get("scenario", ""),
            "first_mes": data.get("first_mes", ""),
            "creator_notes": data.get("creator_notes", ""),
            "system_prompt": data.get("system_prompt", ""),
            "creator": data.get("creator", ""),
            "character_version": data.get("character_version", "1.0"),
            "alternate_greetings": data.get("alternate_greetings", []),
        },
        "extensions": {
            "talkativeness": ext.get("talkativeness", "0.5"),
            "world": ext.get("world", ""),
        },
        "worldbook": {
            "name": wb.get("name", ""),
            "entries": [
                {
                    "comment": e.get("comment", ""),
                    "keys": e.get("keys", []),
                    "content": e.get("content", ""),
                    "constant": e.get("constant", True),
                    "position": e.get("position", "after_char"),
                    "order": e.get("insertion_order", 100),
                    "enabled": e.get("enabled", True),
                }
                for e in wb.get("entries", [])
            ],
        },
        "regex_scripts": [],
        "tavern_helper": {"scripts": []},
        "mvu": {"enabled": False},
    }

    # Regex scripts
    for rs in ext.get("regex_scripts", []):
        template["regex_scripts"].append({
            "name": rs.get("scriptName", ""),
            "findRegex": rs.get("findRegex", ""),
            "replaceString": rs.get("replaceString", ""),
            "markdownOnly": rs.get("markdownOnly", True),
            "promptOnly": rs.get("promptOnly", False),
            "placement": rs.get("placement", [2]),
            "minDepth": rs.get("minDepth"),
            "runOnEdit": rs.get("runOnEdit", False),
        })

    # Tavern helper
    th = ext.get("tavern_helper", [])
    if isinstance(th, list) and len(th) > 0 and isinstance(th[0], list) and len(th[0]) > 1:
        for s in th[0][1]:
            template["tavern_helper"]["scripts"].append({
                "name": s.get("name", ""),
                "content": s.get("content", ""),
            })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(template, f, indent=2, ensure_ascii=False)
    return output_path


# ============================================================
# Validation mode
# ============================================================

def validate_card(card_path):
    """Validate character card JSON."""
    errors = []
    warnings = []

    try:
        with open(card_path, "r", encoding="utf-8") as f:
            card = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        return [f"Unable to read file: {e}"], []

    # Basic structure checks
    if "spec" not in card:
        errors.append("Missing spec field")
    if card.get("spec") != "chara_card_v3":
        warnings.append(f"spec is not chara_card_v3: {card.get('spec')}")
    if "data" not in card:
        errors.append("Missing data object")

    data = card.get("data", {})
    if "name" not in data:
        errors.append("Missing data.name")
    if "extensions" not in data:
        errors.append("Missing data.extensions")

    # Check world book entries
    wb = data.get("character_book", {})
    entries = wb.get("entries", [])
    if entries is None:
        entries = []
    for i, e in enumerate(entries):
        if not e.get("content") or not str(e.get("content", "")).strip():
            errors.append(f"World book entry {i} ({e.get('comment','')}) has empty content")
        ext = e.get("extensions", {})
        if not ext.get("prevent_recursion"):
            warnings.append(f"World book entry {i} ({e.get('comment','')}) prevent_recursion=false")
        if not ext.get("exclude_recursion"):
            warnings.append(f"World book entry {i} ({e.get('comment','')}) exclude_recursion=false")
        # Position validity check (SillyTavern position range is 0-7; invalid values are silently skipped by switch default)
        pos = ext.get("position", e.get("position", -1))
        if isinstance(pos, str):
            pos = {"before_char": 0, "after_char": 1, "at_depth": 4}.get(pos, -1)
        if isinstance(pos, (int, float)) and (pos < 0 or pos > 7):
            errors.append(f"World book entry {i} ({e.get('comment','')}) position={pos} is out of 0-7 range; SillyTavern will silently skip this entry")
        # keys format check (Chinese punctuation or separators can cause keyword matching failures)
        for k in e.get("keys", []):
            if isinstance(k, str) and ('\\uFF0C' in k or '\\u3001' in k):
                warnings.append(f"World book entry {i} ({e.get('comment','')}) keys contain Chinese punctuation: '{k}'; use English commas to separate keywords in SillyTavern")

    ext = data.get("extensions", {})
    for i, rs in enumerate(ext.get("regex_scripts", [])):
        if not rs.get("findRegex"):
            warnings.append(f"Regex {i} ({rs.get('scriptName','')}) has empty findRegex")

    return errors, warnings


# ============================================================
# Decompile: unpack character card into config JSON
# ============================================================

def _detect_mvu_config(card):
    """Detect MVU config from character card JSON."""
    data = card.get("data", {})
    wb = data.get("character_book", {})
    ext = data.get("extensions", {})
    th = ext.get("tavern_helper", [])

    mvu = {"enabled": False}

    scripts_list = []
    if isinstance(th, list) and len(th) > 0 and isinstance(th[0], list) and len(th[0]) > 1:
        scripts_list = th[0][1]
    elif isinstance(th, dict):
        scripts_list = th.get("scripts", [])

    for s in scripts_list:
        content = s.get("content", "")
        if "bundle.js" in content and ("MagVarUpdate" in content):
            mvu["enabled"] = True
    if not mvu.get("enabled"):
        return mvu

    for s in scripts_list:
        content = s.get("content", "")
        if "registerMvuSchema" in content:
            mvu["schema_script"] = content
            break

    entries = wb.get("entries", [])
    for e in entries:
        comment = e.get("comment", "")
        content = e.get("content", "")
        if "[initvar]" in comment:
            inner = content
            if inner.strip().startswith("<initvar>"):
                inner = inner[inner.index("<initvar>") + len("<initvar>"):]
            if inner.strip().endswith("</initvar>"):
                inner = inner[:inner.rindex("</initvar>")]
            mvu["initvar"] = inner.strip()
        if "Variable list" in comment or ("format_message_variable" in content and "status_current_variable" in content):
            mvu["variable_list_path"] = "stat_data"
        if "[mvu_update]" in comment and ("rules" in comment.lower() or "rule" in comment.lower()):
            mvu["update_rules"] = content
        if "[mvu_update]" in comment and "format" in comment.lower():
            mvu["output_format"] = content

    mvu["hide_regex"] = False
    mvu["beautify_regex"] = False
    for rs in ext.get("regex_scripts", []):
        fr = rs.get("findRegex", "").lower()
        if "updatevariable" in fr:
            if rs.get("promptOnly") and rs.get("replaceString", "") == "":
                mvu["hide_regex"] = True
            if rs.get("markdownOnly") and "details" in rs.get("replaceString", ""):
                mvu["beautify_regex"] = True

    return mvu


def _detect_statusbar_config(card):
    """Detect status bar config from character card JSON."""
    ext = card.get("data", {}).get("extensions", {})
    statusbar = {"enabled": False}

    for rs in ext.get("regex_scripts", []):
        fr = rs.get("findRegex", "")
        replace = rs.get("replaceString", "")
        if "StatusPlaceHolderImpl" in fr:
            if replace and not rs.get("promptOnly"):
                statusbar["enabled"] = True
                statusbar["html"] = replace
            if not replace and rs.get("promptOnly"):
                statusbar["hide_regex"] = True

    return statusbar


def decompile_card(card_path, output_path):
    """Unpack character card JSON into a complete editable config JSON (compatible with --config input format)."""
    with open(card_path, "r", encoding="utf-8") as f:
        card = json.load(f)

    data = card.get("data", {})
    ext = data.get("extensions", {})
    wb = data.get("character_book", {})

    template = {
        "card": {
            "name": data.get("name", ""),
            "description": data.get("description", ""),
            "personality": data.get("personality", ""),
            "scenario": data.get("scenario", ""),
            "first_mes": data.get("first_mes", ""),
            "creator_notes": data.get("creator_notes", ""),
            "system_prompt": data.get("system_prompt", ""),
            "post_history_instructions": data.get("post_history_instructions", ""),
            "creator": data.get("creator", ""),
            "character_version": data.get("character_version", "1.0"),
            "alternate_greetings": data.get("alternate_greetings", []),
        },
        "extensions": {
            "talkativeness": ext.get("talkativeness", "0.5"),
            "world": ext.get("world", ""),
        },
        "worldbook": {
            "name": wb.get("name", ""),
            "entries": [],
        },
        "regex_scripts": [],
        "tavern_helper": {"scripts": []},
        "mvu": _detect_mvu_config(card),
        "statusbar": _detect_statusbar_config(card),
    }

    mvu_enabled = template["mvu"].get("enabled", False)

    def _is_mvu_entry(comment, content):
        if "[initvar]" in comment:
            return True
        if "Variable list" in comment or ("format_message_variable" in content and "status_current_variable" in content):
            return True
        if "[mvu_update]" in comment and ("rules" in comment.lower() or "rule" in comment.lower()):
            return True
        if "[mvu_update]" in comment and "format" in comment.lower():
            return True
        return False

    for e in wb.get("entries", []):
        entry_comment = e.get("comment", "")
        entry_content = e.get("content", "")
        if mvu_enabled and _is_mvu_entry(entry_comment, entry_content):
            continue
        entry_ext = e.get("extensions", {})
        template["worldbook"]["entries"].append({
            "comment": entry_comment,
            "keys": e.get("keys", []),
            "secondary_keys": e.get("secondary_keys", []),
            "content": entry_content,
            "constant": e.get("constant", True),
            "position": e.get("position", "after_char"),
            "order": e.get("insertion_order", 100),
            "enabled": e.get("enabled", True),
            "depth": entry_ext.get("depth", 4),
            "prevent_recursion": entry_ext.get("prevent_recursion", True),
            "exclude_recursion": entry_ext.get("exclude_recursion", True),
        })

    for rs in ext.get("regex_scripts", []):
        template["regex_scripts"].append({
            "name": rs.get("scriptName", ""),
            "findRegex": rs.get("findRegex", ""),
            "replaceString": rs.get("replaceString", ""),
            "markdownOnly": rs.get("markdownOnly", True),
            "promptOnly": rs.get("promptOnly", False),
            "placement": rs.get("placement", [2]),
            "minDepth": rs.get("minDepth"),
            "maxDepth": rs.get("maxDepth"),
            "runOnEdit": rs.get("runOnEdit", False),
            "substituteRegex": rs.get("substituteRegex", 0),
        })

    th = ext.get("tavern_helper", [])
    scripts_list = []
    if isinstance(th, list) and len(th) > 0 and isinstance(th[0], list) and len(th[0]) > 1:
        scripts_list = th[0][1]
    elif isinstance(th, dict):
        scripts_list = th.get("scripts", [])

    for s in scripts_list:
        buttons = []
        btn_cfg = s.get("button", {})
        for b in btn_cfg.get("buttons", []):
            buttons.append({"name": b.get("name", ""), "visible": b.get("visible", True)})
        template["tavern_helper"]["scripts"].append({
            "name": s.get("name", ""),
            "content": s.get("content", ""),
            "enabled": s.get("enabled", True),
            "buttons": buttons,
        })

    # Cleanup: MVU/Statusbar scripts and regex are already captured in dedicated sections, so exclude them from generic lists
    if template["mvu"].get("enabled"):
        mvu_bundle_patterns = ["bundle.js", "MagVarUpdate"]
        mvu_schema_pattern = "registerMvuSchema"
        template["tavern_helper"]["scripts"] = [
            s for s in template["tavern_helper"]["scripts"]
            if not any(p in s["content"] for p in mvu_bundle_patterns) and mvu_schema_pattern not in s["content"]
        ]
        template["regex_scripts"] = [
            r for r in template["regex_scripts"]
            if "updatevariable" not in r.get("findRegex", "").lower()
        ]

    if template["statusbar"].get("enabled"):
        template["regex_scripts"] = [
            r for r in template["regex_scripts"]
            if "StatusPlaceHolderImpl" not in r.get("findRegex", "")
        ]

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(template, f, indent=2, ensure_ascii=False)
    return output_path


# ============================================================
# Edit: in-place character card editing
# ============================================================

def edit_card(card_path, *, name=None, description=None, personality=None,
              scenario=None, first_mes=None, creator_notes=None, creator=None,
              talkativeness=None, add_greeting=None, enable_mvu=None,
              enable_statusbar=None):
    """Edit fields in-place in a character card JSON file."""
    with open(card_path, "r", encoding="utf-8") as f:
        card = json.load(f)

    data = card.get("data", {})
    ext = data.get("extensions", {})

    top_fields = {
        "name": name, "description": description,
        "personality": personality, "scenario": scenario,
        "first_mes": first_mes,
    }
    for k, v in top_fields.items():
        if v is not None:
            card[k] = v
            if k in data:
                data[k] = v

    if creator_notes is not None:
        data["creator_notes"] = creator_notes
    if creator is not None:
        data["creator"] = creator
    if talkativeness is not None:
        card["talkativeness"] = str(talkativeness)
        ext["talkativeness"] = str(talkativeness)

    if add_greeting is not None:
        if "alternate_greetings" not in data:
            data["alternate_greetings"] = []
        data["alternate_greetings"].append(add_greeting)

    if enable_mvu is not None:
        builder = CardBuilder()
        if enable_mvu:
            builder.card = card
            builder.add_mvu_core_script()
            scheme_type = input("MVU complexity (1=Simple affinity 2=Full game system) [1]: ").strip() or "1"
            if scheme_type == "1":
                schema_js = (
                    "import { registerMvuSchema } from "
                    "'https://testingcf.jsdelivr.net/gh/StageDog/tavern_resource/dist/util/mvu_zod.js';\n\n"
                    "export const Schema = z.object({\n"
                    "  Character: z.object({\n"
                    "    Affinity: z.coerce.number().transform(v => _.clamp(v, 0, 100)).prefault(20),\n"
                    "    Mood: z.string().prefault('Calm'),\n"
                    "  }),\n"
                    "});\n\n"
                    "$(() => { registerMvuSchema(Schema); });"
                )
                builder.add_mvu_schema_script(schema_js)
                builder.add_initvar_entry("Character:\n  Affinity: 20\n  Mood: Calm\n")
                builder.add_variable_list_entry()
                builder.add_variable_update_rules(
                    "---\nVariable update rules:\n  Character:\n    Affinity:\n      type: number\n      range: 0~100\n      check:\n        - Adjust by +/- (3~6) based on interaction\n    Mood:\n      check:\n        - Update based on scene atmosphere\n")
                builder.add_variable_output_format()
            builder.add_mvu_hide_regex()
            builder.add_mvu_beautify_full_regex()
            builder.add_mvu_beautify_partial_regex()
        card = builder.build()

    if enable_statusbar is not None:
        builder = CardBuilder()
        builder.card = card
        if enable_statusbar:
            name_val = data.get("name", "Character")
            html = (
                "<style>body{margin:0;padding:8px;background:transparent;font-family:'Noto Sans SC',sans-serif;"
                "display:flex;justify-content:center;color:#e0e0e0;font-size:13px}"
                ".s{background:linear-gradient(145deg,#1a1a2e,#16213e);border-radius:12px;padding:12px 16px;"
                "box-shadow:0 4px 20px rgba(0,0,0,.3);backdrop-filter:blur(10px);min-width:280px}"
                ".r{display:flex;justify-content:space-between;align-items:center;padding:5px 0;"
                "border-bottom:1px solid rgba(255,255,255,.06)}"
                ".bar{flex:1;height:5px;background:rgba(255,255,255,.1);border-radius:3px;margin:0 10px;overflow:hidden}"
                ".fill{height:100%;background:linear-gradient(90deg,#ff6b9d,#c44dff);border-radius:3px;"
                "transition:width .5s ease}</style>"
                f"<div class='s'>"
                f"<div class='r'><span>Affinity</span><div class='bar'><div class='fill' style='width:{{{{format_message_variable::stat_data.{name_val}.Affinity}}}}%'></div></div>"
                f"<span>{{{{format_message_variable::stat_data.{name_val}.Affinity}}}}/100</span></div>"
                f"<div class='r'><span>Mood</span><span>{{{{format_message_variable::stat_data.{name_val}.Mood}}}}</span></div>"
                f"</div>"
            )
            builder.add_statusbar_regex(html)
            builder.add_statusbar_hide_regex()
        card = builder.build()

    card["create_date"] = now_iso()
    with open(card_path, "w", encoding="utf-8") as f:
        json.dump(card, f, indent=2, ensure_ascii=False)
    return card_path


# ============================================================
# List: character card summary
# ============================================================

def list_card(card_path):
    """List key summary information for a character card."""
    with open(card_path, "r", encoding="utf-8") as f:
        card = json.load(f)

    data = card.get("data", {})
    ext = data.get("extensions", {})
    wb = data.get("character_book", {})

    print(f"Character card: {os.path.abspath(card_path)}")
    print(f"  Name: {data.get('name', '')}")
    print(f"  Version: {data.get('character_version', '')}")
    print(f"  Author: {data.get('creator', '')}")
    print(f"  Description length: {len(data.get('description', ''))} chars")
    print(f"  Default opening length: {len(data.get('first_mes', ''))} chars")
    print(f"  Alternate openings: {len(data.get('alternate_greetings', []))}")
    print(f"  World name: {ext.get('world', '')}")
    print()

    entries = wb.get("entries", [])
    print(f"  World book: {wb.get('name', '')} (total {len(entries)} entries)")
    for i, e in enumerate(entries):
        pos_map = {"before_char": "UpChar", "after_char": "DownChar", "at_depth": "@D"}
        pos_label = pos_map.get(e.get("position", ""), e.get("position", "?"))
        light = "Blue light" if e.get("constant") else "Green light"
        status = "Disabled" if not e.get("enabled", True) else "Enabled"
        entry_ext = e.get("extensions", {})
        print(f"    [{i}] {e.get('comment', '')[:50]} | pos={pos_label} | {light} | {status} | "
              f"preventRec={entry_ext.get('prevent_recursion', False)} | "
              f"excludeRec={entry_ext.get('exclude_recursion', False)}")

    regex_scripts = ext.get("regex_scripts", [])
    print(f"\n  Regex scripts: {len(regex_scripts)}")
    for i, rs in enumerate(regex_scripts):
        md = "Beautify" if rs.get("markdownOnly") else ""
        pt = "Hidden" if rs.get("promptOnly") else ""
        tags = "/".join(filter(None, [md, pt])) or "General"
        print(f"    [{i}] {rs.get('scriptName', '')[:40]} | {tags} | placement={rs.get('placement')}")

    th = ext.get("tavern_helper", [])
    scripts_list = []
    if isinstance(th, list) and len(th) > 0 and isinstance(th[0], list) and len(th[0]) > 1:
        scripts_list = th[0][1]
    elif isinstance(th, dict):
        scripts_list = th.get("scripts", [])
    print(f"\n  Tavern helper scripts: {len(scripts_list)}")
    for i, s in enumerate(scripts_list):
        print(f"    [{i}] {s.get('name', '')[:30]} | enabled={s.get('enabled', True)}")

    errors, warnings = validate_card(card_path)
    if errors:
        print(f"\n  Validation errors: {len(errors)}")
        for e in errors:
            print(f"    [ERROR] {e}")
    if warnings:
        print(f"  Validation warnings: {len(warnings)}")
        for w in warnings:
            print(f"    [WARN] {w}")
    if not errors and not warnings:
        print(f"\n  Validation: [OK]")


# ============================================================
# CLI entry
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="SillyTavern chara_card_v3 character card generator - supports create/decompile/edit/validate",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate from config
  python card-generator.py --config config.json --output card.json

  # Interactive creation
  python card-generator.py --interactive

  # Decompile character card into editable config (with MVU/statusbar detection)
  python card-generator.py --decompile card.json -o template.json

  # Show character card summary
  python card-generator.py --list card.json

  # Edit character card fields in place
  python card-generator.py card.json --edit --name "new_name" --description "new description"

  # Validate character card
  python card-generator.py --validate card.json

  # Extract simple template (legacy-compatible argument)
  python card-generator.py --extract existing.json -o template.json
        """
    )

    parser.add_argument("card_path", nargs="?", help="Character card JSON path (for edit/list modes)")
    parser.add_argument("--config", "-c", help="JSON config file path")
    parser.add_argument("--output", "-o", help="Output JSON file path", default="output.json")
    parser.add_argument("--interactive", "-i", action="store_true", help="Interactive creation")
    parser.add_argument("--extract", "-e", help="Extract simple config template from existing character card")
    parser.add_argument("--decompile", "-d", help="Decompile character card into complete editable config (with MVU/statusbar detection)")
    parser.add_argument("--validate", "-v", help="Validate character card JSON")
    parser.add_argument("--list", "-l", action="store_true", help="List character card summary")

    # Edit mode arguments
    parser.add_argument("--edit", action="store_true", help="Edit character card fields in place")
    parser.add_argument("--name", help="Character card name")
    parser.add_argument("--description", help="Character description")
    parser.add_argument("--personality", help="Personality")
    parser.add_argument("--scenario", help="Scenario")
    parser.add_argument("--first-mes", dest="first_mes", help="Default opening message")
    parser.add_argument("--creator-notes", dest="creator_notes", help="Creator notes")
    parser.add_argument("--creator", help="Author name")
    parser.add_argument("--talkativeness", help="Talkativeness (e.g. 0.5)")
    parser.add_argument("--add-greeting", dest="add_greeting", help="Append one alternate greeting")
    parser.add_argument("--enable-mvu", dest="enable_mvu", type=lambda x: x.lower() in ("true", "1", "yes"),
                        help="Enable/disable MVU variable system (true/false)")
    parser.add_argument("--enable-statusbar", dest="enable_statusbar", type=lambda x: x.lower() in ("true", "1", "yes"),
                        help="Add/remove status bar beautification (true/false)")

    args = parser.parse_args()

    # --list
    if args.list:
        if not args.card_path:
            print("Error: --list requires a character card path", file=sys.stderr)
            sys.exit(1)
        list_card(args.card_path)
        return

    # --edit
    if args.edit:
        if not args.card_path:
            print("Error: --edit requires a character card path", file=sys.stderr)
            sys.exit(1)
        print(f"Editing character card: {args.card_path}")
        edit_card(
            args.card_path,
            name=args.name,
            description=args.description,
            personality=args.personality,
            scenario=args.scenario,
            first_mes=args.first_mes,
            creator_notes=args.creator_notes,
            creator=args.creator,
            talkativeness=args.talkativeness,
            add_greeting=args.add_greeting,
            enable_mvu=args.enable_mvu,
            enable_statusbar=args.enable_statusbar,
        )
        print("Edit complete")
        if args.list:
            list_card(args.card_path)
        return

    # --decompile
    if args.decompile:
        out = args.output if args.output != "output.json" else args.decompile.replace(".json", "_config.json")
        path = decompile_card(args.decompile, out)
        print(f"Config decompiled to: {path}")
        return

    # --extract (legacy-compatible, simple extraction)
    if args.extract:
        out = args.output if args.output != "output.json" else args.extract.replace(".json", "_template.json")
        path = extract_template(args.extract, out)
        print(f"Template extracted to: {path}")
        return

    # --validate
    if args.validate:
        errors, warnings = validate_card(args.validate)
        if errors:
            print("Errors:")
            for e in errors:
                print(f"  [ERROR] {e}")
        if warnings:
            print("Warnings:")
            for w in warnings:
                print(f"  [WARN] {w}")
        if not errors and not warnings:
            print("Validation passed [OK]")
        return 1 if errors else 0

    # --interactive
    if args.interactive:
        cli = InteractiveCLI()
        cli.run()
        return

    # --config
    if args.config:
        config = CardConfig.from_file(args.config)
        builder = CardBuilder()
        config.apply_to(builder)
        builder.save(args.output)
        print(f"Character card generated: {args.output}")
        return

    parser.print_help()


if __name__ == "__main__":
    sys.exit(main() or 0)
