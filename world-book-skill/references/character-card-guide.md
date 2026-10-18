# Character Cardwritetranslated text

> translated textCharacter CardWorld Bookentrytranslated textgreetingtranslated textwritetranslated text. description fieldtranslated text. characteralltranslated text(basic profile, appearance, background, relationship, personality)translated textWorld Bookentry. 

---

## This document covers

>translated textCharacter Cardtranslated textWorld Bookentrytranslated textgreetingwrite. translated textCharacter Cardcompletetranslated text(translated textcharactertranslated textWorld Bookentry + greetingtranslated textwrite), greetingtranslated text(translated text→characterstatus→usertranslated text→translated text→open ending), translated text MVU/EJS/HTML beautificationtranslated text. characterentrytranslated text character-guide.md translated text, Worldviewtranslated text world-building-guide.md translated text. 

---

## workflow

### Phase 1: translated textconfirm

translated text, confirmtranslated text: 

1. charactertranslated text: translated text, age, gender, identity, translated text user translated textrelationshiptranslated text
2. charactertranslated texttraitstranslated textappearance(is nottranslated text, translated texttraits)
3. charactertranslated textbackgroundtranslated text(translated textcharactertranslated text)
4. charactertranslated text user translated textrelationship(translated text, translated text, translated text)
5. translated textneedtranslated textscenariotranslated text(translated text/translated text/translated text/translated text)

translated textneedtranslated text: personalitytranslated text(translated text character-guide.md), Worldviewtranslated text(translated text world-building-guide.md). 

### Phase 2: writeWorld Bookcharacterentry

characteralltranslated textWorld Bookentry, description fieldtranslated text. translated textwritecharactertranslated textentry(XMLtranslated textYAML): 

```
<character>
name: translated text
name_en: English Name
age: age + identitytranslated text
gender: gender
nicknames: nickname1, nickname2, nickname3
appearance:
 height: translated text
 hair: translated text
 eyes: translated text
 ...
background: |
 key eventstranslated text
relationships:
 - name: Character name
 detail: relationshiptranslated text
</character>
```

completetranslated textfieldtranslated text `character-guide.md`. writetranslated textmusttranslated textappearancetranslated text. 

### Phase 3: writegreeting

translated textwrite 2-4 translated textoptionaltranslated text. translated text, translated text. 

translated text: 
1. translated text + translated text + translated text(translated text user translated text, translated text user translated text, translated text, translated text)
2. characterstatus(user translated textcharactertranslated text, translated textstatus)
3. user translated text(user translated textposition, status, translated textcharactertranslated textrelationship)
4. translated text(charactertranslated text user Note, translated text)
5. open ending(translated text user translated text. translated text user translated text, translated text user translated text)
6. translated textenabledtranslated text MVU translated text, translated text `<StatusPlaceHolderImpl/>` translated text "greetingtranslated text". 

### Phase 4: self-check

translated text: 

1. forbidden-word scan: reference writing-optimization-guide.md translated textforbidden wordstranslated text, translated text description translated textgreeting
2. appearancetranslated text: translated textcharactertranslated text
3. translated text: translated textscenario/translated text/translated text, translated text
4. open ending: translated text user translated text
5. translated text user: translated text user translated textappearance, translated text, personality, gendertranslated texttraits

---

## detailed specification

### translated text, Character Cardcompletetranslated text

Character Cardtranslated text, description translated text: 

| translated text | content | translated textfile |
|------|------|----------|
| World Bookcharacterentry | basic profile, appearance, background, relationship, personality | character-guide.md + translated textfile |
| Worldviewtranslated text | translated textbackground, rules, faction | world-building-guide.md + world-book-guide.md |
| greeting | translated textscenario, translated textoptionaltranslated text | translated textfile |

description fieldtranslated text. charactertranslated text(charactertranslated text + personality)translated textWorld Bookentry. personalitymusttranslated textcharactertranslated textentry. 

### translated text, World Bookcharacterentrywritetranslated text

