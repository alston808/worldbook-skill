# scriptusagetranslated text

> translated textdescriptiontranslated text Python scripttranslated textcompletetranslated text. translated textparameters, configurationformat, translated texterrortranslated text. usagetranslated textmusttranslated text. 

## This document covers

>translated text card-generator.py(Character Card JSON generate/unpack/edit/validate/list), query.py(translated textWorld Bookentryquery), world-book-create.py(translated textWorld Booktranslated text)translated textcompletetranslated text. translated textall CLI parameters, config.json fieldtranslated textrelationship, MVU/status bartranslated textgeneratetranslated text, translated text v2 translated text, translated text. 

---

## workflow

### Phase 1: translated textscript

| scenario | script | translated text |
|------|------|---------|
| translated text config.json generateCharacter Card JSON | card-generator.py | `--config` — **translated textmustusagetranslated text** |
| translated textCharacter Cardunpacktranslated textedit config.json | card-generator.py | `--decompile` |
| modifytranslated textCharacter Cardfield | card-generator.py | `--edit` |
| validateCharacter Card JSON translated text | card-generator.py | `--validate` |
| translated textCharacter Cardtranslated text(entrytranslated text/translated text/translated textrecursion) | card-generator.py | `--list` |
| translated text | card-generator.py | `--interactive` |
| extracttranslated text | card-generator.py | `--extract` |
| translated textWorld Bookentry | query.py | default / `--brief` / `--uid` / `--search` / `--resolve` |
| translated text/edit/translated textWorld Bookentry | world-book-create.py | `--add` / `--batch-edit` / `--delete` |

**hard rules: translated text JSON, musttranslated text card-generator.py --config generate. **

---

## card-generator.py — Character Cardgeneratetranslated text(translated text)

### all CLI parameters

```
python card-generator.py # translated text
python card-generator.py --config config.json -o output.json # translated textconfigurationgenerate(translated text)
python card-generator.py --interactive # translated text
python card-generator.py --decompile card.json -o config.json # unpackCharacter Cardtranslated texteditconfiguration
python card-generator.py --extract card.json -o template.json # extracttranslated text(translated textparameters)
python card-generator.py --validate card.json # validateCharacter Cardtranslated text
python card-generator.py --list card.json # translated textCharacter Cardtranslated text
python card-generator.py card.json --edit --name "translated text" # translated textedit
python card-generator.py card.json --edit --add-greeting "translated text" # translated textoptionaltranslated text
python card-generator.py card.json --edit --enable-mvu true # enabledMVU
```

### config.json completefieldtranslated text

```json
{
 "card": {
 "name": "Character Cardname(translated text)",
 "description": "",
 "personality": "",
 "scenario": "",
 "first_mes": "defaultgreeting(translated text<StatusPlaceHolderImpl/>, if anyMVU)",
 "creator_notes": "translated textnotes",
 "system_prompt": "",
 "post_history_instructions": "",
 "creator": "translated text",
 "character_version": "1.0",
 "alternate_greetings": ["translated text2", "translated text3"]
 },
 "extensions": { "talkativeness": "0.5" },
 "worldbook": {
 "name": "World Bookname",
 "entries": [
 {
 "comment": "entrytranslated text",
 "keys": [],
 "secondary_keys": [],
 "content": "entrycontent(XMLtranslated textYAMLformat)",
 "constant": true,
 "position": "before_char",
 "order": 1,
 "enabled": true,
 "depth": 4,
 "prevent_recursion": true,
 "exclude_recursion": true
 }
 ]
 },
 "regex_scripts": [
 {
 "name": "translated textname",
 "findRegex": "/<pattern>/flags",
 "replaceString": "",
 "markdownOnly": true,
 "promptOnly": false,
 "placement": [2],
 "minDepth": null,
 "maxDepth": null,
 "runOnEdit": false,
 "substituteRegex": 0
 }
 ],
 "tavern_helper": {
 "scripts": [
 {
 "name": "scripttranslated text",
 "content": "JScode",
 "enabled": true,
 "buttons": [{"name": "translated text", "visible": true}]
 }
 ]
 },
 "mvu": {
 "enabled": true,
 "schema_script": "completeZod Schema JScode(translated textimport registerMvuSchema + registerMvuSchematranslated text)",
 "initvar": "Character name:\n Affinity: 20\n relationship status: translated text",
 "update_rules": "YAMLformattranslated textvariable update rules",
 "output_format": "optional, translated textusagetranslated textJSON Patchtranslated text",
 "variable_list_path": "stat_data",
 "hide_regex": true,
 "beautify_regex": true
 },
 "statusbar": {
 "enabled": true,
 "html": "<!DOCTYPE html>...completeHTMLstatus barcode...",
 "hide_regex": true
 }
}
```

