# World Bookconfigurationrulestranslated text

## This document covers

>translated textWorld Bookconfigurationtranslated text. translated textcontent,translated textcontentconfigurationtranslated text AI translated textcorrectreadtranslated textentry. translated textfielddescription, parameterstranslated text, scenariotranslated text, configurationtranslated text, configurationtranslated text. 

---

## translated text, workflow

```
translated textcontent → translated texttype → translated text → translated textposition/order/recursion → translated textscripttranslated text → query.py self-check
```

translated textordertranslated text: translated texttypetranslated textconfiguration, translated textconfigurationtranslated text, translated textself-check. 

---

## translated text, positiontranslated text (position)

`position` translated textentrycontenttranslated textTiptranslated textposition. translated text 0–7: 

| translated text | translated text | CLI flag | translated text | translated text |
|----|------|----------|------|------|
| 0 | ↑Char | `--position 0` | charactertranslated text (before_char) | translated text: worldview outline, rules, geography, history |
| 1 | ↓Char | `--position 1` | charactertranslated text (after_char) | translated text: charactertranslated text, NPC, scenario, item |
| 2 | ↑AT | `--position 2` | translated text | translated textrules, formattranslated text |
| 3 | ↓AT | `--position 3` | translated text | translated textusage |
| 4 | @D | `--position 4 --depth 0 --role 0` | Dtranslated text (at_depth) | translated text, secondary interpretation, translated text AI |
| 5 | ↑EM | — | exampletranslated text | do not use |
| 6 | ↓EM | — | exampletranslated text | do not use |
| 7 | Outlet | `--position 7 --outlet-name <translated text>` | translated text | do not use |

**@D translated texthard rules**: position=4 translated textmusttranslated text depth, translated text**translated text depth=0**. D1 translated text, translated texthistorytranslated textcompletetranslated text. AI translated textdescriptiontranslated text. D0 translated text, translated text. 

**role parameters**: position=4 translated text `--role 0` (System), translated textpositiontranslated text role. 

---

## translated text, constant translated text

`constant` translated textentrytranslated text: 

| translated text | translated text | translated text |
|----|------|------|
| `true` | translated text | entrytranslated text, translated text AI |
| `false` | translated text | translated text |

translated text = musttranslated text. translated text = translated text. translated text: translated text → token translated text; translated text → AI translated text. 

---

## translated text, scanDepth translated text entrytranslated text. translated text"translated text"translated text: 

| translated text | translated text |
|----|------|
| `null` (translated text) | translated textalltranslated text |
| `2` | translated text + translated text AI translated text |

**recommended: translated textentrytranslated text `scanDepth=2`. ** translated text. charactertranslated text, translated text AI translated texthistorytranslated text, entrytranslated text, translated text. 

---

## translated text, recursiontranslated textfield(translated text)

```
preventRecursion: true ← translated textentrytranslated textentry
excludeRecursion: true ← translated textentrytranslated textentrytranslated text
```

**translated textentrymusttranslated text `true`, translated text. ** translated textneed. 

translated text `preventRecursion=true` translated textconsequences: entry A contenttranslated textentry B translated text → B translated text → B translated textcontenttranslated text C → translated text → token translated text. translated text `excludeRecursion=true` translated textconsequences: B translated text C translated text C translated text B translated text → translated textrecursion → translated textentrytranslated text. 

**scriptdefault valuetranslated text `false`, translated text flag translated text. ** translated textmusttranslated text `--prevent-recursion --exclude-recursion`. 

---

## translated text, order translated textrules

translated textpositiontranslated textentrytranslated text `order` translated text, translated text. 

| entrytype | order | notes |
|----------|-------|------|
| worldview outline | 1 | translated text, AI translated text |
| background setting / translated text | 2–3 | translated text |
| charactertranslated text | 4 | translated textcharactertranslated text |
| scenario / translated text | 50–98 | translated textscenariotranslated text |
| translated textcharactertranslated text | 99 | translated text |
| NPC / controller | 100 | translated text |

translated textCharacter Cardtranslated textentrytranslated text: translated text 10 → appearance 20 → personality 30 → background 40 → NSFW 50. 

translated textCharacter Cardtranslated textsecondary interpretationentrytranslated text: characterA=1, characterB=2, translated text. 

---

## translated text, keys format

translated text**translated text** `,` translated text. translated text `, ` translated text. 

translated text: 

| entrytype | keys translated text |
|----------|-----------|
| characterentry | full name, nickname, translated text |
| NPC entry | full name, nickname, translated text, position |
| scenarioentry | scenariotranslated text, translated text, translated text, translated text |
| factionentry | full name, translated text, translated text |