characteralltranslated textWorld Bookentry, translated textconfiguration. charactertranslated textentrytranslated text"translated text"(basic profile), personalityentrytranslated text"translated text"(translated texttraits). translated textmusttranslated textentrytranslated text. 

#### 2.1 translated text , translated text: 

| field | description |
|------|------|
| translated text | characterfull name |
| age | translated text + translated text(translated text"17translated text") |
| gender | translated text/translated text/translated text |
| identity | translated text/translated text/translated text, translated text |
| translated text{{user}}relationship | translated text("translated text""translated text""translated text"), translated text |

"translated text{{user}}relationship"translated text. translated textrelationshiptranslated text"relationshiptranslated text"translated text. 

#### 2.2 appearance traits. translated texttraits, do not writetranslated text

appearancetranslated textis not"translated text", translated text"traits". traitstranslated text: translated textcharactertranslated text. 

**what to write: **
- translated textdefaulttranslated texttraits(translated text, translated text, translated text, translated text, translated text)
- translated text(translated text, translated text, translated text, translated text)
- translated text(translated text/translated text/translated text/translated text; "translated text"translated text)
- translated text(translated text, translated text)

**what not to write: **
- translated textdefault value. translated text/translated text/agetranslated textappearance(translated text, translated text, 18translated text, translated text)
- translated text. translated text, translated text, translated text
- translated text. translated text, translated text token translated textNotetranslated text
- translated text. translated textappearancetranslated textdescriptiontranslated text, translated textis nottranslated text
- "translated text"translated text. "translated text""translated text"translated textpersonalitytranslated textappearancetranslated text

**translated text: ** translated text, translated texttraitstranslated text？translated text → translated text. translated text → translated textis nottraits, translated text. 

#### 2.3 background setting. translated textkey events

translated text"translated textcharactertranslated text"translated text, do not writetranslated text. 

**what to write: **
- translated textbackground. translated textcharactertranslated text
- translated text. translated textcharactertranslated text
- translated text. translated textcharactertranslated text, translated text, translated text
- translated textrelationship. charactertranslated text, translated text

**what not to write: **
- translated textagetranslated text(translated textcharacter)
- translated textcharactertranslated textstatustranslated text
- translated text("translated text""translated text")

**translated text: ** translated text, charactertranslated text？translated text → translated text. 

#### 2.4 relationshiptranslated text. translated text, do not writetranslated text : charactertranslated text user translated text, translated text, translated text. 

**translated text: ** translated text, is nottranslated text. 

do not write"translated text"→ translated text: 
- translated text: translated text, translated text
- translated text: translated text, translated text
- translated text: translated text(translated text, translated text, translated text)

"translated text"translated text"translated text"translated text. translated text, translated text. 

"translated text user translated text, translated text user translated text, translated text". translated text, translated text, translated text. translated textneedtranslated text"translated text", translated textbackgroundtranslated text, translated text. 

### translated text, greetingtranslated text

greetingtranslated text user translated textcharactertranslated text. translated text user translated text. greetingtranslated textCharacter Cardtranslated text. forbidden wordstranslated text, translated text. 

#### 4.1 translated text greetingtranslated textordertranslated text. translated text, translated text: 

**translated text: translated text + translated text + translated text**

translated text user translated text, translated text user translated textscenariotranslated text: 
- translated text(translated text, translated text, translated text)
- translated text(translated text, translated text/translated text)
- translated text(user translated textposition, translated text)
- translated text/translated text(translated textscenariotranslated text)

do not write"translated text""translated text"translated text. translated text. 

**translated text: characterstatus**

user translated textcharactertranslated text, translated textstatus: 
- charactertranslated textposition(translated text, translated text, translated text)
- charactertranslated text(translated text, translated text)
- charactertranslated text(translated text, translated textstatustranslated text, is notappearancetranslated text)

translated text user translated text. do not writecharactertranslated text. do not write"translated text". translated text. 

**translated text: user translated text**

user translated textposition, status, translated textcharactertranslated textrelationship: 
- user translated text(translated text, translated text, translated text)
- user translated textcharactertranslated textrelationship
- user translated text(translated text, translated text, translated text, translated text. translated text, do not writetranslated text)

