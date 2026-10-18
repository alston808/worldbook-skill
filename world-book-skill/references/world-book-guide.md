# World Bookentrywritetranslated text

> translated textWorldviewtranslated textWorld Booktranslated textentry. translated text. translated text world-building-guide.md translated text, translated textfiletranslated textentrytranslated textconfiguration. 

## This document covers

>translated textWorld Bookentrytranslated text. translated textWorldviewtranslated textphasetranslated text(translated text, charactertranslated text, scenariodescriptiontranslated text)translated textWorld Bookentry, translated textentrycontent, translated text(translated text/translated text), positionconfiguration, recursiontranslated text. translated textWorldviewtranslated text, translated textconfiguration. translated textentrymusttranslated text query.py validate. 

>**scripttranslated text `references/card-generator-guide.md`. translated textmusttranslated text`references/card-generator-guide.md`, translated text, translated textmusttranslated textConfig.jsonformat, usagescripttranslated textWorld Book. **

---

## workflow

### Phase 1: translated text — translated textentrytranslated text : translated textcompletetranslated textWorldviewtranslated text(translated text, charactertranslated text, scenariotranslated text), translated text. 

#### steps1: translated texttype

translated textcharacterquantitytranslated text. translated textcharactertranslated textentry(translated text/appearance/personality/background/abilitytranslated text)translated textcharacter. 

| type | translated text | translated text |
|------|---------|------------|
| translated textCharacter Card | translated text1translated textcharacter, translated textentry | translated textcharactertranslated textentrytranslated text |
| translated textCharacter Card | translated text2translated textcharacter | charactertranslated text + translated textcharactertranslated text |

#### steps2: translated textentrytranslated text ordertranslated text, outputtranslated textconfirm. entrytranslated textmusttranslated textorder. 

| order | entrytype | position | constant | description |
|-------|---------|----------|----------|------|
| 1 | worldview outline | 0 (before_char) | true | translated text, translated text |
| 4 | charactertranslated text | 1 (after_char) | true | translated textCharacter Cardtranslated text, translated textCharacter Cardtranslated text |
| 10-35 | charactertranslated textentry | 1 (after_char) | translated text | translated textcharactertranslated text, XMLtranslated text; translated text, translated text |
| 35-45 | personalityentry | 1 (after_char) | translated text | translated textcharactertranslated textentry; translated text, translated text |
| 50-98 | item/ability/scenario/translated text | 1 (after_char) | false | translated text, scanDepth=2 |
| 99 | charactertranslated text | 1 (after_char) | translated text | translated text |
| 100 | NPC/translated text | 1 (after_char) | false | translated text |

confirmtranslated textphase. 

---

### Phase 2: translated text — translated textworldview outlineentry

translated text: entrytranslated textconfirm. 

#### steps1: translated textcontent

translated textWorldviewtranslated textdescription, include: translated texttype, translated textbackground, translated textrules/translated text, factiontranslated text. translated text, translated text300-500translated text. do not useXMLtranslated text, translated textYAMLtranslated text. 

#### steps2: configurationtranslated textentry

```
position: 0 (before_char)
order: 1
constant: true
prevent_recursion: true
exclude_recursion: true
```

translated textconfiguration items(position/constant/recursion), translated textphase. 

---

### Phase 3: translated text — translated textordertranslated text : translated textconfirm. 

#### steps1: charactertranslated textentry(translated textCharacter Card)

contenttranslated textcharactertranslated text. translated text, identity, translated texttraits. translated textcharactertranslated text. 

configuration: 
```
position: 1 (after_char)
order: 4
constant: true
prevent_recursion: true
exclude_recursion: true
```

#### steps2: charactertranslated textentry

translated textcharactertranslated text, usage `<character>` XML translated text. **completetranslated textfieldtranslated text `character-guide.md`**. 

configuration(translated textCharacter Card): 
```
position: 1 (after_char)
order: 10
constant: true
prevent_recursion: true
exclude_recursion: true
```

configuration(translated textCharacter Card): 
```
position: 1 (after_char)
order: 10(translated textcharactertranslated text)
constant: false
keys: characterfull name,nickname,translated text(translated text)
prevent_recursion: true
exclude_recursion: true
```

#### steps3: personalityentry