correctexample: `Lin Xiaoyu,Xiaoyu,class monitor`
errorexample: `Lin Xiaoyu, Xiaoyu, class monitor` `Lin Xiaoyu Xiaoyu class monitor`

---

## translated text, translated text

configurationtranslated textmusttranslated textscenariotype. translated text: World Booktranslated textdescriptiontranslated text**translated textcharacter**. translated textcharactertranslated textentry(translated text/appearance/personality/background……)translated textcharacter. 

### 8.1 translated textCharacter Card(1 translated textcharacter)

**hard rules: translated textcharactertranslated textentryalltranslated text. ** translated text 5 translated text = 5 translated text, translated text 10 translated text = 10 translated text. translated text. 

| entrytype | translated text/translated text | position | order | keys | scanDepth |
|----------|----------|----------|-------|------|-----------|
| worldview outline | translated text | 0 (↑Char) | 1 | — | — |
| background setting | translated text | 0 (↑Char) | 2–3 | — | — |
| charactertranslated text | translated text | 1 (↓Char) | 10 | — | — |
| characterappearance | translated text | 1 (↓Char) | 20 | — | — |
| characterpersonality | translated text | 1 (↓Char) | 30 | — | — |
| characterbackground | translated text | 1 (↓Char) | 40 | — | — |
| character NSFW | translated text | 1 (↓Char) | 50 | — | — |
| charactersecondary interpretation | translated text | 4 (@D, depth=0) | 1 | Character name,nickname | 2 |
| NPC | translated text | 1 (↓Char) | 100 | NPCtranslated text,nickname,position | 2 |
| scenario/translated text | translated text | 1 (↓Char) | 50–98 | scenariotranslated text,translated text | 2 |

### 8.2 translated textCharacter Card(2+ translated textcharacter)

**hard rules: translated text, charactertranslated textalltranslated text. ** translated textcharactertranslated text. 

| entrytype | translated text/translated text | position | order | keys | scanDepth |
|----------|----------|----------|-------|------|-----------|
| worldview outline | translated text | 0 (↑Char) | 1 | — | — |
| background setting | translated text | 0 (↑Char) | 2–3 | — | — |
| charactertranslated text | translated text | 0 (↑Char) | 4 | — | — |
| characterA translated text | translated text | 1 (↓Char) | 99 | characterAtranslated text,nickname,translated text | 2 |
| characterB translated text | translated text | 1 (↓Char) | 99 | characterBtranslated text,nickname,translated text | 2 |
| characterA secondary interpretation | translated text | 4 (@D, depth=0) | 1 | characterAtranslated text,nickname | 2 |
| characterB secondary interpretation | translated text | 4 (@D, depth=0) | 2 | characterBtranslated text,nickname | 2 |
| NPC | translated text | 1 (↓Char) | 100 | NPCtranslated text,nickname,position | 2 |
| scenario/translated text | translated text | 1 (↓Char) | 50–98 | scenariotranslated text,translated text | 2 |

### 8.3 translated textWorld Book(translated text, translated textCharacter Card)

**hard rules: translated textentrytranslated text. ** translated text EJS translated textcontenttranslated text, rather thanDependenciestranslated text. 

| entrytype | translated text/translated text | position | order | keys | notes |
|----------|----------|----------|-------|------|------|
| translated textbackground | translated text | 0 (↑Char) | 1 | — | |
| rules/translated text | translated text | 0 (↑Char) | 2 | — | |
| translated text | translated text | 1 (↓Char) | 99 | — | translated text EJS translated text |
| variable update rules | translated text | 1 (↓Char) | 100 | — | |
| EJS controller | translated text | 1 (↓Char) | 100 | — | |
| EJS translated textentry | disabled (enabled=false) | 1 (↓Char) | — | — | translated textcontrollertranslated text getwi() translated text, translated textphasecontenttranslated text |

---

## translated text, translated textpositionrecommended

```
worldview outline → position=0 (↑Char, before_char)
 translated text: translated textrules, geography, history, background. AI translated textcharactertranslated text. 

charactertranslated text → position=1 (↓Char, after_char)
 translated text: charactertranslated text, NPC, scenario, item. AI translated textcharactertranslated text. 

secondary interpretation → position=4, depth=0, role=0 (@D)
 translated text AI translated textcontent. do not write"translated text", translated text"translated text". 
 D0 translated text, translated text AI translated textcharacter/translated text. 

translated textrules → position=2 (↑AT)
 translated textformattranslated text. 

D1 translated text (@D, depth≥1) → translated textdo not use. 
```

---

## translated text, configurationtranslated text usage. translated textrecursion flag. 

