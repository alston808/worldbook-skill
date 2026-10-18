# derivativeinformation extractiontranslated text

> translated textfiletranslated textderivativetranslated text. translated text/translated text/translated text, translated textfiletranslated textinformation extraction. originaltranslated text. 

---

## This document covers

>translated textderivativetranslated textextracttranslated text. translated textextractcharacter(8translated text: translated text, appearance, identity, personalitytranslated text, key events, relationship, ability, chapter appearance), Worldview(A/B/Ctypetranslated textgeography/history/faction/rules/translated textextract)translated textitem/chaptertranslated text, output outline.txt translated textentrywriteusage. 

---

## workflow

### Phase 1: translated text

#### steps 1: translated textsource

- translated text/translated textfile → readtranslated textfile, translated textsteps 3. 
- user requestusagetranslated text → translated textsteps 2. 
- translated textfiletranslated text → translated text, translated textneedtranslated text. 

#### steps 2: translated text : 

1. translated textextract. 
2. translated text, translated text(translated text 50-100 translated text). 
3. translated text txt file, translated text. 
4. translated textwriteentrytranslated text, translated textreadtranslated text txt filetranslated text. 

**translated textexample: **

```
# translated text
## characterA
- identity: XXtranslated text, translated text(source: translated text)
- appearance: translated text, translated text(source: wikicharactertranslated text)
- key events: translated textXXtranslated text, translated text(source: translated text)

## Worldview
- XXtranslated text: translated text, translated text(source: translated text)
```

#### steps 3: original texttranslated textline numbertranslated text /translated text: 

1. **translated textline number. ** translated textchaptertranslated textline numbertranslated text, translated text. 

```
translated text1translated text: L1 - L350
translated text2translated text: L351 - L720
translated text3translated text: L721 - L1100
```

2. **translated text. ** translated textmarktranslated textcontenttranslated text: 

| mark | translated text | example |
|------|------|------|
| `[W]` | Worldviewtranslated text: translated textgeography, history, faction, rules, translated text | `[W] translated text` |
| `[C]` | charactertranslated text: translated text, appearancetranslated text, backgroundtranslated text, relationship | `[C] translated text, translated text, 168cm` |
| `[I]` | item/ability/translated text | `[I] translated text` |
| `[★]` | translated textchapter: translated textcharactertranslated textstorytranslated text | `[★] translated text5translated textcharactertranslated text, translated text` |

3. **charactertranslated text. ** translated textcharacter: 
 - translated text(translated text)
 - translated textcharactertranslated textchapterlist

```
charactertranslated text: 
- translated text: translated text20translated text, translated text. translated text: translated text1/3/5/7/8translated text
- translated text: translated text, translated textability. translated text: translated text1/2/4/6/8translated text
```

---

### Phase 2: characterextract

translated textcharacter, translated textextract. translated textoutputformattranslated text: 

```
### [translated textname]
- translated text: (translated text)
- translated text: (1-3translated textoriginal texttranslated text, translated textchapterline number)
- forbidden wordsmark: (original texttranslated text/forbidden words, translated text)
- extraction result: (translated textforbidden wordstranslated textcontent, translated textentryfield)
```

#### translated text 1: translated text

**extractcontent: **
- translated text, age, gender, identitytranslated text
- translated textchaptertranslated textline number
- original texttranslated text {{user}} translated textrelationshipdescription(if applicable)

**Notetranslated text: **
- ageoriginal texttranslated text, mark `// original texttranslated text`
- identitytranslated text, translated text

#### translated text 2: appearance traits

**musttranslated text `character-guide.md` translated textappearancerulestranslated text: **

| rules | description |
|------|------|
| do not writedefaulttraits | translated textdo not writetranslated text, translated textdo not writetranslated text, translated textdo not writetranslated text, 18translated textdo not writetranslated text |
| do not writetranslated text | "translated text""translated text""translated text""translated text". translated textcharactertranslated textextract |
| do not writetranslated text | "translated text""translated text""translated text"→ translated texttraitstranslated text |
| translated texttraits | translated text, translated text, translated text, translated text, translated text, translated text, translated text, translated text, translated text |