translated text user translated texttraits. do not write user translated textappearance, gender, personality, translated text. user translated text user translated text. 

**translated text: translated text**

charactertranslated text user Note, translated text: 
- charactertranslated text(translated text)
- charactertranslated text(translated text, translated textposition, translated text)

translated textcharactertranslated text. translated textcharactertranslated text user translated text. user translated textneed"translated text", charactertranslated text. 

**translated text: open ending**

translated text user translated text. translated text user translated text, translated text user translated textcharactertranslated text, translated text user translated text. translated textcharactertranslated text, translated text, translated text user translated text. 

**translated text(MVU enabledtranslated text): ** translated text `<StatusPlaceHolderImpl/>`

#### 4.2 translated text

**translated text. ** translated textscenario, translated text, translated text. do not writetranslated text. translated text. translated text → translated text → translated text. 

**scenariotranslated text. ** translated text. translated text, translated text, translated text. is not"translated text", translated text"translated text, translated text". 

**user translated text. ** translated text user translated text. user translated text, translated text, translated text. charactertranslated text user translated text. do not write. 

**open ending. ** translated text user translated text. translated text"translated text user translated text"translated textposition. translated text, translated text, translated text user translated text. 

**translated text user. ** translated textdo not write user translated texttraits. appearance, personality, gender, translated text, translated text. user translated text user translated text. translated textcharactertranslated text user translated textscenariotranslated text. 

**translated textcharacter. ** greetingtranslated text"charactertranslated textscenariotranslated text user translated text, translated text". charactertranslated text, translated text, translated textposition. translated textgreetingtranslated textcontent. user translated text. 

#### 4.3 greetingtranslated text filetranslated textforbidden wordstranslated text. translated textforbidden wordstranslated text writing-optimization-guide.md translated text. translated textgreetingtranslated texthard rules: 

1. **do not writetranslated textcharactertranslated text/translated text. ** charactertranslated text, translated text"translated text". "translated text"translated text, "translated text"translated text. translated text → translated text. 
2. **translated text. ** "translated text, translated text". "translated text"translated text. translated text, translated text"translated text"translated text. translated text → translated text. 
3. **translated text. ** scenariotranslated text. charactertranslated text. user translated text. translated text, translated text. user translated text. 

translated textforbidden words(translated text, translated text, translated text, translated text, translated text, translated text)translated text writing-optimization-guide.md. greetingwritetranslated textmusttranslated textfiletranslated textforbidden wordstranslated text. 

#### 4.4 translated textoptionaltranslated text Character Cardtranslated text 2-4 translated text alternate_greetings. translated text: 

| translated text | translated text |
|------|----------|
| translated text | translated text/translated text/translated text/translated text |
| translated text | translated text/translated text/translated text/translated text |
| translated text | charactertranslated text/charactertranslated text/charactertranslated text user translated text/charactertranslated text |
| translated textrelationship | user translated textcharactertranslated text/charactertranslated text user translated text/translated text/translated text |

translated text. translated text, translated textscenario, translated text. 

#### 4.5 greetingtranslated text greetingtranslated text. translated textcontenttranslated text `[...]` translated text: 

```
[translated text]. [translated text], [translated text/translated text/translated text——user translated text]. 

[Character name][position], [translated text——translated text]. [user translated text——translated text, charactertranslated text]. 

translated text[user translated text/status/position——translated text, translated text, translated textcharactertranslated textrelationship]. 

[charactertranslated text user translated text——translated text]. 

[charactertranslated text, translated text user translated text——open ending]. [translated textenabledMVU, translated text] <StatusPlaceHolderImpl/>
```

---

## translated text, MVU / EJS / HTML translated text(translated text)

translated text reference filetranslated text. translated textfiletranslated textdescription: 