```bash
# worldview outline(translated text, charactertranslated text)
python world-book-create.py <World Book.json> --add \
 --comment "<translated text>" --content "@<contentfile.txt>" \
 --constant --position 0 --order 1 \
 --prevent-recursion --exclude-recursion

# charactertranslated text(translated text, charactertranslated text, translated textCharacter Card)
python world-book-create.py <World Book.json> --add \
 --comment "<Character name>_translated text" --content "@<contentfile.txt>" \
 --constant --position 1 --order 10 \
 --prevent-recursion --exclude-recursion

# charactertranslated text(translated text, charactertranslated text, translated textCharacter Card)
python world-book-create.py <World Book.json> --add \
 --comment "<Character name>_translated text" --content "@<contentfile.txt>" \
 --keys "<Character name>,<nickname>,<translated text>" --position 1 --order 99 --scan-depth 2 \
 --prevent-recursion --exclude-recursion

# NPC(translated text, charactertranslated text)
python world-book-create.py <World Book.json> --add \
 --comment "NPC_<Character name>" --content "@<contentfile.txt>" \
 --keys "<full name>,<nickname>,<position>" --position 1 --order 100 --scan-depth 2 \
 --prevent-recursion --exclude-recursion

# scenario(translated text, charactertranslated text)
python world-book-create.py <World Book.json> --add \
 --comment "scenario_<scenariotranslated text>" --content "@<contentfile.txt>" \
 --keys "<scenariotranslated text>,<translated text>" --position 1 --order 80 --scan-depth 2 \
 --prevent-recursion --exclude-recursion

# secondary interpretation(translated text, D0)
python world-book-create.py <World Book.json> --add \
 --comment "<Character name>_secondary interpretation" --content "@<contentfile.txt>" \
 --keys "<Character name>,<nickname>" --position 4 --depth 0 --role 0 --scan-depth 2 \
 --prevent-recursion --exclude-recursion

# disabledentry(EJS translated textentrytranslated text)
python world-book-create.py <World Book.json> --add \
 --comment "<entrytranslated text>" --content "@<contentfile.txt>" \
 --disable --position 1 --order 100 \
 --prevent-recursion --exclude-recursion

# edittranslated textentry(translated text UID)
python world-book-create.py <World Book.json> --edit <UID> \
 --content "@<translated textcontentfile.txt>" --depth 4

# translated textentry
python world-book-create.py <World Book.json> --list

# translated text(translated text JSON translated textfile)
python world-book-create.py <World Book.json> --batch <translated textconfiguration.json>
```

---

## translated text, query.py translated text

```bash
# translated textentrytranslated text(translated text content_preview, keys, position, constant translated text)
python query.py <World Book.json>

# translated text(uid / comment / content_length / keys / constant / translated textrecursionstatus)
python query.py <World Book.json> --brief

# translated text UID entrytranslated textcomplete JSON(outputtranslated text --batch-edit)
python query.py <World Book.json> --uid <UID>

# translated textentry(translated text/content/translated text)
python query.py <World Book.json> --search "<translated text>"

# translated textentrytranslated text @UID/@name translated text
python query.py <World Book.json> --resolve
```

querytranslated textfieldtranslated text: 

| field | translated text | translated text |
|------|------|----------|
| `constant` | true=translated text, false=translated text | translated textCharacter Cardtranslated textcharacterentrymusttranslated text true |
| `preventRecursion` | translated textentry | allentrymusttranslated text true |
| `excludeRecursion` | translated textentrytranslated text | allentrymusttranslated text true |
| `scanDepth` | null=translated text, 2=translated text | translated textentrytranslated text 2 |
| `keys` | translated text | translated text, translated text |

---

## translated text, self-checklist

configurationtranslated text, translated text `python query.py <World Book.json> --brief` translated text, translated text: 

- [ ] **translated textcharactertranslated text**: 1 translated text → translated textCharacter Card, 2+ translated text → translated textCharacter Card
- [ ] translated textCharacter Card？→ translated textcharactertranslated textentry `constant=true`
- [ ] translated textCharacter Card？→ translated text `constant=true`, charactertranslated text `constant=false` + translated text `keys`
- [ ] Worldviewentryall `constant=true`
- [ ] NPC / scenario / storychapterall `constant=false` + translated text `keys`
- [ ] **translated textentry `preventRecursion=true` translated text `excludeRecursion=true`**(scriptdefault false, translated text flag translated text！)
- [ ] translated text `,` translated text, translated text, translated text
- [ ] translated textentry `scanDepth=2`
- [ ] translated textentryusage position=3/5/6/7
- [ ] translated textentry depth≥1(translated text D0 translated text)
- [ ] translated textCharacter Cardtranslated textentrytranslated text order translated text(10→20→30→40→50)
- [ ] secondary interpretationentrytranslated text position=4, depth=0, role=0