**translated text: translated text, translated textappearancetranslated textcharacter？**

**extractoutputformat: **
```
### appearance traits
- translated text: (translated textappearancetranslated text: translated text/translated text/translated text)
- translated text: 
 "translated text" — translated text3translated text L450
 "translated text, translated text" — translated text1translated text L20
- forbidden wordsmark: 
 "translated text" → translated text, translated text, changed to"translated text"
 "translated text" → translated text, translated text
 "translated text" → AItranslated textdefault value+translated text, translated text
- extraction result: 
 translated text: translated text
 (translated texttraits, do not writetranslated text skin field)
```

#### translated text 3: identitytranslated text

- age(translated textoriginal texttranslated text)
- gender
- identity/translated text/translated textcharacter
- translated text {{user}} translated textrelationshiptranslated text(if applicable)
- original texttranslated text

#### translated text 4: personalitytranslated text

**translated text: translated textextractoriginal texttranslated text, is nottranslated textpersonalitytranslated text. **

- original texttranslated text"translated text" → translated textextract, translated textdescriptiontranslated text"translated text"translated text
- original texttranslated text"translated text" → translated textextract, translated text
- translated textoriginal texttranslated text → translated textpersonalitytranslated textextract

**extracttranslated text: **
1. translated textextract(translated text, translated text)
2. translated textextract(translated text, translated text)
3. translated textextract(translated text, translated textneedtranslated text)
4. translated textextract(translated text, translated texthiddentranslated text)

**extractoutputformat: **
```
### personalitytranslated text
- translated text: (translated textpersonalitytranslated text: translated text/translated text/translated text)
- translated text+translated text: 
 - translated text: translated text？translated text？
 translated text: "translated text, translated text" — translated text1translated text L88-L95
 translated text: translated text——translated text
 - personality traits1(description+translated text): 
 original text: "translated text'translated text', translated text" — translated text5translated text L560
 extract: translated text——translated text, translated text
 - personality traits2: 
 original text: "translated text" — translated text8translated text L1050
 translated text: translated text → translated text
- forbidden wordsmark: translated textoriginal texttranslated text"translated text"translated text → translated text"translated textxxtranslated text", translated text
- extraction result: (translated textpersonality = translated text + original texttranslated text)
```

#### translated text 5: key events

**translated textextract"translated textcharacter"translated textkey events. ** translated text: translated text, charactertranslated text？translated text → translated textextract. 

- translated textoriginal texttranslated text(translated text, translated text, translated text, translated text)
- translated textextracttranslated text
- translated textchaptertranslated text

#### translated text 6: relationshiptranslated text

- translated textrelationshiptranslated text: translated text, translated text, relationshiptranslated text
- **translated text, do not writetranslated text. **
 - do not write"translated text" → translated text"translated text, translated text"
 - do not write"translated text" → translated text"translated text, translated text"
- translated textrelationshiptranslated text

**extractoutputformat: **
```
### relationshiptranslated text
- translated text(translated textchapter): 
 "translated text" — translated text1translated text L100
 "translated text" — translated text7translated text L890
- extraction result: 
 translated text: translated text → translated text"translated text"translated text"translated text". 
```

#### translated text 7: abilitytranslated textitem

- translated textabilitytranslated text(original texttranslated textsource/translated text)
- translated textabilitytranslated text(original texttranslated text, is not"translated text"translated textdescription)
- format: "translated textXtranslated textY" rather than "translated textXability"
- translated text(translated text"usagetranslated text")

#### translated text 8: chapter appearancetranslated text

listformat, translated textcharactertranslated textoriginal texttranslated textchapter: 
```
chapter appearance: 
- translated text1translated text L1-L350(translated text, translated text)
- translated text3translated text L721-L1100(translated text)
- translated text5translated text L1500-L1800(translated textchapter, translated text)
```

---

### Phase 3: Worldviewextract

#### steps 1: typetranslated text `world-building-guide.md` translated textWorldviewtype: 

