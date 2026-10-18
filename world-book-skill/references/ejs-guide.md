# EJS dynamic contenttranslated text

> EJS Dependencies MVU translated textvariable. MVU translated textneed EJS, translated text EJS musttranslated text MVU variabletranslated text. translated textWorld Bookentrytranslated text"translated textvariabletranslated textcontent"translated textentry. 

## This document covers

>translated text EJS dynamic contenttranslated text. translated text MVU variable system(Affinity, relationship status, translated text), writetranslated textcodetranslated textWorld Bookentrytranslated textvariabletranslated textcontent. translated text EJS codetranslated text, translated textcontent, translated textphasetranslated text. 

---

## workflow

### Phase 1: confirm MVU variablepath

translated text EJS codetranslated text, musttranslated textconfirmtranslated text: 

1. **Affinitypath**: translated text `stat_data.Character name.Affinity`
2. **relationship statuspath**: translated text `stat_data.Character name.relationship status`
3. **translated textvariable**: translated text, translated textphase, translated textphasetranslated textvariable
4. **default value**: translated textvariabletranslated text

> variablepathtranslated text `mvu-guide.md`. translated texthard rules: EJS translated textread MVU variablemusttranslated text `stat_data` prefix, translated text `[0]` translated text. 

#### phasetranslated text phasetranslated text: 

```
Phase 1(translated text): Affinity < 150, relationship statustranslated text"translated text"
Phase 2(translated text): Affinity 150–400, relationship statustranslated text"translated text"
Phase 3(translated text): Affinity 400–700, relationship statustranslated text"translated text"
Phase 4(translated text): relationship statustranslated text"translated text"
```

**translated textmusttranslated text, translated text**. translated text `<` `>=` `&&` translated text. 

---

### Phase 2: translated textentrytranslated text typetranslated text: 

#### translated text A: controller + disabledphaseentry(recommendedtranslated textcontent)

translated textphasecontenttranslated text 200 translated text. translated textphasetranslated text: 

```
[controllerentry] ← translated text, Order 100
 ├── readvariable
 ├── translated text
 └── translated text getwi() translated textphaseentry

[phase01entry] ← disabled, Order 98
[phase02entry] ← disabled, Order 98
[phase03entry] ← disabled, Order 98
```

controllertranslated text `@activate` translated text, phaseentrytranslated text `enabled=false`, translated text `getwi()` translated text. translated textmatchtranslated textphasecontenttranslated text AI, translated text token. 

#### translated text B: translated textentrytranslated text if/else translated text(translated textcontent)

translated textcontenttranslated textentrytranslated text, translated text `<%_ _%>` translated text: 

```
translated textentry, Order 99
 ├── variablereadtranslated text
 ├── Phase 1translated textTiptranslated text(if translated text)
 ├── Phase 2translated textTiptranslated text(else if translated text)
 ├── Phase 3translated textTiptranslated text(else translated text)
 └── translated textTiptranslated text(if translated text, translated text)
```

#### translated text

| translated text | scenario |
|--------|------|
| `@activate` | controllerentry: translated text |
| `@preprocessing` | translated text: translated textentry |
| `@private` | translated text, translated textvariabletranslated text |
| `@iframe` | HTML status bar: translated text |
| `@if translated text` | translated text: translated textentry |
| `@render_after` | translated text(translated text AI) |
| `@generate_before` | translated textTiptranslated text |

---

### Phase 3: write EJS code

translated textorderwritecodetranslated text. 

#### steps 1: translated textvariablereadtranslated text

entrytranslated text, readtranslated textphasetranslated textvariable: 

```javascript
<%_
if (typeof gw === 'undefined') var gw = getvar('stat_data.Character name.Affinity', { defaults: 0 });
if (typeof rel === 'undefined') var rel = getvar('stat_data.Character name.relationship status', { defaults: 'translated text' });
if (typeof trust === 'undefined') var trust = getvar('stat_data.Character name.translated text', { defaults: 0 });
_%>
```

**hard rulestranslated text: **

1. musttranslated text `typeof` translated text. translated textentrytranslated textusagetranslated textvariable
2. musttranslated text `var` translated text. translated text `const` / `let`
3. pathmusttranslated text `stat_data` prefix, translated textneed `[0]` translated text

#### steps 2: translated text

**translated text: if / else if / else**

```javascript
<%_ if (gw < 150) { _%>
translated text AI translated textdescription
<%_ } else if (gw < 400) { _%>
translated text AI translated textdescription
<%_ } else if (gw < 700) { _%>
translated text AI translated textdescription
<%_ } else { _%>
translated text AI translated textdescription
<%_ } _%>
```

**translated textvariabletranslated text: **