### card field

| field | type | description |
|------|------|------|
| `name` | string | Character Cardname(translated text) |
| `description` | string | translated text. charactertranslated textalltranslated textWorld Bookentrytranslated text |
| `first_mes` | string | defaulttranslated text. if anyMVU, translated text `<StatusPlaceHolderImpl/>` |
| `alternate_greetings` | string[] | optionaltranslated text |
| `creator` | string | translated text |
| `character_version` | string | translated text |

### worldbook.entries field

| field | type | default | description |
|------|------|------|------|
| `comment` | string | — | entrytranslated text/notes |
| `keys` | array | `[]` | trigger keywords(translated textlist) |
| `secondary_keys` | array | `[]` | translated texttrigger keywords |
| `content` | string | — | entrycontent(XMLtranslated textYAMLformat) |
| `constant` | boolean | `true` | true=translated text, false=translated text |
| `position` | string | `"after_char"` | `"before_char"` / `"after_char"` / `"at_depth"` |
| `order` | number | `100` | translated textorder, translated text |
| `enabled` | boolean | `true` | enabled/disabled |
| `depth` | number | `4` | translated text(position=at_depth translated text) |
| `prevent_recursion` | boolean | `true` | translated textentrytranslated textentry. **musttranslated texttrue** |
| `exclude_recursion` | boolean | `true` | translated textentrytranslated textentry. **musttranslated texttrue** |

**translated textWarning(translated text): **
- position0-7translated text switch translated text default translated textbranch → translated textpositiontranslated textentrytranslated text, translated text
- `getSortedEntries()` translated text `[]` → translated texterrorentrytranslated textWorld Bookentrytranslated text
- translated textfieldtranslated text `addMissingWorldInfoFields()` translated textdefault value(excludeRecursion=false translated textdefault value！)
- **translated text: translated textentrytranslated text `prevent_recursion` translated text `exclude_recursion` musttranslated text true, translated textDependenciesdefault value**

### regex_scripts field

| field | type | default | description |
|------|------|------|------|
| `name` | string | — | translated textname |
| `findRegex` | string | — | slashtranslated text `/pattern/flags`. translated text `/` translated text `\/` |
| `replaceString` | string | `""` | translated textcontent. translated text=hidden |
| `markdownOnly` | boolean | `true` | true=translated text(translated textbeautification), false=AItranslated text |
| `promptOnly` | boolean | `false` | true=translated textTiptranslated textphasetranslated text(translated textAIhiddencontent) |
| `placement` | int[] | `[2]` | [1]=translated textphase, [2]=Tiptranslated textphase |
| `minDepth` | int? | `null` | translated text |
| `maxDepth` | int? | `null` | translated text |
| `runOnEdit` | boolean | `false` | edittranslated text |
| `substituteRegex` | int | `0` | translated text |

**translated textrules: **
- translated textbeautification: `markdownOnly=true, promptOnly=false` — translated textbeautificationtranslated text
- AIhidden: `markdownOnly=false, promptOnly=true` — AItranslated textcontent
- translated text: `[do not send]translated textvariableupdate` translated text `minDepth=4` — translated texthiddentranslated text, translated text3translated textAItranslated text

### tavern_helper.scripts field

| field | type | description |
|------|------|------|
| `name` | string | scriptname |
| `content` | string | completeJScode |
| `enabled` | boolean | enabledstatus |
| `buttons` | object[] | translated textconfiguration: `{"name": "translated text", "visible": true/false}` |

### mvu translated textgeneratetranslated text `mvu.enabled = true` translated text, card-generator.py translated textgeneratetranslated textcontent. **translated text config.json translated text worldbook.entries translated textentry: **

| translated textgenerate | content | configuration |
|---------|------|------|
| MVU translated textscript | bundle.js import | tavern_helper: "MVU", 6translated text |
| Zod Schema script | translated text schema_script field | tavern_helper: "variabletranslated text" |
| [initvar]entry | `<initvar>YAML</initvar>` translated text | position=0 (before_char), enabled=false, order=14720 |
| variable listentry | `<status_current_variable>` + translated text | position=4 (at_depth), depth=0, order=14720 |
| [mvu_update]variable update rules | translated text update_rules field | position=4 (at_depth), depth=0, order=14720 |
| [mvu_update]variableoutputformat | JSON Patch translated text | position=4 (at_depth), depth=0, order=14720 |
| [do not send]translated textvariableupdate translated text | hidden UpdateVariable translated text | promptOnly, minDepth=4 |
| [beautification]completevariableupdate translated text | details translated text | markdownOnly |
| [beautification]variableupdatetranslated text | translated textcompletetranslated textTip | markdownOnly |