| type | traits | example | extracttranslated text |
|------|------|------|---------|
| **A** | translated textbackground | translated text, translated text, translated text | translated textextract AI translated text |
| **B** | translated text | translated text, translated text, translated text | extracttranslated text AI translated text |
| **C** | translated text | translated textoriginaltranslated text, translated text, translated text | completeextracttranslated text |

**translated text: translated text, AI translated textcorrecttranslated text？translated text → translated textextract. translated text → extract. **

#### steps 2: translated textextract

translated textextract. translated textoutputformattranslated textcharacterextracttranslated text(translated text + translated text + extraction result). 

**translated text 1: geographytranslated text**
- translated text, translated texttraits
- translated text(translated text/translated text/translated text)
- translated textextractgeographytranslated text, translated textoriginal texttranslated text

**translated text 2: historytranslated text**
- translated texthistorytranslated text
- translated textbackground(translated text/translated text)
- translated textextracttranslated texthistory, translated textextracttranslated text(translated textcharactertranslated text)

**translated text 3: factiontranslated text**
- name + translated text
- factiontranslated textrelationship
- translated textfactiontranslated text

**translated text 4: rulestranslated text**
- translated textsource(translated text/translated text/translated text/translated text)
- translated text/phasetranslated text(if any)
- translated text
- translated text

**translated text 5: translated text**
- translated text/translated text(if any)
- translated text(if anytranslated text/translated text/translated text)
- translated text(AItranslated text)

#### steps 3: extracttranslated text

| original texttranslated text | extracttranslated text |
|---------|---------|
| "translated text, translated text" | translated text |
| "translated text" | translated text: translated text |
| "translated text" | translated text: translated text, translated text, translated text... |
| "translated text" | translated text |
| "translated text...translated text""translated text""translated text" | translated textlisttranslated text |

---

### Phase 4: output outline.txt

translated textPhase 1translated textextracttranslated text, translated text outline.txt. filetranslated textformat: `<World Booktranslated text>_outline.txt`, translated text. 

#### outline.txt completetranslated text

```yaml
# World Booktranslated text: <World Booktranslated text>

## translated text :
 translated text: <translated textcontent>
 translated text: <translated textneedtranslated text——translated text"light noveltranslated textCharacter Card"translated textneedextractWorldview>
 translated text: <translated text？translated text？>

entrytranslated text:
 Worldviewtype: A / B / C
 translated textcharactertranslated text: N
 translated textentrytranslated text: translated text X translated text type: translated textCharacter Card / translated textCharacter Card

---

## chapterline numbertranslated text 1translated text: L1 - L350
translated text2translated text: L351 - L720
translated text3translated text: L721 - L1100
...

---

## charactertranslated text
- <Character name>: <translated text>. chapter appearance: translated text1/3/5/7translated text
- <Character name>: <translated text>. chapter appearance: translated text2/4/6translated text
...

---

## charactertranslated text
- <Character name>: <translated text——translated text, translated text>
- <Character name>: <translated text>

---

## Worldviewtranslated text
Worldviewtype: A / B / C
translated textrules: <1-3translated text>
translated text: <translated text>
faction: <translated textfaction>
translated text: <translated text>

---

## translated textchaptertranslated text

### translated text[Character name]translated textchapter
- translated textXtranslated text Lxxx-Lxxx: <translated text——translated textcharactertranslated text>
- translated textYtranslated text Lxxx-Lxxx: <translated text>

### translated textstorytranslated textchapter
- translated textXtranslated text Lxxx-Lxxx: <translated text——translated text>
- translated textYtranslated text Lxxx-Lxxx: <translated text>

---

## entrytranslated text
| entryname | type | position | translated text | order | translated texttoken | Dependencieschapter |
|----------|------|------|------|------|-----------|---------|
| worldview outline | Worldview | ↑Char | translated text | 1 | ~200 | - |
| translated text·XXX | character | ↓Char | translated text | 99 | ~400 | translated text1/3/5translated text |
| translated text·YYY | character | ↓Char | translated text | 99 | ~350 | translated text2/4/6translated text |
| item·ZZZ | item | ↓Char | translated text | 95 | ~150 | translated text2/7translated text |
| story·translated text1translated text | chapter | ↓Char | translated text | 201 | ~200 | translated text1translated text |
| forbidden words·translated text | forbidden words | ↑AT | translated text | 1 | ~150 | - |
| forbidden words·translated text | forbidden words | ↑AT | translated text | 2 | ~120 | - |
| forbidden words·translated text | forbidden words | ↑AT | translated text | 3 | ~150 | - |
...
```