| translated text | translated textfile | description |
|------|----------|------|
| user request MVU variable system | translated text mvu-guide.md | variabletranslated text, translated text, updatetranslated text |
| user request EJS translated text | translated text ejs-guide.md | EJS translated text, phasetranslated text, Dependencies MVU |
| user request HTML beautificationtranslated text | translated text html-beautify-guide.md | translated text HTML translated text, translated text |

translated text, translated text reference filetranslated text. 

---

## self-checklist

### World Bookcharacterentrytranslated text

- [ ] description fieldtranslated text(do not writetranslated textcontent)
- [ ] translated textcharactertranslated textalltranslated textWorld Bookentry
- [ ] charactertranslated textentrytranslated textpersonalityentrytranslated textentrytranslated text

### greetingtranslated text

- [ ] translated textincludecompletetranslated text
- [ ] translated text, translated text, translated text, translated text user translated text
- [ ] characterstatustranslated text user translated text
- [ ] translated text user translated texttraits(appearance, gender, personalitytranslated text)
- [ ] translated textcharactertranslated text
- [ ] translated text, translated text user translated text
- [ ] translated text
- [ ] translated text
- [ ] translated textscenariotranslated text

### forbidden wordstranslated text(translated text)

- [ ] translated text(translated text writing-optimization-guide.md): matches are 0
- [ ] translated text: matches are 0
- [ ] translated text: matches are 0
- [ ] translated text: matches are 0
- [ ] translated text: matches are 0
- [ ] translated text: matches are 0
- [ ] metaphor forbidden words(translated text writing-optimization-guide.md metaphor forbidden wordstranslated text): matches are 0
- [ ] translated text(translated text writing-optimization-guide.md translated text): matches are 0
- [ ] translated text(translated text writing-optimization-guide.md narrative forbidden wordstranslated text): matches are 0
- [ ] translated textcharactertranslated text/translated text: no matches in full text
- [ ] translated textcharactertranslated text/translated text/translated text/translated text: no matches in full text
- [ ] translated text: no matches in full text

### translated text

- [ ] translated text 2-4 translated textoptionaltranslated text
- [ ] translated text/translated text/translated text
- [ ] translated textenabled MVU, translated text `<StatusPlaceHolderImpl/>`
- [ ] filetranslated textforbidden words

---

## common error examples

### World Bookcharacterentryerror

**error 1: appearancetranslated text**

```
appearance traits:
 translated text: translated text, translated text, translated text, translated text : translated text, translated text : translated text
```
issues: translated text, translated text. translated textcharactertranslated text. 

correct: 
```
appearance traits:
 translated text: translated text, translated text, translated text : translated text, translated text : translated text, translated text
 traits: translated text
```

**error 2: appearancetranslated texttraits**

```
translated text: translated text, translated text : translated text
```
issues: translated textis nottranslated text. translated texttraitstranslated text. 

correct: 
```
translated text: translated text : translated text
```

**error 3: relationshiptranslated text**

```
translated textuserrelationship: translated text, translated text
```
issues: translated text, translated textcontent. 

correct: 
```
translated textuserrelationship:
 translated text: usertranslated textsolotranslated text : translated text, translated text : translated text——translated textusertranslated text, usertranslated text
```

**error 4: backgroundtranslated text**

```
background: translated text, translated text, translated text. translated text, 
translated text. translated text, translated text, translated text, translated text. translated text , translated text. 
```
issues: translated textcharactertranslated text. translated text. 

correct: 
```
background:
 translated text: translated text, translated text :
 - translated text
 - translated text, translated text
 - translated textmusttranslated text"translated text"translated text
```

**error 5: charactertranslated textentrytranslated textpersonality**

```
# ❌ charactertranslated textentry
<character>
name: Qiu Mingyue
personality:
 mbti: ISTP
 traits:
 - translated text, translated text
</character>
```
issues: personalitytranslated textcharactertranslated textentrytranslated text. translated textentrymusttranslated text. 

correct: translated textpersonalitytranslated text `<Qiu Mingyue_personality>` entrytranslated text(translated text character-guide.md translated text), charactertranslated textentrytranslated textdo not writepersonalitycontent. 

### greetingerror

**error 1: translated text user traits**

