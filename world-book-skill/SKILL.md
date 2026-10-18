---
name: world-book-skill
description: >-
 Create and manage SillyTavern Character Cards (Character Card) and World Books (World Book).
 Supports character card writing, world book creation, MVU ZOD variables, HTML beautification,
 opening scene writing, and card-generator.py integration.
 supportCharacter Cardwrite, World Booktranslated text, MVU ZOD variable system, HTML front-end beautification, greetingtranslated text, 
 card-generator.py translated textscenario. usagetranslated textreadscenarioroutertranslated textreferencefile. 
---

# SillyTavern Character Card/World Booktranslated text

## This document covers

>translated text skill translated textfile. translated text(original/derivative)translated text reference file: derivativetranslated text `information-extraction-guide.md` extracttranslated text, originaltranslated text Plan translated text. Character Cardwritetranslated textWorld Bookentrytranslated text, translated textgreeting. MVU/EJS/HTML beautificationtranslated textenabled. translated textforbidden-word scan. 

---

## hard rules(translated text)

translated textrulestranslated textalltranslated text, translated text: 

0. **translated text** — translated text RolePlay translated text. translated text, translated text, translated text API translated textgenerateCharacter Cardtranslated textWorld Book. 
1. **originaltranslated textderivativetranslated text** — originaltranslated text Plan translated text; derivativetranslated text `information-extraction-guide.md` extracttranslated text. translated text. 
2. **Character Card description translated text** — description fielddo not writetranslated textcontent. characteralltranslated text(basic profile, appearance, background, relationship, personality)translated textWorld Bookentry. 
3. **Worldviewtranslated textWorld Bookentry conversion** — translated text `world-building-guide.md` translated text, translated text `world-book-guide.md` translated textentrytranslated text. translated textphasetranslated text. 
4. **translated text, translated textCharacter Card** — Character Cardwritetranslated textWorld Bookentrytranslated text. translated text, do not writegreeting. 
5. **translated text MVU/EJS/HTML** — translated text, translated text. EJS Dependencies MVU, user request EJS musttranslated textconfirm MVU translated textenabled. 
6. **forbidden wordstranslated text** — finalizationphasetranslated text `writing-optimization-guide.md`, translated text. 
7. **itemtranslated text** — translated text: translated text, do not writetranslated text. translated text: translated text, do not writetranslated text. 
8. **translated text reference, translated text** — translated textwrite, translated texttypemustreadtranslated textall reference filetranslated text. translated text**musttranslated text `references/card-generator-guide.md`**, usage `card-generator.py`, `query.py`, `world-book-create.py` translated textCharacter Card/World Book. 

---

## translated text , translated textread `references/guide.md` translated texttype, translated textreadtranslated text reference file. guide.md translated text 11 translated texttype(originalCharacter Card, derivativeextract, translated textWorldview, itemability, MVU, EJS, HTML beautification, forbidden-word scantranslated text)translated textcompletetranslated text. 

---

## branchtranslated text: derivativetranslated text(translated textoriginal texttranslated text)

applicable scenarios: light novel, translated textunpack, translated textextracttranslated text. 

**Step 1 — readinformation extractiontranslated text**
translated text `references/information-extraction-guide.md`, confirmextracttranslated textformattranslated text. 

**Step 2 — translated text**
- translated text: translated text txt file, writeentrytranslated textread. 
- translated textoriginal text: translated textchapterline number(translated text: translated text L100, translated text L280). translated textcharactertranslated textchapter. 
- writetranslated textentrytranslated text, translated textchaptertranslated text txt. 

**Step 3 — extracttranslated text**
translated textextraction resulttranslated textcontenttypetranslated text: 
- charactertranslated text → translated textbranchtranslated text(translated textCharacter Card)
- Worldviewtranslated text → translated textbranchtranslated text(Worldviewtranslated text + World Bookentry conversion)
- item/ability/equipment → translated textbranchtranslated text(World Bookentry conversion, itemtranslated text `world-book-guide.md` translated text)

**Step 4 — writetranslated text**
writetranslated textentrytranslated text, translated textchaptertranslated text txt. 

---

## branchtranslated text: originaltranslated text(translated textoriginal text)

applicable scenarios: translated textcharacter/Worldviewtranslated text, translated textreferencetranslated text. 

**Step 1 — translated text Plan translated text**
translated text Plan translated text, translated text, translated text: translated texttype, translated textbackground, translated textrules, factiontranslated text, charactertranslated textrelationship. 

**Step 2 — translated text**
translated text, translated textusage. 