translated textcharactertranslated textpersonalityentry, contenttranslated text `<personality>` translated text. musttranslated text: translated text"translated text", personalitytranslated text"translated text". translated textAItranslated textreadtranslated texterrortranslated textpersonalitytranslated text. 

configurationtranslated textsteps2translated textcharactertranslated textentry. 

#### steps4: item/abilityentry

```yaml
<item>
name: itemtranslated text
type: typetranslated text
description: translated textdescription——translated textAItranslated textWhat is this, do not writetranslated textdescriptiontranslated text
</item>
```

**translated textitemtranslated text(translated text): **

| itemtype | what to write | what not to write |
|---------|--------|---------|
| translated text | translated text, translated text, translated text, translated text | translated text, translated text, translated text |
| translated text | translated texttraits, translated text, translated textdescription | translated text, translated text |
| translated text/translated text | type, translated text, usagetranslated text, translated textparameters | translated text, "translated text"translated text |

configuration: 
```
position: 1 (after_char)
order: 50-70
constant: false
keys: itemtranslated text,translated text,translated text(translated text)
scanDepth: 2
prevent_recursion: true
exclude_recursion: true
```

#### steps5: scenario/translated textentry

```yaml
<scene>
name: scenariotranslated text
location: geographyposition
description: scenariodescription——translated text, traits, translated textcharactertranslated text
</scene>
```

configuration: 
```
position: 1 (after_char)
order: 80-98
constant: false
keys: scenariotranslated text,translated text,translated text(translated text)
scanDepth: 2
prevent_recursion: true
exclude_recursion: true
```

#### steps6: story/chapterentry

translated textstoryphasetranslated textchaptertranslated text. formattranslated text, translated text. 

configuration: 
```
position: 1 (after_char)
order: 100
constant: false
keys: chaptertranslated text(translated text)
scanDepth: 2
prevent_recursion: true
exclude_recursion: true
```

---

### Phase 4: validate — finalizationself-check

allentrytranslated text: 

- translated textrecursiontranslated textalltranslated text(preventRecursion=true, excludeRecursion=true)
- translated textCharacter Cardtranslated textentrytranslated textalltranslated text(constant=true)
- translated textCharacter Cardtranslated textentrytranslated text(constant=false)translated textcomplete
- D1translated text(@D depth>=1)translated textentry
- contenttranslated textincludeforbidden words. translated text writing-optimization-guide.md translated text

> translated text, **musttranslated text `references/card-generator-guide.md`**, translated textcompleteparameters, config.json formattranslated text. translated textmusttranslated textscripttranslated text. 

---

## detailed specification

### entrytranslated textordertranslated text

| order | entrytype | position | constant | recursion | notes |
|-------|---------|----------|----------|------|------|
| 1 | worldview outline | 0 (before_char) | true | enable both | translated text |
| 4 | charactertranslated text | 1 (after_char) | true | enable both | translated textCharacter Cardtranslated text; translated textCharacter Cardtranslated text |
| 10+ | charactertranslated textentry | 1 (after_char) | translated text | enable both | XMLtranslated text, reference character-guide.md |
| 35+ | personalityentry | 1 (after_char) | translated text | enable both | translated textentry |
| 50-70 | item/abilityentry | 1 (after_char) | false | enable both | translated text |
| 80-98 | scenario/translated textentry | 1 (after_char) | false | enable both | translated text, scanDepth=2 |
| 99 | charactertranslated text | 1 (after_char) | translated text | enable both | translated text |
| 100 | NPC/story/translated text | 1 (after_char) | false | enable both | translated text |

### translated textrules

```
translated textCharacter Card
 └─ translated textcharactertranslated textentry → constant=true(translated text, translated textentry)

translated textCharacter Card
 ├─ charactertranslated text → constant=true(translated text)
 ├─ translated textcharactertranslated text → constant=false + keystranslated text
 └─ translated textcharacterpersonality → constant=false + keystranslated text

Worldviewentry
 └─ constant=true(translated text)

NPC / scenario / translated text / item / ability
 └─ constant=false + scanDepth=2
```

### positionconfiguration

| position translated text | translated text | translated text |
|-------------|------|-----------|
| 0 (before_char) | charactertranslated text | translated textWorldview. translated text, translated text, history |
| 1 (after_char) | charactertranslated text | charactertranslated text, item, scenario, NPC |
| 4 (at_depth) | Dtranslated text0 | translated textAItranslated text(secondary interpretationtranslated text) |