```javascript
<%_ if (gw >= 400 && trust >= 30 && rel !== 'translated text') { _%>
translated text + translated text + translated text → translated text
<%_ } _%>

<%_ if (rel === 'translated text') { _%>
relationshipconfirmtranslated text → translated textcontent
<%_ } _%>
```

**translated text(translated text): **

```javascript
<%_ if (rel !== 'translated text') { _%>
 <%_ if (gw < 400) { _%>
 translated text + translated text → translated text
 <%_ } else { _%>
 translated text + translated text → translated text
 <%_ } _%>
<%_ } else { _%>
translated text → translated text
<%_ } _%>
```

#### steps 3: translated text getwi() translated textphaseentry(translated text A translated text)

controllertranslated text: 

```javascript
<%_
if (typeof gw === 'undefined') var gw = getvar('stat_data.Character name.Affinity', { defaults: 0 });
if (typeof rel === 'undefined') var rel = getvar('stat_data.Character name.relationship status', { defaults: 'translated text' });
_%>

<%_ if (gw < 150) { _%>
<%- await getwi('Character name_phase01_translated text') %>
<%_ } else if (gw < 400) { _%>
<%- await getwi('Character name_phase02_translated text') %>
<%_ } else if (rel === 'translated text') { _%>
<%- await getwi('Character name_phase04_translated text') %>
<%- await getwi('Character name_translated textcontent') %>
<%_ } else { _%>
<%- await getwi('Character name_phase03_translated text') %>
<%_ } _%>
```

**getwi() hard rules: **
- musttranslated text `await`: `<%- await getwi('entrytranslated text') %>`
- translated text: `<%_ print(await getwi('entrytranslated text')); _%>`
- translated text: `await getwi('entrytranslated text', { key: value })`
- phaseentrymusttranslated textdisabledstatus(`enabled=false`), translated text

#### steps 4: translated textcontent

translated textneedtranslated textcontenttranslated text `if` translated text: 

```
translated textdescription, translated textphasetranslated text
```

#### steps 5: translated text print() translated textcodetranslated text(optional)

translated textcontentalltranslated text, translated text `print()` translated text `<%_ _%>`: 

```javascript
<%_
if (gw < 150) {
 print('translated textphase: translated text. charactertranslated text, translated text. ');
} else if (gw < 400) {
 print('translated textphase: translated text. charactertranslated text. ');
} else {
 print('translated textphase: translated text. charactertranslated text. ');
}
_%>
```

---

### Phase 4: configurationtranslated text

#### entryconfigurationtranslated text

| entrycharacter | translated text | Order | status | recursion |
|---------|----------|-------|------|------|
| controller(translated text getwi) | `@activate` translated text | 100 | enabled=true | anti-recursion |
| phaseentry(translated text getwi translated text) | disabled | 98–800 | enabled=false | anti-recursion |
| translated textentry if/else translated text | translated text | 99 | enabled=true | anti-recursion |
| @preprocessing translated text | `@preprocessing` translated text | 100 | enabled=true | anti-recursion |
| translated textentry | translated text | translated text | enabled=true | anti-recursion |
| @iframe status bar | `@render_after` translated text | translated text | enabled=true | anti-recursion |

#### translated text

inputtranslated text"enabled/disabledTiptranslated text"translated text: 

- **translated textphase**: translated text → AI translated text EJS code(translated textcorrect)
- **translated text/translated textphase**: translated text → AI translated text(translated text `<%= getvar(...) %>`)

#### translated text

```javascript
<%_ console.info('translated textAffinity:', gw); _%> // F12 Console translated text
<%_ toastr.info('translated textPhase 2'); _%> // translated text
<%_ debugger; _%> // F12 translated text, translated textvariable
```

translated textinputtranslated text → Tiptranslated text, translated text EJS translated text AI translated textcompletecontent. 

---

## detailed specification

### translated texttypetranslated text

| translated text | translated text | output | description |
|------|------|------|------|
| `<%_ _%>` | ✅ | ❌ | translated textcode, translated text(recommended) |
| `<%= %>` | ❌ | ✅ translated text | outputvariabletranslated text, HTML translated text |
| `<%- %>` | ❌ | ✅ translated text | outputtranslated text, translated text(getwi translated text) |
| `<%# %>` | ❌ | ❌ | translated text, translated text |

### variablereadtranslated textrules

```javascript
/* readtranslated text, translated textdefault value */
getvar('stat_data.Character name.Affinity', { defaults: 0 })

/* translated textvariabletranslated text */
getvar('stat_data.Character name.Affinity') !== undefined

/* translated textmusttranslated text === */
getvar('stat_data.translated text') === 'translated text'

/* translated text !== */
getvar('stat_data.relationship status') !== 'translated text'

/* translated text */
getvar('stat_data.translated text', { defaults: '' }).includes('10translated text25translated text')
```

