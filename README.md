# SillyTavern Character Card/World Booktranslated text — Character & World Book Manager

translated text AI translated textlight novel/translated text, translated textgeneratetranslated textWorld Book JSON translated textCharacter Card. 

**Note: translated text AI generate, translated textissues. translated text, translated text issue. **

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## Acknowledgements
translated textCharacter Cardwritetranslated textTiptranslated textreferencetranslated text [sanmingyue](https://github.com/sanmingyue) translated text, translated text. 

## Position Statement
translated textRolePlaytranslated text, translated textcharactertranslated text. 
translated textdisabledtranslated text AI translated text, translated text API translated text, translated textCharacter Cardtranslated text. 
translated textusagetranslated text, translated textsupport. 

---

## What is this

translated text **AI Skill + CLI translated text** translated text. translated text AI translated text, SAY: 

> "translated textlight novel, translated textcharacter, Worldviewtranslated textWorld Bookentry"
> "translated text, translated text MVU status bartranslated text HTML beautificationtranslated textCharacter Card"
> "translated textgeneratetranslated textWorld Book, translated textextracttranslated text"

AI translated text: 
1. **translated text** — translated textoriginaltranslated textderivative, Character Cardtranslated textWorld Book, translated textneed MVU/EJS/HTML beautification. 
2. **write** — translated text"Character Cardwritehard rules", XML translated text YAML format, description translated text, alltranslated textWorld Bookentry. 
3. **self-check** — translated text SubAgent translated textforbidden-word scan(translated text, narrative forbidden words, metaphor forbidden words, translated text), self-checktranslated textgenerate. 
4. **generate** — translated text CLI scriptoutputtranslated text SillyTavern translated textWorld Booktranslated textCharacter Card JSON. 

## Feature Overview

| translated text | description |
|------|------|
| **light novel→World Book** | translated text, AI translated textcharacter/Worldview, translated textchapterline number, generatetranslated textWorld Book JSON |
| **translated textCharacter Card** | generatesupport MVU ZOD translated textfront-end beautificationtranslated textCharacter Card, translated textcharactertranslated text, personality, Worldview, greeting |
| **MVU & EJS dynamic content** | translated text ZOD variable system + EJS translated textphasetranslated text/translated text, supportstatus bartranslated textbeautification |
| **HTML beautification** | translated textbeautification + status barbeautification + translated text, translated text CSS variabletranslated text, inline SVG translated text |
| **CLI translated text** | `world-book-create.py` (World Book) / `card-generator.py` (Character Card) / `query.py` (query) |
| **SubAgent translated text** | generate JSON translated text SubAgent, translated textforbidden words, translated text, configurationcorrecttranslated text, translated textoutput |

## Supported Scenarios

| scenario | usagetranslated text reference |
|------|-----------------|
| **originalCharacter Cardtranslated text** | character-card-guide + character-guide + card-generator-guide |
| **derivative/light noveltranslated text** | information-extraction-guide + character-card-guide + world-book-guide |
| **MVU variable system** | mvu-guide |
| **EJS dynamic content** | ejs-guide(translated text MVU) |
| **HTML front-end beautification** | html-beautify-guide |
| **originalWorldviewtranslated text** | world-building-guide + world-book-guide + config-guide |
| **item/ability/equipment** | world-book-guide + config-guide |
| **translated text/storyextract** | information-extraction-guide + writing-optimization-guide |
| **modify/querytranslated textcontent** | query.py + card-generator.py --decompile |
| **forbidden-word scantranslated text** | writing-optimization-guide |

---

## Directory Structure

```
world-book-skill/
├── SKILL.md # translated text: v4.0 translated text, derivative/originaltranslated text, SubAgentself-check
├── plan.md # translated text: filetranslated textreferencesourcetranslated text
├── agents/openai.yaml # translated text
├── scripts/
│ ├── world-book-create.py # World Booktranslated text CLI (+position 0-7 translated text)
│ ├── card-generator.py # Character Card V3 JSON generate/unpack/edit/validate/list
│ └── query.py # World Booktranslated textquery/translated text
└── references/
 ├── guide.md # scenariorouter(11 translated texttype, AI translated textread)
 ├── character-card-guide.md # Character Cardwrite: World Bookentry + greeting(description translated text)
 ├── character-guide.md # characterentrytranslated text(XML translated text YAML)
 ├── world-building-guide.md # Worldviewtranslated text(translated text, A/B/C typetranslated text)
 ├── world-book-guide.md # World Bookentry conversion(translated text, translated text, itemtranslated text)
 ├── information-extraction-guide.md # derivativeinformation extraction(chapterline numbertranslated text, outline.txt)
 ├── writing-optimization-guide.md # forbidden-word scan + translated text(translated textforbidden words)
 ├── card-generator-guide.md # translated textscriptcompleteusagetranslated text(translated text)
 ├── config-guide.md # World Bookconfigurationrules(position/translated text/recursion)
 ├── position-guide.md # ST translated textpositionreference
 ├── mvu-guide.md # MVU ZOD variable system(translated textphasetranslated text)
 ├── ejs-guide.md # EJS dynamic content(translated textphasetranslated text, translated text)
 └── html-beautify-guide.md # HTML front-end beautification(translated text/status bar/translated textrules)
```

## Dependencies

- Python 3.8+
- SillyTavern (translated textgeneratetranslated text JSON)

---

# Changelog

## v4.0.2 — 2026-05-18 (Current)

### Tiptranslated text
- **`card-generator-guide.md` translated text**: translated text `SKILL.md`(hard rules/branchtranslated text/branchtranslated text/finalization), `guide.md`(scenariorouter/type2/translated text), `world-book-guide.md`(translated text/Phase 4/self-checklist)translated text 11 translated textpositionadded/translated textmusttranslated text `card-generator-guide.md` translated text, translated text AI translated textoutputtranslated textWorld Book/Character Card JSON format. 

## v4.0.1 — 2026-05-18

### Merged PR fixes and enhancements

| source | PR | content |
|------|-----|------|
| **pisces1986** | [#1](https://github.com/echo-xianyu/worldbook-skill/pull/1) | `world-book-create.py`: added `_camel_to_snake()` translated text, `_Args` support camelCase/snake_case translated text. batch JSON translated text `preventRecursion` translated text `prevent_recursion` translated textfieldtranslated text. |
| **pisces1986** | [#3](https://github.com/echo-xianyu/worldbook-skill/pull/3) | `world-book-create.py`: `parse_key_list()` translated textsupporttranslated textinput. `card-generator.py`: added `card.name` translated text, added MVU translated text(zod/beta translated text), MVU enabledtranslated textgreetingtranslated text `<StatusPlaceHolderImpl/>` translated textWarning. |
| **uiharuayako** | [#4](https://github.com/echo-xianyu/worldbook-skill/pull/4) | `agents/openai.yaml`: translated text14translated textCharacter Cardtranslated textfiletranslated text(`card-writing-guide.md` → `character-card-guide.md`), translated text23translated textforbidden-word scantranslated textfiletranslated text(→ `writing-optimization-guide.md`). |

## v4.0 — 2026-05-17

### Architecture refactor
- **workflowtranslated text**: originaltranslated textderivativetranslated text. originaltranslated text Plan translated text, derivativetranslated text `information-extraction-guide.md` extracttranslated text. 
- **description translated text**: Character Card description fieldtranslated textcontent, translated textcharactertranslated text(basic profile, appearance, background, relationship, personality)alltranslated textWorld Bookentry, translated text AI translated textread description translated textpersonalitytranslated text. 
- **Worldviewtranslated textWorld Booktranslated text**: Worldviewtranslated text(`world-building-guide.md`)translated textWorld Bookentry conversion(`world-book-guide.md`)translated textphase, translated text. 
- **SubAgent self-checktranslated text**: generate JSON translated textmusttranslated text SubAgent translated textforbidden wordsself-check, translated text card-generator.py generateoutput. 

### New features
- **EJS dynamic contentsupport**: added `ejs-guide.md`, translated textphasetranslated text(controller + phaseentry + getwi translated text)translated textphasetranslated text(translated text/translated text/secondary interpretationtranslated textvariabletranslated text). EJS Dependencies MVU, translated text. 
- **translated textscriptusagetranslated text**: added `card-generator-guide.md`, translated text Python scripttranslated textall CLI parameters, config.json translated textfielddescription, MVU/status bartranslated textgeneratetranslated text, translated text v2 translated text(position 0-7 translated text, translated textrecursiontranslated text). 
- **scripttranslated text**: `card-generator.py` added position translated text, content translated text, keys translated text; `world-book-create.py` added position translated text. 

### Forbidden-word and quality optimizations
- **translated textforbidden words**: `writing-optimization-guide.md` forbidden wordstranslated textadded"——"(translated text/translated text), skill translated textall 11 translated text reference filealready cleanedtranslated text. 
- **translated textrules**: `html-beautify-guide.md` added 4 translated textbeautificationrules(translated text white-space, translated text, CSS translated text, translated text), translated textbeautificationtranslated textstatus bartranslated text, translated textissues. 

### Guide updates
- translated text reference filetranslated text"Your role"changed to"This document covers", skill is nottranslated text AI translated textcharacter, translated text AI translated text. 
- `character-guide.md` translated text XML changed to XML translated text YAML format. 
- `world-book-guide.md` item/scenarioentrytranslated textchanged to XML translated text YAML. 
- `guide.md` scenarioroutertranslated text, translated textstory/chapterextracttranslated texttype 6. 
- `SKILL.md` hard rules, branch, finalizationalltranslated text, self-checktranslated textgeneratetranslated text. 

## v3.0 — 2026-05-14

### Major feature upgrades
- **Character Cardtranslated text**: added `card-generator.py`, supportgenerate/unpacktranslated text V3 Character Card JSON. 
- **beautificationsupport**: added `html-beautify-guide` translated text `mvu-guide`, support ZOD variablestatus bartranslated textbeautificationtranslated text. 
- **translated text**: translated text DoubleCheck translated text, includetranslated textforbidden-word scantranslated text. 
- **formattranslated text**: translated text XML translated text YAML format, translated text AI writetranslated text. 

### Detail optimizations
- `SKILL.md` translated text, translated text. 
- translated textscenariorouter `guide.md`, translated textWorld Book, Character Card, beautificationtranslated text. 
- updatetranslated textextracttranslated text, translated text YAML translated textoutput. 

## v2.1 — 2026-05-09
- `world-book-create.py` added `excludeRecursion` support. 
- translated textTiptranslated text, translated textWorld Bookforbidden wordstranslated text. 

## v2.0 — 2026-04-26
- added `query.py` querytranslated text. 
- addedscenariorouter `guide.md` translated textextract/translated text. 
- characterentryformattranslated text, translated textcharacter, Worldview, configurationtranslated text. 

## v1.0 — 2025
- Initial release, supports basic World Book JSON generation.

---

## Contributors

Thanks to the following contributors for code contributions:

| Contributor | GitHub | Contribution |
|--------|--------|---------|
| **sanmingyue** | [@sanmingyue](https://github.com/sanmingyue) | Character Cardwritetranslated textTiptranslated text |
| **pisces1986** | [@pisces1986](https://github.com/pisces1986) | [#1](https://github.com/echo-xianyu/worldbook-skill/pull/1) `_Args` camelCase→snake_case translated text / [#3](https://github.com/echo-xianyu/worldbook-skill/pull/3) inputtranslated text, MVU translated text(translated text) |
| **uiharuayako** | [@uiharuayako](https://github.com/uiharuayako) | [#4](https://github.com/echo-xianyu/worldbook-skill/pull/4) openai.yaml prompt translated text |