**initvar formathard rules(translated texterror3): **
- entryposition: `before_char` (position=0)
- entry enabled=false(disabledstatus)
- contentformat: musttranslated text `<initvar>` translated text YAML, translated text: 
 ```
 <initvar>
 Character name:
 Affinity: 20
 relationship status: translated text
 </initvar>
 ```
- translated text initvar

**variableentrypositionhard rules(translated texterror3): **
- variable update rules: [mvu_update] prefix, position at_depth D0
- variableoutputformat: [mvu_update] prefix, position at_depth D0
- variable list: position at_depth D0
- translated text MVU entry order translated text 14720

### statusbar translated textgeneratetranslated text `statusbar.enabled = true` translated textgenerate: 

| translated textgenerate | configuration |
|---------|------|
| [translated text]status bar translated text | findRegex=`<StatusPlaceHolderImpl/>`, markdownOnly, placement=[2] |
| [do not send]translated text | findRegex=`<StatusPlaceHolderImpl/>`, promptOnly, placement=[2] |

**statusbar.html Notetranslated text(translated texterror4): **
- mustusage `{{format_message_variable::stat_data.path}}` translated textreadMVUvariabletranslated text
- translated textusage `${AFFECTION}` translated text Python translated text
- scripttranslated text HTML translated text, HTML translated textconfigurationfiletranslated text statusbar.html fieldtranslated text
- translated textneedJStranslated text, translated text replaceString translated textincludecompleteHTML+JS(translated text eventOn translated text VARIABLE_UPDATE_ENDED)

### translated text

#### --config(translated textgeneratetranslated text, mustusage)

```bash
python card-generator.py --config config.json -o card.json
```

read config.json, translated textcompletetranslated text chara_card_v3 JSON translated text. translated textcorrecttranslated textgeneratetranslated text. translated textstepstranslated text JSON. 

#### --validate(generatetranslated textmusttranslated text)

```bash
python card-generator.py --validate card.json
```

translated text: 
- spec translated text chara_card_v3
- translated text data translated text data.name
- World Bookentrytranslated text content
- World Bookentrytranslated text prevent_recursion translated text exclude_recursion translated text true(translated text WARN)
- translated textscripttranslated text findRegex translated text(translated text WARN)

#### --list(translated text)

```bash
python card-generator.py --list card.json
```

output: name, translated text, translated text, description/translated text, optionaltranslated text, World Bookentrylist(position/translated text/enabled/translated textrecursion), translated textscriptlist, translated textscriptlist, validatetranslated text. 

#### --decompile(unpack)

```bash
python card-generator.py --decompile card.json -o config.json
```

translated textCharacter Card JSON translated textextractcompleteconfiguration. translated text MVU translated textstatus barconfiguration, outputformattranslated text --config inputformattranslated text. 

#### --edit(translated textedit)

```bash
python card-generator.py card.json --edit --name "translated text"
python card-generator.py card.json --edit --add-greeting "translated text"
python card-generator.py card.json --edit --enable-mvu true
```

supporttranslated texteditparameters: --name, --description, --personality, --scenario, --first-mes, --creator-notes, --creator, --talkativeness, --add-greeting, --enable-mvu, --enable-statusbar

---

## query.py — translated textWorld Bookquery

translated text `.json` World Bookfile. Character Cardtranslated textWorld Booktranslated text card-generator.py --list translated text. 

### all CLI parameters

```bash
query.py <World Book.json> # translated textentrytranslated text
query.py <World Book.json> --brief # translated text(translated textrecursionfield)
query.py <World Book.json> --uid <UID> # translated textentrycompletecontent
query.py <World Book.json> --search "translated text" # translated textentry(translated text/content/translated text)
query.py <World Book.json> --resolve # translated textentrytranslated text @UID/@name translated text
```

### outputfield(--brief translated text)

uid, comment, content_length, content_preview, keys, position, constant, order, depth, scanDepth, preventRecursion, excludeRecursion

---

## world-book-create.py — translated textWorld Booktranslated text Character Cardtranslated textWorld Bookfile. 

### all CLI parameters

```bash
# translated textWorld Book
python world-book-create.py <World Book.json> --init --name "World Bookname"

# translated textentry
python world-book-create.py <World Book.json> --add \
 --comment "entryname" \
 --content "entrycontent(translated text @filepath translated textfileread)" \
 --keys "translated text1,translated text2" \
 --position 0 --order 1 --constant \
 --prevent-recursion --exclude-recursion

# translated texteditentry
python world-book-create.py <World Book.json> --batch-edit --uid 0 --comment "translated textname"

# translated textentry
python world-book-create.py <World Book.json> --delete --uid 0
```

### all flag