#### outline.txt rules

- **Dependencieschaptertranslated text**: translated textentrytranslated textneedtranslated textchapter. translated textwriteentrytranslated text, musttranslated textchapter. 
- **translated text**: is nottranslated text, translated textreadtranslated textchaptertranslated textline numbertranslated text, translated textentrytranslated text. 
- **forbidden wordsentrytranslated text**: translated textWorld Bookmustincludetranslated textforbidden wordsentry. 
- **translated textentry**, translated textsteps. 

---

## detailed specification

### extracttranslated textoutputformat(translated text)

translated textextracttranslated textmusttranslated textoutput: 

```
### [translated textname]
- translated text: (1-2translated text, translated text)
- translated text: (1-3translated textoriginal texttranslated text, translated text"translated textXtranslated text Lxxx"translated text)
- forbidden wordsmark: (translated textoriginal texttranslated textforbidden wordstranslated text, translated text)
- extraction result: (translated textforbidden wordstranslated textcontent, translated textentryfield)
```

### forbidden wordstranslated text extractoriginal texttranslated text, translated textcontentmusttranslated text: 

| translated text | translated textcontent | translated text |
|------|---------|---------|
| translated text | "translated text""translated text""translated text""translated text" | translated texttraitstranslated text: "translated text""translated text""translated text" |
| translated text | "translated text""translated text""translated text""translated text" | translated text, translated textcharactertranslated text |
| defaulttraits | translated text, 18translated text, translated text | translated text, AItranslated text |
| narrative forbidden words | translated text, translated text, translated text, translated text, translated text, translated text | translated text |
| personalitytranslated text | "translated text""translated text""translated text""translated text" | translated textoriginal texttranslated text |
| translated text | "translated text""translated text""translated text" | translated text |
| translated text | "translated text" | translated text, translated text |
| translated text | "translated text""translated text" | translated text, translated textcontent |

### translated textrules

- original texttranslated textfield → translated text, mark `// original texttranslated text`
- original texttranslated text → translated textextracttranslated text, translated text
- original texttranslated text → translated text, translated textif anytranslated textentrytranslated textdescription"translated textXtranslated text"
- translated textcharactertranslated textpersonalitytranslated text → translated text"translated text", translated textoriginal texttranslated text

### translated textrules

- translated textcharacter/itemtranslated textchaptertranslated text → translated text, translated textchapter appearancetranslated text
- translated textchaptertranslated text"translated text"translated text"translated text", translated textentry
- translated text → translated text, translated text, descriptiontranslated text

---

## self-checklist

translated textinformation extractiontranslated text, translated text: 

### translated textphase
- [ ] translated textfiletranslated textcompleteread
- [ ] translated textchaptertranslated textline numbertranslated text
- [ ] charactertranslated textchapter appearancetranslated text
- [ ] [W]/[C]/[I]/[★] marktranslated text
- [ ] translated text, translated text txt translated text

### characterextractphase
- [ ] translated textcharactertranslated textalltranslated textextract(translated text, appearance, personality, key events, relationship, ability, chapter appearance)
- [ ] translated textextracttranslated textincludetranslated text AI default valuetranslated texttraits
- [ ] translated texttraitstranslated text
- [ ] "translated text""translated text""translated text"translated text
- [ ] personalitytranslated textoriginal texttranslated text(translated textpersonality)
- [ ] relationshiptranslated text(translated text"translated text""translated text"translated text)
- [ ] key eventstranslated textextract"translated textcharacter"translated text(translated text)
- [ ] translated textchaptertranslated text
- [ ] translated textappearance traitstranslated textcharacter

### Worldviewextractphase
- [ ] Worldviewtype(A/B/C)translated text
- [ ] extracttranslated texttypetranslated text(A translated text, B translated text, C completeextract)
- [ ] geography/history/faction/rules/translated textextract
- [ ] translated text
- [ ] original texttranslated textgeographytranslated text
- [ ] translated text

