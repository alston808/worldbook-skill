# characterentrywritehard rules

translated textcharacterentrytranslated textcontenttranslated text, translated text. entrycontenttranslated text **XML translated text YAML** translated textformat: XMLtranslated text, translated textYAMLtranslated text. 

---

## translated text, characterentrycompletetranslated text

```yaml
<character>
name: translated text(English Name)
name_en: English Name
age: age + identitytranslated text
gender: gender
nicknames: nickname1, nickname2, nickname3
appearance:
 height: translated text(translated text+translated text)
 weight: translated text(translated text+translated text)
 three_sizes: translated text(if any, format: C86 - W60 - H88)
 hair: translated text/translated text/translated text/translated text——30translated text, translated texttraitsdo not writetranslated text
 eyes: translated text/translated text/translated text——30translated text, translated texttraitsdo not writetranslated text
 skin: translated text/translated text——20translated text, translated textdefaulttranslated texttraits
 build: translated text/translated text——20translated text
 clothing:
 translated text: xxx
 translated text: xxx
 distinguishing: translated texttraits, translated text, translated text
 voice: translated text/translated text/translated text
personality:
 mbti: MBTItype(if applicable)
 core_drive: translated text——translated text, translated text, translated text
 traits:
 - personality traits1(includetranslated text)
 - personality traits2
 - ...(10-15translated text)
 likes: translated text——translated text, translated textdo not writetranslated text
 dislikes: translated text——translated text
 habits: translated text/translated text——translated text
 hidden_self:
 - translated text——translated text/translated text/translated text
 - translated textcharactertranslated text, translated text
background: |
 translated text——translated text, translated text, translated text. 
 translated text"translated text"translated textkey events, do not writetranslated text. 
 translated text, translated text, translated text, translated text, translated text——translated text. 
abilities:
 - name: abilityname
 acquisition: translated text——translated text
 effects:
 - translated text——translated textdescription, translated textrather than"translated text"
 - translated text
relationships:
 - name: Character nametranslated text{{user}}
 detail: relationshipdescription——translated textrather thantranslated text. translated text, translated text, translated text. translated text, do not write"translated text"
</character>
```

---

## translated text, translated textfieldtranslated text

### 2.1 appearance. translated texttraits

AItranslated text. translated textdefaulttranslated text. 

| charactertype | translated text |
|----------|--------|
| translated text | translated text |
| translated text | translated text |
| translated text | translated text |
| 18translated text | translated text, translated text |

**what to write: ** translated text, translated text, translated text, translated text, translated text, translated text, translated text, translated text, translated text. 

**what not to write: ** translated text("translated text""translated text""translated text"), translated text("translated text""translated text"), translated text. 

**translated text: translated text, translated textappearance traitstranslated text？**

### 2.2 personality. translated text

- `traits` translated text(translated textdescriptiontranslated text)
- do not write"translated text"→ translated text"translated text. translated text, translated text"
- `hidden_self` translated text: "translated text, translated text(translated text)"

### 2.3 background. translated textkey events

- translated textbackground(translated text)
- translated text(translated textcharactertranslated text)
- do not write: "translated text""translated text"
- translated text: translated text, charactertranslated text？translated text→translated text

### 2.4 ability. translated text

- translated text, do not write"translated text""translated text"
- format: "translated textXtranslated textY" rather than "translated textXability"
- translated text effects translated text(translated text"usagetranslated text")

### 2.5 relationship. translated text

- do not write"translated text""translated text"
- translated text
- translated textrelationshiptranslated text

---

## translated text, completeexample

```yaml
<character>
name: Qiu Mingyue(Qiu Mingyue)
name_en: Qiu Mingyue
age: 17translated text·translated text·translated text
gender: translated text
nicknames: translated text, translated text, translated text
appearance:
 height: 168cm
 weight: 52kg
 three_sizes: B82 - W58 - H85
 hair: translated text, translated text, translated text, translated text
 eyes: translated text, translated text, translated text
 skin: translated text——translated text
 build: translated text, translated text(translated text), translated text
 clothing:
 translated text: translated text, translated text : translated textTtranslated text, translated text, translated text
 distinguishing: translated text, translated text, translated text
 voice: translated text, translated text. translated text, translated text. translated text
personality:
 mbti: ISTP(translated text)
 core_drive: translated text"translated text"translated text——translated textneedtranslated text, translated textneedtranslated text. translated textcharactertranslated text
 traits:
 - translated text, translated text——translated text
 - translated text——translated text, translated text. "translated text"translated text
 - translated text——translated text, translated text
 - translated text——translated text, translated text, translated text
 - translated text——translated textidentitytranslated text, translated text
 - translated text——translated text, translated text
 - translated text——translated text, translated text
 - translated text——translated text, translated text
 - translated text{{user}}translated text——translated text, translated text
 - translated text, translated text
 likes: translated text, translated text, translated text, translated text, translated text{{user}}translated text
 dislikes: translated text, translated text"translated text", translated text, translated text
 habits: translated text, translated text, translated textriff, translated text
 hidden_self:
 - translated text——is nottranslated text, translated text
 - translated text——"translated text"
 - translated text{{user}}translated text"translated text"——"translated text"
 - translated text, translated text
background: |
 translated text, translated text. translated text"translated text". translated text——translated text"translated text". translated text, translated textmusttranslated text——translated textidentitytranslated text. translated text{{user}}, {{user}}translated textsolotranslated text. 
abilities:
 - name: translated text
 acquisition: translated text——translated text
 effects:
 - translated text, translated textsolotranslated text
 - translated text(translated textDependenciestranslated text)
 - translated textability——translated text
 - name: translated text
 acquisition: translated text
 effects:
 - translated text, translated textitem
 - translated text, translated text——translated text"translated text"
relationships:
 - name: "{{user}}"
 detail: translated textsolotranslated text→translated text→translated text. translated text, translated text. translated text{{user}}, {{user}}translated text——translated text"translated text"translated text
 - name: translated text
 detail: translated text——translated text. translated text
 - name: translated text
 detail: relationshiptranslated text——translated text, translated text. translated text
 - name: translated text
 detail: translated text"translated text"translated text——translated text. translated text: "translated text"
</character>
```

---

## translated text, personalityentryformat

personalitymusttranslated textcharactertranslated text, translated textWorld Bookentry. formattranslated text XML translated text YAML: 

```yaml
<{{charactertranslated text/translated text}}_personality>
MBTI: xxxx
translated text: translated text, translated text, translated text
personality traits:
 - traits——translated text
 - ...
translated text:
 - translated text : translated text, translated text : translated text, translated text : translated text
</{{charactertranslated text/translated text}}_personality>
```

---

## translated text, personalitytranslated text

personality**do not writetranslated text**, translated textpersonalityWorld Bookentrytranslated text. 

"translated text17translated text, translated text, translated text"translated text. "translated text, translated text, translated text"translated textpersonality. 

translated text = AI translated textpersonalitytranslated text, translated textpersonalityentrytranslated text. 

---

## translated text, translated textrules

| error | correct |
|------|------|
| translated text, translated text, translated text | translated text, translated text |
| translated text, translated text | 168cm, translated text, translated text |
| translated text | do not write, translated textpersonalitytranslated text |
| translated textability | translated textsolo. translated text |
| translated text | translated text |