```
translated text, translated text. translated text, 
translated text. 
```
issues: translated text user translated text, translated text, translated textidentity, translated text. translated textis nottranslated text. 

correct: do not write user translated text, appearance, identity, translated text. translated textcharactertranslated textscenario. 

**error 2: translated text user translated text**

```
Qiu Mingyuetranslated text, translated text: "translated text. "
translated text, translated text. translated text. 
```
issues: "translated text"translated text user translated text. "translated text"translated text user translated text. user translated text, translated text. 

correct: translated textcharactertranslated text, translated text user translated text. 

**error 3: translated text**

```
translated text, translated text, translated text. 
```
issues: "translated text"translated text. translated text, translated textneedtranslated text"translated text". 

correct: 
```
translated text, translated text. translated text. 
```

**error 4: translated textcharactertranslated text**

```
translated text, translated textconfirmtranslated textis nottranslated text. translated text . 
```
issues: "translated textconfirmtranslated textis nottranslated text"translated textcharactertranslated text. "translated text"translated text, is not user translated text. 

correct: 
```
translated text. translated text, translated text. 
```

**error 5: translated text**

```
translated text, translated text. 
```
issues: "translated text"translated text user translated text. translated text, translated text. 

correct: 
```
translated text. translated text. translated text. 
```

**error 6: translated textcharactertranslated text**

```
translated text, translated text, translated text. 
```
issues: "translated text"translated textcharactertranslated text. translated text, translated textneedtranslated text. 

correct: 
```
translated text, translated text, translated text. 
translated text, translated text. 
translated text. 
```

---

## Character Cardcompleteoutputexample

translated textCharacter Cardtranslated textWorld Bookentrytranslated textgreetingoutputexample. charactertranslated textQiu Mingyue, translated textWorld Bookentrytranslated text. 

### World Bookentry

```yaml
<character>
name: Qiu Mingyue
name_en: Qiu Mingyue
age: 17translated text·translated text·translated text
gender: translated text
nicknames: translated text, translated text, translated text
appearance:
 height: 168cm
 hair: translated text, translated text, translated text
 eyes: translated text, translated text, translated text
 skin: translated text——translated text
 clothing:
 translated text: translated text, translated text : translated textTtranslated text, translated text, translated text
 distinguishing: translated text, translated text, translated text
background: |
 translated text, translated text. translated text. translated text. translated text, translated textidentitytranslated text. translated text{{user}}. 
relationships:
 - name: "{{user}}"
 detail: translated textsolotranslated text→translated text→translated text. translated text"translated text"translated text
 - name: translated text
 detail: translated text, translated text
</character>
```

personalityentrytranslated text `character-guide.md` translated text. 

### greeting

**translated text 1 . translated text**

```
translated text. translated text, translated text. 

Qiu Mingyuetranslated text, translated text. translated text, translated text, translated text. translated text, translated text. translated text, translated text. 

translated text. translated text. 

translated text, translated text. "translated text. "translated text, translated text. 

<StatusPlaceHolderImpl/>
```

**translated text 2 . translated text**

```
translated text. translated text, translated text. 

Qiu Mingyuetranslated text, translated text. translated text, translated text, translated text. 

translated text, translated textTtranslated text. translated text, translated text. 

"translated textsolotranslated text. "

translated text, translated text, translated text. 

<StatusPlaceHolderImpl/>
```

**translated text 3 . translated text**

```
translated text. translated text, translated text. translated text, translated text. 

Qiu Mingyuetranslated text. translated text, translated text. translated text. 

translated text. translated text, translated text, translated text. 

"translated text. "

translated text, translated text. 

<StatusPlaceHolderImpl/>
```

---

> **translated text: ** World Bookentrywritetranslated text → translated text writing-optimization-guide.md translated textforbidden-word scan → world-building-guide.md writeWorldviewentry → config-guide.md configurationWorld Book → card-generator-guide.md generate JSON. translated text MVU/EJS/HTML translated text, translated textreference mvu-guide.md, ejs-guide.md, html-beautify-guide.md. 