### outline.txt phase
- [ ] translated textcomplete(translated text + translated text + translated text)
- [ ] chapterline numbertranslated textcomplete
- [ ] charactertranslated textcharactertranslated text
- [ ] Worldviewtranslated text
- [ ] translated textchaptertranslated text(translated text)
- [ ] entrytranslated textDependencieschaptertranslated text
- [ ] forbidden wordsentrytranslated text(translated text)
- [ ] translated text `// original texttranslated text` translated textfieldtranslated text

### forbidden wordsself-check
- [ ] outline.txt translated textforbidden words(translated text/translated text/translated text/translated text/translated text)
- [ ] outline.txt translated text
- [ ] outline.txt translated text

---

## common error examples

### error 1: translated textoriginal texttranslated text

original text: "translated text, translated text. "

extract: 
"translated text, translated text. "

correct: 
- translated textmark: "translated text"→ translated text, translated text. "translated text"→ translated text, translated text. 
- extraction result: translated text: translated text. translated text. 

---

### error 2: extracttranslated text

original text: "translated text, translated text, translated text. "

extract: 
"appearance: translated text, translated text, translated text. "

correct: 
- translated textmark: "translated text"→ translated text, translated text. "translated text"→ AIdefault value, translated text. "translated text"→ translated text, translated text. 
- extraction result: translated text: translated text. (translated texttraits, translated textextract)

---

### error 3: personalitytranslated text

original texttranslated text: translated text, translated text, translated text. 

extract: 
"personality: translated text. "

correct: 
"personality: translated text(translated text3translated text L420). translated text(translated text5translated text L680). translated text(translated text8translated text L1200). "

---

### error 4: relationshiptranslated text

original texttranslated text: translated text, translated text, translated text. 

extract: 
"translated text: relationshiptranslated text, translated text. "

correct: 
"translated text → translated text: translated text(translated text1translated text L100). translated text(translated text7translated text L890). translated text(translated text12translated text L1800). "

---

### error 5: extract AI translated text

original text: 22translated text, translated text, translated text. 

extract: 
"appearance: 22translated text, translated text, translated text. "

correct: 
- translated textmark: translated text → translated textdefault, "translated text"→22translated textdefault. 
- extraction result: translated textappearance traits, do not writetranslated textappearancefield. 

---

### error 6: translated textoriginal texttranslated text

original texttranslated textcharactertranslated text, age, translated text, translated textbackground. 

extract: 
"background: translated text, translated text, translated text. "

correct: 
"background: // original texttranslated text"

---

### error 7: Worldviewextracttranslated text

original text: "translated text, translated text. translated text, translated text. "

extract: 
"Worldview: translated text, translated text, translated text. "

correct: 
- translated textmark: "translated text"→ translated text. "translated text"→ translated text. "translated text""translated text""translated text"→ translated text. 
- extraction result: background: translated text. translated text: translated text. translated text: translated text. 

---

### error 8: entrytranslated textforbidden wordsentry

entrytranslated textcharacterentrytranslated textWorldviewentry, translated textforbidden wordsentrytranslated text. 

correct: 
entrytranslated textmustincludetranslated text: 
| forbidden words·translated text | forbidden words | ↑AT | translated text | 1 |
| forbidden words·translated text | forbidden words | ↑AT | translated text | 2 |
| forbidden words·translated text | forbidden words | ↑AT | translated text | 3 |

---

### error 9: translated text , translated textentry, translated text"Dependencieschapter"translated textchapter. 

consequences: appearancetranslated text(translated text1translated text, translated text5translated text, translated text5translated text); relationshiptranslated text(translated text3translated textrelationshiptranslated text, translated text"translated text"). 

correct: 
1. translated text"entrytranslated text"translated textentrytranslated text"Dependencieschapter"translated text
2. translated textreadtranslated textchaptertranslated textline numbertranslated text
3. translated textentrytranslated text(is nottranslated text)
4. translated textoriginal texttranslated text, translated textentry