---

## translated text, common error examples

### error 1: translated textCharacter Cardtranslated textcharactertranslated textentrytranslated text

```
error: Lin Xiaoyu_personality → constant=false(translated text)
consequences: AI translated textpersonalitytranslated text, translated textcharactertranslated text, charactertranslated text. 
correct: translated textCharacter Cardtranslated textcharacterentry constant=true. translated text. 
```

### error 2: translated textrecursion flag

```
error: translated textentrytranslated text --prevent-recursion --exclude-recursion
consequences: scriptdefaulttranslated text preventRecursion=false, excludeRecursion=false. 
 translated textentrytranslated text, token translated text. 
correct: translated text --prevent-recursion --exclude-recursion. 
```

### error 3: translated text

```
error: --keys "Lin Xiaoyu, Xiaoyu, class monitor"
consequences: translated text, translated text. 
 translated textinputcompletetranslated text"Lin Xiaoyu, Xiaoyu, class monitor"translated text. 
correct: --keys "Lin Xiaoyu,Xiaoyu,class monitor"
```

### error 4: secondary interpretationtranslated text position=1

```
error: secondary interpretationtranslated text ↓Char (position=1), translated textentrytranslated text
consequences: secondary interpretationtranslated text, AI translated text. 
correct: position=4, depth=0, role=0. D0 translated textposition. 
```

### error 5: translated textCharacter Cardtranslated text

```
error: 3 translated textcharacter, translated text 5 translated text, all constant=true
consequences: 15 translated text + Worldview + NPC, translated text. 
correct: translated text, translated textcharactertranslated text + translated text. 
```

### error 6: EJS translated textentrytranslated textenabled

```
error: translated textphasetranslated textphaseentry enabled=true, translated text constant=true
consequences: translated textphasecontenttranslated text AI translated text, charactertranslated textstatustranslated text. 
correct: translated textentry enabled=false, translated text EJS controllertranslated text getwi() translated text. 
```

### error 7: scanDepth translated text

```
error: translated textentrytranslated text scanDepth(default null, translated text)
consequences: charactertranslated text, translated text 20 translated text, AI translated texthistorytranslated text, 
 entrytranslated text, token translated text. 
correct: translated textentry scanDepth=2. 
```

---

## translated text, fieldtranslated text

World Bookentrytranslated textfieldtranslated text, translated text CLI parameters / JSON fieldtranslated text: 

| CLI flag | JSON field | type | default value | description |
|----------|-----------|------|--------|------|
| `--comment` | `comment` | string | `""` | entrytranslated text/notes |
| `--content` | `content` | string | `""` | entrytranslated text, support `@filepath` translated textfileread |
| `--keys` | `key` | string[] | `[]` | translated text, translated text |
| `--keys2` | `keysecondary` | string[] | `[]` | translated text |
| `--constant` | `constant` | bool | `false` | true=translated text |
| `--position` | `position` | 0–7 | `0` | translated textposition |
| `--order` | `order` | int | translated text+100 | translated text, translated text |
| `--depth` | `depth` | int | `1` | translated text(translated text position=4 translated text 0) |
| `--role` | `role` | 0–2 | `0` | 0=System, 1=User, 2=Assistant |
| `--scan-depth` | `scanDepth` | int/null | `null` | translated text, translated textrecommended 2 |
| `--prevent-recursion` | `preventRecursion` | bool | `false` | musttranslated text true |
| `--exclude-recursion` | `excludeRecursion` | bool | `false` | musttranslated text true |
| `--disable` | `disable` | bool | `false` | true=disabledentry |
| `--selective` | `selective` | bool | `false` | translated text |
| `--selective-logic` | `selectiveLogic` | 0–3 | `0` | 0=AND_ANY, 1=NOT_ALL, 2=NOT_ANY, 3=AND_ALL |
| `--group` | `group` | string | `""` | translated text |
| `--group-weight` | `groupWeight` | int | `100` | translated text |
| `--probability` | `probability` | int | `100` | translated text 1–100 |
| `--case-sensitive` | `caseSensitive` | bool/null | `null` | translated text |
| `--match-whole-words` | `matchWholeWords` | bool/null | `null` | translated text |
| `--sticky` | `sticky` | int | `0` | translated text |
| `--cooldown` | `cooldown` | int | `0` | translated text |
| `--delay` | `delay` | int | `0` | translated text |