### contenttranslated textprefix

translated textentry**translated text(comment)**translated textprefix, translated textcontenttranslated textposition: 

| prefix | translated textposition |
|------|---------|
| `[GENERATE:BEFORE]` | translated text AI translated textTiptranslated text |
| `[GENERATE:AFTER]` | translated text AI translated textTiptranslated text |
| `[RENDER:BEFORE]` | translated text(translated text AI) |
| `[RENDER:AFTER]` | translated text(translated text AI) |

### @preprocessing translated text entrycontenttranslated textsource, translated textentry: 

```javascript
@preprocessing
<%_
if (typeof evt === 'undefined') var evt = getvar('stat_data.translated text.translated text', { defaults: '' });
_%>

<%_ if (evt === 'translated text') { _%>
translated text <%_ } else if (evt === 'translated text') { _%>
translated text <%_ } _%>
```

translated textentrycontenttranslated text, translated textentry. translated text SillyTavern 1.13.4+. 

Note: `@preprocessing` translated text `@generate_before` / `@generate_after` translated textusage. 

### @iframe translated textstatus bar

```javascript
@render_after
@iframe
@if !is_user && !is_system
<html>
<head></head>
<body>
<div>
Affinity: <%- variables.stat_data.Character name.Affinity %>
</div>
</body>
</html>
```

translated textcharactertranslated text HTML, translated text. `@iframe` translated text. 

### @@if translated text , do not writecomplete `<%_ _%>` translated text: 

```
@if variables.stat_data.Character name.Affinity >= 90
charactertranslated text
```

```
@if variables.stat_data.Character name.Affinity > 50 && variables.stat_data.Character name.Affinity < 90
charactertranslated text
```

### translated textphasetranslated text EJS translated text phasetranslated text EJS entrytranslated textcompletetranslated text: 

```
<%_
if (typeof gw === 'undefined') var gw = getvar('stat_data.Character name.Affinity', { defaults: 0 });
if (typeof rel === 'undefined') var rel = getvar('stat_data.Character name.relationship status', { defaults: 'translated text' });
_%>

personalitytranslated text: translated textpersonalitytranslated text, translated textpersonalitytranslated text

<%_ if (gw < 150) { _%>
translated text: translated text : translated text
personalitytranslated text: translated text
<%_ } else if (gw < 400) { _%>
translated text: translated text : translated text
personalitytranslated text: translated text
<%_ } else { _%>
translated text: translated text : translated text
personalitytranslated text: translated text
<%_ } _%>

<%_ if (gw < 150) { _%>
translated text: ...
translated text: ...
<%_ } _%>

<%_ if (gw >= 150 && gw < 400) { _%>
translated text: ...
translated text: ...
<%_ } _%>

<%_ if (gw >= 400 && rel !== 'translated text') { _%>
translated text: ...
translated text: ...
<%_ } _%>

<%_ if (rel === 'translated text') { _%>
translated text: ...
translated text: ...
<%_ } _%>

translated textphasetranslated text: ...(translated text)
translated textphasetranslated text: ...

translated textcharactertranslated text:

<%_ if (gw < 150) { _%>
 translated text: 
 ...
<%_ } _%>

<%_ if (gw >= 150 && gw < 400) { _%>
 translated text: 
 ...
<%_ } _%>

 translated text: (translated text if translated text)
 ...

 translated text: translated text[Character name]translated textpersonalitytranslated text...
```

entryconfiguration: translated text, position=after_char, order=99, anti-recursion. 

### translated textphasetranslated textcontrollertranslated text

```javascript
<%_
if (typeof gw === 'undefined') var gw = getvar('stat_data.Character name.Affinity', { defaults: 0 });
if (typeof rel === 'undefined') var rel = getvar('stat_data.Character name.relationship status', { defaults: 'translated text' });
if (typeof trust === 'undefined') var trust = getvar('stat_data.Character name.translated text', { defaults: 0 });
_%>

<%_ if (gw < 150) { _%>
<%- await getwi('Character name_phase01_translated text') %>
<%_ } else if (gw < 400) { _%>
<%- await getwi('Character name_phase02_translated text') %>
<%_ } else if (gw < 700 && rel !== 'translated text') { _%>
<%- await getwi('Character name_phase03_translated text') %>
<%_ } else if (rel === 'translated text') { _%>
<%- await getwi('Character name_phase04_translated text') %>
<%_ } else { _%>
<%- await getwi('Character name_phase03_translated text') %>
<%_ } _%>
```

### translated textphasetranslated text

**translated text: **