**Step 3 — translated text**
translated textcontenttypetranslated text: 
- charactertranslated text → translated textbranchtranslated text(translated textCharacter Card)
- Worldviewtranslated text → translated textbranchtranslated text(Worldviewtranslated text + World Bookentry conversion)

---

## branchtranslated text: translated textCharacter Card(translated text: greeting)

applicable scenarios: translated text, translated textCharacter Card JSON. 

**Step 1 — confirm MVU？**
translated text MVU/ZOD variable system？
translated text → translated text `references/mvu-guide.md`

**Step 2 — confirm EJS？**
translated text EJS dynamic content？
translated text → translated text `references/ejs-guide.md`(translated textconfirm MVU translated textenabled; EJS Dependencies MVU)

**Step 3 — confirm HTML beautification？**
translated text HTML beautification？beautificationtranslated text(status bar/translated text/translated text)？
translated text → translated text `references/html-beautify-guide.md`

**Step 4 — readCharacter Cardwritetranslated text**
translated text `references/character-card-guide.md`

**Step 5 — translated text description, writeWorld Bookcharacterentry**
translated text `character-guide.md` translated text XML translated text, writetranslated textcontent: translated text, appearance traits, background setting, relationshiptranslated text. translated textpersonalitytranslated text. 

**Step 6 — writepersonalityentry**
translated textcharacterpersonalitytranslated textWorld Bookentry, translated text `character-guide.md` translated text `<personality>` translated text(core_drive, traits, likes, dislikes, habits, hidden_self). 

**Step 7 — writegreeting**
write `first_mes` translated text 2-4 translated text `alternate_greetings`: 
- translated text, translated text
- translated text user translated text, translated textopen endingtranslated text
- translated text user translated textappearance, translated text, personality, gender
- translated textenabled MVU, translated text `<StatusPlaceHolderImpl/>` translated text

**Step 8 — translated text SubAgent self-check**
translated textgenerate JSON translated text, translated text SubAgent translated textself-check: 
- read `references/writing-optimization-guide.md` translated textforbidden wordstranslated text
- translated text(World Bookentry, greeting, description if any, config.json configuration)
- translated text: forbidden wordsmatchtranslated text, translated textusagetranslated text, greetingtranslated text, World Booktranslated text, translated textrecursiontranslated text
- outputself-checktranslated text, translated text
- translated text Agent translated textcontenttranslated text, translated text

**Step 9 — translated text → confirm → generate JSON**
translated text. translated textconfirmtranslated text, musttranslated text `references/card-generator-guide.md` translated textscripttranslated text config.json format, translated text`references/card-generator-guide.md`translated textformatgenerateconfig.json, translated textscriptgeneratetranslated textCharacter Cardtranslated text JSON, translated text `--validate` translated text `--list` validate. 

---

## branchtranslated text: Worldviewtranslated text + World Bookentry conversion

applicable scenarios: translated textWorldviewtranslated textWorld Bookconfiguration. 

### phase 1: Worldviewtranslated text `references/world-building-guide.md`, translated text: geographytranslated text, translated textbackground, factiontranslated text, rulestranslated text, historytranslated text. outputtranslated textworldview outlinetranslated text. 

### phase 2: World Bookentry conversion

translated text `references/world-book-guide.md`, translated textWorldviewtranslated textconfirmtranslated textcontenttranslated textWorld Bookentry: 
- translated text(translated textCharacter Card / translated textCharacter Card)
- translated textordertranslated text: translated text → charactertranslated text → translated textentry → personalityentry → item/ability/scenario → NPC
- configurationtranslated textentrytranslated text position, constant, translated text, recursiontranslated text
- translated textentrytranslated text `config.json`(translated textconfirmtranslated text)

### phase 3: validateconfiguration

translated text `references/card-generator-guide.md` translated textscripttranslated text, translated textusage `python scripts/world-book-create.py` translated text, translated textusage `python scripts/query.py <World Bookpath> --brief` validateconfigurationtranslated textcorrect. 

---

## branchtranslated text: translated text , translated text reference: 

**modifytranslated textWorld Book**
→ translated text `python scripts/query.py <World Bookpath> --brief` translated textentry
→ translated textmodifycontenttranslated texttype, readtranslated text reference(reference branchtranslated text~translated text)
→ translated text `references/config-guide.md`

**MVU / ZOD variable system**
→ translated text `references/mvu-guide.md`

**EJS dynamic content**
→ translated text `references/ejs-guide.md`(translated textconfirm MVU translated textenabled)

