# Position Reference

Sourced from SillyTavern `public/scripts/world-info.js:855-864`.

| Value | Label | JS Constant | Description |
|-------|-------|-------------|-------------|
| 0 | ↑Char | `world_info_position.before` | charactertranslated text — Before character definitions |
| 1 | ↓Char | `world_info_position.after` | charactertranslated text — After character definitions |
| 2 | ↑AT | `world_info_position.ANTop` | Author's Note translated text — Before Author's Note |
| 3 | ↓AT | `world_info_position.ANBottom` | Author's Note translated text — After Author's Note |
| 4 | @D | `world_info_position.atDepth` | translated text — At specific depth in chat |
| 5 | ↑EM | `world_info_position.EMTop` | exampletranslated text — Before Example Messages |
| 6 | ↓EM | `world_info_position.EMBottom` | exampletranslated text — After Example Messages |
| 7 | Outlet | `world_info_position.outlet` | outputtranslated text Outlet — Requires `--outlet-name` |

## Recommended usage

| Entry type | Position | Reason |
|------------|----------|--------|
| worldview outline, background setting, translated textrules | 0 (↑Char) | AI needs world framework before character info |
| charactertranslated text (multi-character) | 0 (↑Char) | Macro-level: what characters exist |
| charactertranslated text (all) | 1 (↓Char) | Supplements character description, placed after it |
| NPC translated text | 1 (↓Char) | Supports character details, keyword-triggered |
| scenario/translated text/item | 1 (↓Char) | Specific details, keyword-triggered |
| translated text/translated text | 2 (↑AT) | Writing rules injected into system prompt area |
| secondary interpretation (behavior correction) | 4 (@D, depth=0) | Last thing AI reads → strongest influence. role=system |
| formattranslated text for examples | 5 (↑EM) or 6 (↓EM) | Wraps example messages |

## What NOT to do

- **Never use D1/D2/D3+ (@D with depth >= 1)**: inserting content between chat messages breaks conversation flow and confuses the AI
- **D0 only for behavior guidance, not for settings**: D0 is for direct instructions like "when X happens, do Y", not for worldbuilding lore
- **All entries must have recursion prevention**: use `--prevent-recursion` for every entry

## Notes

- When using position 7 (Outlet), `--outlet-name` is required
- The `@D` position uses the entry's `depth` value to determine insertion point
- `role` field matters for `@D`: use `--role 0` (system) for D0 behavior instructions