D1translated textcontent. translated textAI"translated texthistory", translated textcompletetranslated text, translated textAItranslated text. 

### XMLtranslated textYAMLformattranslated text

entrycontenttranslated textusage XML translated text YAML translated textformat: 

**musttranslated textrules: **
1. XMLtranslated text, translated textcontenttranslated text
2. translated textcontenttranslated text(2translated text4translated text)
3. translated textXMLformat. translated textXMLtranslated text, translated textmusttranslated text

**correctexample: **

```
<character>
 translated text: translated text
 age: 20
 appearance:
 translated text: 175cm
 translated text: translated text
 personality:
 - translated text
 - translated text
</character>
```

**errorexample(translated text): **

```
<character><name>translated text</name><age>20</age></character><!-- translated textXML, translated text -->
<character>translated text: translated text age: 20 appearance: translated text175cm</character><!-- contenttranslated text -->
```

### recursiontranslated text entrymusttranslated textrecursiontranslated text, translated text: 

- **translated textrecursion**(prevent_recursion / prevent_outgoing): translated textentrycontenttranslated textentry
- **translated textrecursion**(exclude_recursion / prevent_incoming): translated textentrycontenttranslated textentry

translated texttokentranslated text. translated textusagetranslated textconsequences. 

### translated text

- translated text `,` translated text, disabledtranslated text, translated text, translated text
- translated text: 
 - characterentry: full name,nickname,translated text(translated text: Qiu Mingyue,translated text,translated text)
 - NPCentry: full name,nickname,translated text,position(translated text: translated text,translated text,translated text)
 - scenarioentry: scenariotranslated text,translated text,translated text(translated text: translated text,translated text,translated text)
 - itementry: itemtranslated text,translated text,translated text(translated text: translated text,translated text,translated text)

---

## self-checklist

- [ ] translated textCharacter Cardtranslated textCharacter Card？
- [ ] entrytranslated textconfirm？
- [ ] translated textentrytranslated textconfirm？
- [ ] translated textcharacterentrytranslated textusagetranslated text `<character>` XML translated text(reference character-guide.md)？
- [ ] personalitytranslated textcharactertranslated textentry？
- [ ] translated textCharacter Cardtranslated textentrytranslated textalltranslated text？
- [ ] translated textCharacter Cardtranslated textentrytranslated textalltranslated text？
- [ ] translated textentrytranslated text, translated text？
- [ ] translated textentrytranslated text, translated text？
- [ ] translated textentrytranslated texttype/translated text/translated text, translated text？
- [ ] **translated textscripttranslated text `card-generator-guide.md`？**
- [ ] translated text `query.py --brief` validate？
- [ ] translated textentrytranslated textrecursion(translated textrecursion + translated textrecursion)translated text？
- [ ] D1translated textentry？
- [ ] XMLtranslated text, contenttranslated text？
- [ ] translated textusagetranslated text？
- [ ] filetranslated textincludeforbidden words？

---

## common error examples

❌ error: translated textCharacter Cardtranslated text5translated textentry, translated textpersonalityentrytranslated text
✅ correct: translated textCharacter Cardtranslated textentryalltranslated text, translated textentry

❌ error: entrycontenttranslated text"translated text, translated text, translated text"
✅ correct: translated text"translated text, translated text, translated text"

❌ error: translated textentrytranslated text"translated text18translated text, translated text3.5translated text, translated text"
✅ correct: translated text"translated text, translated text, translated text"

❌ error: translated textentrytranslated text"translated text, translated text, translated textequipment"
✅ correct: translated text"9mmtranslated text, usage9×19mmtranslated text, 15translated text"

❌ error: translated text5translated textentrytranslated text4translated text, translated textrecursion
✅ correct: translated textentrytranslated text, translated textrecursiontranslated text

❌ error: content translated textXMLtranslated text
✅ correct: XMLtranslated text, contenttranslated text

❌ error: translated textcharactertranslated textentry, translated text
✅ correct: translated textmusttranslated text, confirmtranslated textentry

❌ error: scenarioentrytranslated textkeystranslated text: translated text, translated text, translated text
✅ correct: scenarioentrytranslated textkeystranslated text: translated text,translated text,translated text

❌ error: Dtranslated text1translated textscenariotranslated textentry
✅ correct: D1translated text, scenarioentrytranslated textafter_charposition