```javascript
<%_ if (gw < 150) { _%> // translated text
<%_ } else if (gw < 400) { _%> // translated text
<%_ } else if (gw < 700) { _%> // translated text
<%_ } else { _%> // translated text
<%_ } _%>
```

**translated text + translated text: **

```javascript
<%_ if (gw >= 400 && trust >= 30 && rel !== 'translated text') { _%>
// translated text + translated text + translated text = translated text
<%_ } _%>
```

**translated text: **

```javascript
<%_
if (typeof date === 'undefined') var date = getvar('stat_data.translated text.translated text', { defaults: '' });
_%>
<%_ if (date.includes('12translated text24translated text') || date.includes('12translated text25translated text')) { _%>
translated textcontent
<%_ } _%>
```

---

## self-checklist

- [ ] translated textvariableusage `typeof` translated text + `var` translated text
- [ ] translated textvariablepathtranslated text `stat_data` prefix, translated text `[0]` translated text
- [ ] `<%_ _%>` formatcorrect, translated text
- [ ] `getwi()` translated text `await`
- [ ] translated text(translated textAffinitytranslated textmatchtranslated textphase)
- [ ] translated text(translated textAffinitytranslated textmatchtranslated textphase)
- [ ] translated textcontent(translated textphasetranslated textcontent)translated text `if` translated text
- [ ] translated textphasetranslated textsecondary interpretation(translated text)translated text if translated text
- [ ] controllerentry: translated text, order=100, anti-recursion
- [ ] phaseentry(translated text getwi translated text): disabledstatus, order 98–800, anti-recursion
- [ ] translated textentrytranslated text: translated text, order=99, anti-recursion
- [ ] `@preprocessing` entrytranslated text `@generate_before` / `@generate_after` translated textusage
- [ ] translated textTiptranslated textcode, translated text
- [ ] filecontenttranslated textforbidden words(narrative forbidden words/metaphor forbidden words/translated text)

---

## common error examples

### error 1: getwi translated text await

```javascript
/* ❌ error: translated text await, entrytranslated text */
<%- getwi('character_phase01') %>

/* ✅ correct */
<%- await getwi('character_phase01') %>
```

### error 2: variablepathtranslated text stat_data prefix

```javascript
/* ❌ error: translated text stat_data prefix, translated text */
const gw = getvar('character.Affinity', { defaults: 0 });

/* ✅ correct */
const gw = getvar('stat_data.character.Affinity', { defaults: 0 });
```

### error 3: usage const/let translated textvariable

```javascript
/* ❌ error: const/let translated textentrytranslated text */
const gw = getvar('stat_data.character.Affinity', { defaults: 0 });

/* ✅ correct: var + typeof translated text */
if (typeof gw === 'undefined') var gw = getvar('stat_data.character.Affinity', { defaults: 0 });
```

### error 4: translated text

```javascript
/* ❌ error: Affinity 400 translated textmatchtranslated text */
if (gw < 400) { ... }
else if (gw <= 400) { ... } // 400 translated text

/* ✅ correct: translated text < translated text >= translated text, translated text */
if (gw < 400) { ... }
else if (gw < 700) { ... } // 400 translated textphase
```

### error 5: translated text

```javascript
/* ❌ error: Affinity ≥ 400 translated text */
if (gw < 200) { ... }
else if (gw < 400) { ... }

/* ✅ correct: translated text else translated text */
if (gw < 200) { ... }
else if (gw < 400) { ... }
else { ... } // ≥ 400 translated text
```

### error 6: phaseentrytranslated text

```javascript
/* ❌ error: phaseentrytranslated text, translated textphasecontenttranslated text, translated text */
/*
entryA(controller): @activate, enabled=true → correct
entryB(phase01): @activate, enabled=true → error！translated text enabled=false
*/

/* ✅ correct: phaseentrytranslated textdisabled, translated textcontrollertranslated text getwi translated text */
```

### error 7: @preprocessing translated text

```javascript
/* ❌ error: translated text, preprocessing translated text */
@preprocessing
@generate_before
content...

/* ✅ correct: translated text @preprocessing */
@preprocessing
content...
```

### error 8: translated textcontenttranslated text if translated text

```javascript
/* ❌ error: translated texttraitstranslated textAffinitytranslated text */
<%_ if (gw >= 400) { _%>
charactertranslated text phasetranslated texttraits xxx
<%_ } _%>

/* ✅ correct: translated textcontenttranslated text if translated text */
charactertranslated text
<%_ if (gw < 400) { _%>
translated texttraits
<%_ } else { _%>
translated texttraits
<%_ } _%>
```

### error 9: translated text == rather than ===

```javascript
/* ❌ error: == translated texttypetranslated text */
getvar('stat_data.relationship status') == 'translated text'

/* ✅ correct */
getvar('stat_data.relationship status') === 'translated text'
```