| flag | description |
|------|------|
| `--init` | translated textWorld Bookfile |
| `--add` | translated textentry |
| `--batch-edit` | translated textedit(translated text --uid) |
| `--delete` | translated textentry(translated text --uid) |
| `--name "name"` | World Bookname |
| `--comment "name"` | entrytranslated text |
| `--content "content"` | entrycontent. support `@filepath` translated textfileread |
| `--keys "k1,k2"` | trigger keywords, translated text |
| `--keys2 "k1,k2"` | translated texttrigger keywords |
| `--position N` | translated textposition(0-7translated text) |
| `--order N` | translated textorder |
| `--constant` | translated text |
| `--no-constant` | translated text |
| `--prevent-recursion` | translated textrecursion. **must** |
| `--exclude-recursion` | translated textrecursion. **must** |
| `--depth N` | translated text(position=4translated text, default1) |
| `--disable` | disabledentry |
| `--enable` | enabledentry |
| `--selective` | translated text |
| `--selective-logic N` | translated text(0=AND_ANY, 1=NOT_ALL, 2=NOT_ANY, 3=AND_ALL) |
| `--scan-depth N` | translated text |
| `--role N` | character(0=system, 1=user, 2=assistant) |
| `--outlet-name "translated text"` | translated text(position=7 translated text) |

---

## translated text v2 translated text `world-info.js` translated text `characters.js`, translated textCharacter Cardtranslated text: 

### position(position)

- translated textusage 0-7 translated text, is nottranslated text
- card-generator.py translated text `"before_char"` / `"after_char"` / `"at_depth"` translated textgenerate JSON translated textcorrecttranslated text
- translated text config.json translated text position
- translated text v2 translated text position==0 translated text position!=0 → position 2-7 translated text extensions.position translated text

### translated textrecursion(prevent_recursion / exclude_recursion)

- translated textdefault valuetranslated text false
- card-generator.py generatetranslated textdefaulttranslated text true
- **translated textmodify config.json translated textgeneratetranslated text, translated textentrytranslated textfield, translated textcodedefault value true translated text**
- translated text world-book-create.py translated text, translated text flag default false, musttranslated text

### entry ID translated text keys

- entry ID translated text 0, 1, 2... translated text
- keys/trigger translated text
- translated text key fieldtranslated text `[]`

### translated textscenario

- translated text position translated text → entrytranslated text, translated texterrorTip
- getSortedEntries() translated text → translated text [], translated textWorld Bookentrytranslated text
- entrytranslated text → translated textentrytranslated text
- loadWorldInfo() HTTP error → translated text null
- **translated text: generatetranslated text --validate translated text, translated text --list confirmentrytranslated textcorrect**

---

## translated texterror

| # | error | reason | correcttranslated text |
|---|------|------|---------|
| 1 | translated text JSON rather thanscriptgenerate | translated text card-generator.py translated text | musttranslated text `--config config.json -o card.json` generate |
| 2 | initvar translated text `<initvar>` translated text | translated text YAML translated text | contentformat `<initvar>\nYAML\n</initvar>` |
| 3 | initvar entrypositionerror | translated text after_char (position 1) | must before_char (position 0) |
| 4 | variable update rulespositionerror | translated text after_char | must at_depth, depth=0 |
| 5 | translated text `<StatusPlaceHolderImpl/>` | greetingtranslated text | translated textgreetingtranslated text `<StatusPlaceHolderImpl/>` |
| 6 | translated text | scripttranslated text escape_regex_body bug | translated text: translated text normalize translated text escape |
| 7 | exclude_recursion translated text prevent_recursion translated text false | translated textdefault false | translated textentrymusttranslated text true |
| 8 | keys translated text/translated text | translated text | translated text |
| 9 | initvar translated text | translated textcodetranslated text | initvar translated textWorld Book [initvar] entrytranslated text |
| 10 | HTML translated textusage `${VARIABLE}` translated text | is not MVU translated text | usage `{{format_message_variable::stat_data.path}}` |

---

## self-checklist

- [ ] usage `--config` generate, translated text JSON
- [ ] generatetranslated text `--validate` translated text
- [ ] translated text `--list` confirmWorld Bookentryquantitycorrect
- [ ] translated textWorld Bookentry `prevent_recursion=true` translated text `exclude_recursion=true`
- [ ] initvar entry position=before_char, enabled=false, content `<initvar>` translated text
- [ ] variable update rules/outputformat/list: position=at_depth, depth=0
- [ ] greetingtranslated text `<StatusPlaceHolderImpl/>`(translated textMVUtranslated text)
- [ ] translated text findRegex usage slash translated text `/pattern/flags`
- [ ] statusbar.html usage `{{format_message_variable::stat_data.path}}` translated text
- [ ] worldbook.entries translated text initvar/variable list/updaterulesentry. translated text mvu.enabled translated textgenerate