**HTML front-end beautification**
→ translated text `references/html-beautify-guide.md`
→ translated text MVU status bar, additional read `references/mvu-guide.md`

**forbidden-word scan / translated text**
→ translated text `references/writing-optimization-guide.md`

---

## finalization: translated textphasevalidate(translated textbranchtranslated text)

### phase A: contentself-check(generate JSON translated text, translated text SubAgent)

translated text card-generator.py translated text, translated text SubAgent translated textself-check: 
- read `references/writing-optimization-guide.md`
- translated textcontent(World Bookentry, greeting, config.json configuration)

| translated text | translated text |
|--------|------|
| narrative forbidden words | translated text(translated text, translated text, translated text, translated text, translated text, translated text, translated text) |
| metaphor forbidden words | translated text(translated text, translated text, translated text, translated text) |
| translated text | translated text(—— translated text/translated text, translated text) |
| translated text | translated text, translated text, translated text, translated text |
| greetingtranslated text | charactertranslated text; translated text user translated text/appearance/gender/translated text; translated textcharactertranslated textscenariotranslated text; open ending |
| World Bookentrytranslated text | Worldviewtranslated text; translated text; itemtranslated text |
| configurationtranslated text | translated textrecursiontranslated text; translated textconfigurationcorrect; position/order translated text; keys translated text |
| charactertranslated text | charactertranslated textWorldviewtranslated text, translated text |

SubAgent outputself-checktranslated text, translated text. translated text Agent translated text, translated textphase B. 

### phase B: generatevalidate(generate JSON translated text)

**musttranslated textread `references/card-generator-guide.md`**, translated textcompleteparameterstranslated texterror, translated textcontenttranslated text config.json, translated text: 
```bash
python scripts/card-generator.py --config config.json -o Character name.json
python scripts/card-generator.py --validate Character name.json
python scripts/card-generator.py --list Character name.json
```

---

## contentformattranslated text World Bookentrycontenttranslated text **XML translated text YAML** format. XML translated text, YAML contenttranslated text. Character Card description fieldtranslated text, charactertranslated textalltranslated textWorld Bookentry. 

correctexample: 
```xml
<character_basic_final>
charactertranslated text:
 translated text:
 translated text: translated text
 age: 20
</character_basic_final>
```

translated text XML format(translated text YAML translated text)translated text JSON format. 

---

## translated text

| translated text | translated text | translated textparameters |
|------|------|---------|
| `card-generator.py` | generateCharacter Card JSON; unpack/edit/validateCharacter Card | `--config` translated textconfigurationgenerate, `--validate` validate, `--decompile` unpack, `--list` translated text |
| `query.py` | translated textWorld Bookentry | `--brief` translated text, `--uid` translated textentry, `--search` translated text |
| `world-book-create.py` | translated text/modifytranslated textWorld Book | `--add` translated textentry, `--delete` translated text, `--init` translated text |

translated textcompleteparametersdescriptiontranslated text config.json formattranslated text `references/card-generator-guide.md`. 

---

## filetranslated text

| file | translated text | translated textread |
|------|------|-----------|
| `references/guide.md` | scenariorouter, translated texttype | translated text, translated text |
| `references/information-extraction-guide.md` | derivativeinformation extractiontranslated text | derivativetranslated text, translated text |
| `references/character-card-guide.md` | Character CardWorld Bookentrytranslated textgreetingwrite | translated textCharacter Cardtranslated text, translated text |
| `references/character-guide.md` | characterentry XML translated text | translated textCharacter Cardtranslated textentrytranslated text |
| `references/world-building-guide.md` | Worldviewtranslated text | translated textWorldviewtranslated text |
| `references/world-book-guide.md` | World Bookentry conversiontranslated textconfiguration | translated textWorldviewtranslated textitemtranslated text |
| `references/card-generator-guide.md` | translated textscriptusagetranslated text(card-generator/query/world-book-create) | translated textscripttranslated text |
| `references/config-guide.md` | World Bookconfigurationrules(position/translated text/recursion) | translated textneedtranslated text/modifytranslated text |
| `references/position-guide.md` | translated textposition(position)configuration | translated textneedtranslated text/modifytranslated text |
| `references/mvu-guide.md` | MVU ZOD variable system | user request MVU translated text |
| `references/ejs-guide.md` | EJS dynamic content | user request EJS translated text(translated text MVU) |
| `references/html-beautify-guide.md` | HTML front-end beautification | user requestbeautificationtranslated text |
| `references/writing-optimization-guide.md` | forbidden wordstranslated textself-checktranslated text | finalizationphase, translated text |
