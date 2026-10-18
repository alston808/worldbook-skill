# MVU ZOD variable systemtranslated text

> **translated textcharacter: ** translated text MVU variable systemtranslated text, translated textcomplete MVU ZOD variabletranslated text. 
>
> **translated textdescription: ** MVU translated textvariabletranslated text, translated textDependencies EJS translated text. translated textWorld Booktranslated text, translated textTiptranslated text, EJS mustDependencies MVU(needtranslated textvariabletranslated textreadtranslated text). translated text. **MVU translated textneed EJS, translated text EJS need MVU**. 

---

## translated text

1. [translated text](#translated text)
2. [Phase 1: translated textvariabletranslated textscript](#translated textPhase 1translated textvariabletranslated textscript)
3. [Phase 2: writeWorld Bookentry](#translated textPhase 2writeWorld Bookentry)
4. [Phase 3: configurationtranslated text](#translated textPhase 3configurationtranslated text)
5. [Phase 4: translated text](#translated textPhase 4translated text)
6. [Phase 5: status bartranslated text](#translated textPhase 5status bartranslated text)
7. [translated textvariableprefix](#translated textvariableprefix)
8. [translated text](#translated text)
9. [self-checklist](#translated textself-checklist)
10. [common error examples](#translated textcommon error examples)

---

## translated text, translated text

MVU ZOD translated text SillyTavern translated textvariabletranslated textcompletetranslated text. translated textcompletetranslated text MVU Character Cardtranslated text: 

```
Character Card MVU translated text
├── variabletranslated textscript → Zod Schema(characterscript), translated textvariabletypetranslated text
├── [initvar] translated textvariable → YAML, translated textvariabletranslated text(World Bookdisabledentry)
├── variable list → translated textvariabletranslated text AI(World Booktranslated textentry D0/D1)
├── [mvu_update] updaterules → translated textvariabletranslated textmodify(World Booktranslated textentry)
├── [mvu_update] outputformat → translated text AI translated text JSON Patch formatoutputupdatetranslated text(World Booktranslated textentry)
├── translated text → hidden UpdateVariable translated text, translated text StatusPlaceHolderImpl
├── translated textscript(optional) → translated text MVU translated text, translated textvariable, translated text
└── translated text(optional) → translated text HTML status bar
```

### translated text

1. **variabletranslated textscript** translated text MVU translated textvariabletranslated text(type, translated text, default value, translated text)
2. **[initvar]** translated textvariabletranslated text
3. **variable list** translated text AI translated text
4. **variable update rules** translated text AI translated textvariabletranslated text
5. **variableoutputformat** translated text AI translated textoutputtranslated text JSON Patch translated text
6. **MVU translated text** translated text AI translated textupdatetranslated text, translated textmodify
7. **variabletranslated textscript** translated textmodifytranslated text(translated text clamp translated text)
8. **translated text** translated text `<UpdateVariable>` translated text AI translated text, translated textbeautification

---

## translated text, Phase 1: translated textvariabletranslated textscript

### 2.1 translated text codetranslated text, translated textCharacter Cardneedtranslated text: 

| translated texttype | translated textvariabletranslated text |
|---------|------------|
| translated text/translated text | Affinity, translated text, translated text, translated text, translated text |
| translated text/translated text | inventoryitem, translated text, translated textlist, translated textmark |
| translated text/translated text | translated text, translated text, characterstatustranslated text |

> variabletranslated textusage `{{user}}` translated text. translated text `protagonist` translated textnametranslated text. 

### 2.2 scripttranslated text

variabletranslated textscripttranslated text **translated textscripttranslated text → characterscript** translated text. translated text, translated text: 

```js
import { registerMvuSchema } from 'https://testingcf.jsdelivr.net/gh/StageDog/tavern_resource/dist/util/mvu_zod.js';

export const Schema = z.object({
 // translated textvariabletranslated text
});

$(() => {
 registerMvuSchema(Schema);
});
```

`z`(Zod 4)translated text `_`(Lodash)translated text, **translated text import translated text**. translated textneed import translated text `registerMvuSchema`. 

### 2.3 Zod 4 translated text

| translated text | description |
|-----|------|
| `z.string()` | translated texttype |
| `z.coerce.number()` | translated texttype(translated text, recommendedtranslated textusage) |
| `z.boolean()` | translated texttype(translated text `z.coerce.boolean()`) |
| `z.literal('translated text')` | translated text |
| `z.enum(['A','B','C'])` | translated text, translated textlisttranslated text |
| `z.object({...})` | translated textfieldtranslated text(translated textfiletranslated text) |
| `z.record(translated textSchema, translated textSchema)` | translated text(translated textitemtranslated text, translated text, translated text) |
| `z.partialRecord(translated text, translated text)` | translated text record translated textoptional, translated text |
| `.describe('description')` | translated textfieldtranslated textdescription, AI translated textread |
| `.prefault(default value)` | fieldtranslated text(MVU translated text, translated text `.default()`) |
| `.transform(v => ...)` | translated text/translated text, translated textparameters |
| `.transform(v => _.clamp(v, 0, 100))` | translated text |
| `.transform(data => _.pickBy(data, fn))` | translated text |

### 2.4 writetranslated text

1. **translated text transform translated text, translated text min/max: ** `z.coerce.number().transform(v => _.clamp(v, 0, 100))` translated textrather thantranslated text. 
2. **translated text prefault rather than default: ** MVU translated textrecommended `.prefault()`. 
3. **translated text: ** `z.record()` translated text `z.array()` translated textupdatetranslated text. 
4. **translated text: ** translated text `Schema.parse()` translated textmusttranslated text. 
5. **translated text `.strict()` translated text `.passthrough()`: ** MVU Zod 4 translated textsupporttranslated text. 
6. **transform translated textparameters: ** `(value) => ...` correct, `(value, ctx) => ...` translated text. 
7. **translated text `.prefault({})` translated text, translated textfieldtranslated textmusttranslated text `.prefault()`. **

### 2.5 completeexample

```js
import { registerMvuSchema } from 'https://testingcf.jsdelivr.net/gh/StageDog/tavern_resource/dist/util/mvu_zod.js';

export const Schema = z.object({
 translated text: z.object({
 translated text: z.string(),
 translated text: z.string(),
 translated text: z.record(z.string().describe('translated text'), z.string().describe('translated text')),
 }),

 Asuna: z
 .object({
 Affinity: z.coerce.number().transform(v => _.clamp(v, 0, 100)),
 translated text: z.record(
 z.enum(['translated text', 'translated text', 'translated text', 'translated text', 'translated text', 'translated text']),
 z.string().describe('translated textdescription'),
 ),
 translated text: z.record(
 z.string().describe('translated text'),
 z.object({
 translated text: z.string(),
 translated text: z.string().prefault('translated text'),
 }),
 ).transform(data => {
 // Affinitytranslated text, translated text
 const maxSlots = Math.ceil(_.get(data, '__Affinity__', 0) / 10);
 return _(data).entries().takeRight(maxSlots).fromPairs().value();
 }),
 })
 .transform(data => {
 // translated text transform translated textAffinitytranslated text(Dependencies Schema translated textordertranslated textNote, 
 // translated textquantitytranslated textscripttranslated text VARIABLE_UPDATE_ENDED)
 return data;
 }),

 protagonist: z.object({
 inventory: z.record(
 z.string().describe('itemtranslated text'),
 z.object({
 description: z.string(),
 quantity: z.coerce.number().prefault(1),
 }),
 ).transform(data => _.pickBy(data, ({ quantity }) => quantity > 0)),
 }),
});

$(() => {
 registerMvuSchema(Schema);
});
```

translated textexampletranslated text: translated text, translated text, translated text, inventorytranslated textquantitytranslated textitem. 

### 2.6 translated textvalidate

- **translated textposition: ** translated textscripttranslated text → characterscript, translated text `variabletranslated text`
- **validatetranslated text: ** translated text, translated text `translated textinputtranslated text → translated text` translated text `[script|variabletranslated text]: variabletranslated text`

translated texterrorTip, translated text `[script|variabletranslated text]` translated textalltranslated textentrytranslated textissues. 

---

## translated text, Phase 2: writeWorld Bookentry

### 3.1 [initvar] translated textvariableentry

**content(YAML format, translated textvariabletranslated text): **

```yaml
translated text:
 translated text: 2024-04-08 10:45
 translated text: translated text 2translated textAtranslated text :
 translated text: Asunatranslated text, needtranslated text, translated text
Asuna:
 Affinity: 35
 translated text:
 translated text: translated text : translated text : translated text : translated text : translated text : translated text :
 translated text:
 translated text: translated text : translated text
protagonist:
 inventory:
 translated text:
 description: translated text, translated text
 quantity: 1
```

**World Bookconfiguration: **

| configuration items | translated text |
|-------|----|
| entrytranslated text | `[initvar]variabletranslated text` |
| status | **disabled**(musttranslated text disabled) |
| position | D translated text @D, depth=4 |
| order | 200 |
| translated text | translated text(constant=true) |

> MVU translated textreaddisabledstatustranslated text `[initvar]` entry. translated textenabledtranslated text, translated textTiptranslated text AI, translated text. 

### 3.2 variable listentry

**content(translated text, translated textusage): **

```yaml
---
<status_current_variable>
{{format_message_variable::stat_data}}
</status_current_variable>
```

`{{format_message_variable::stat_data}}` translated text, translated textvariabletranslated text YAML formattranslated text, AI translated textstatus. 

**translated text. translated text: **

```yaml
---
<status_current_variable>
translated text:
 {{format_message_variable::stat_data.translated text}}
Asuna:
 Affinity: {{format_message_variable::stat_data.Asuna.Affinity}}
 translated text:
 {{format_message_variable::stat_data.Asuna.translated text}}
protagonist:
 {{format_message_variable::stat_data.protagonist}}
</status_current_variable>
```

**World Bookconfiguration: **

| configuration items | translated text |
|-------|----|
| entrytranslated text | `variable list`(**translated text**translated text `[mvu_update]` prefix) |
| status | enabled |
| position | D translated text @D, depth=0 translated text 1 |
| order | 200 |
| translated text | translated text |

> **translated textmusttranslated text D0 translated text D1？** variable listtranslated text, musttranslated text AI translated text. translated text D2 translated text, translated texthistorytranslated text, AI translated text. 

### 3.3 [mvu_update] variable update rules

**contenttranslated text: **

```yaml
---
variable update rules:
 translated text:
 translated text:
 format: YYYYtranslated textMMtranslated textDDtranslated text X HH:MM
 translated text:
 type: |-
 {
 [translated text: string]: string; // translated textdescription
 }
 check:
 - translated textneedtranslated text, translated text, translated text
 - translated textlisttranslated text, addedtranslated text
 - translated text 5~8 translated text
 Asuna:
 Affinity:
 type: number
 range: 0~100
 check:
 - translated textAsunatranslated textprotagonisttranslated text ±(3~6)
 - translated text 5~8, translated text 5~10
 - translated textAsunatranslated textprotagonisttranslated textupdate
 translated text.${translated text|translated text|translated text|translated text|translated text|translated text}:
 check:
 - translated text, translated text, translated textupdate
 - descriptiontranslated textincludetranslated text, translated text, translated text :
 type: |-
 {
 [translated text: string]: {
 translated text: string;
 translated text?: string; // default 'translated text'
 }
 }
 check:
 - translated text, translated text
 - translated textstatustranslated textphasetranslated texttraits
 - translated textAffinity: Math.ceil(Affinity/10) translated text
 protagonist:
 inventory:
 type: |-
 {
 [itemtranslated text: string]: {
 description: string;
 quantity?: number; // default 1
 }
 }
 check:
 - translated text, translated text, translated textitemtranslated textupdate
 - quantitytranslated textentrytranslated text
```

**translated textfieldtranslated text: **

| field | translated text | translated text |
|-----|------|---------|
| `type` | variabletranslated texttypetranslated text, translated text `number`, TypeScript typetranslated text | translated textvariabletranslated text(translated text `translated text`) |
| `range` | translated text | translated textvariabledo not write |
| `format` | translated textformattranslated text | translated textformattranslated textdo not write |
| `check` | updatetranslated text. translated textfield, AI translated textupdate | translated text |

**writetranslated text: **
- translated textvariabledo not writetranslated textrules(translated text `translated text` translated textdescriptiontranslated textupdate)
- translated textvariabletranslated text(translated text `translated text.${translated text|translated text|translated text|...}` translated textrulestranslated text)
- translated text `_` translated textvariabletranslated textupdaterules
- translated text(translated text `translated text`)translated text `type` translated text `[translated text: string]` description
- updaterulestranslated textcharactertranslated text, translated text D0. AI outputformattranslated text"translated text"translated text

**World Bookconfiguration: **

| configuration items | translated text |
|-------|----|
| entrytranslated text | `[mvu_update]variable update rules`(**must**translated text `[mvu_update]` prefix) |
| status | enabled |
| position | D translated text @D, depth=0(translated text after_char) |
| order | 200 |
| translated text | translated text |

### 3.4 [mvu_update] variableoutputformat

**content(translated text, translated textusage): **

```yaml
---
variableoutputformat:
 rule:
 - you must output the update analysis and the actual update commands at once in the end of the next reply
 - the update commands works like the **JSON Patch (RFC 6902)** standard, must be a valid JSON array containing operation objects, but supports the following operations instead:
 - replace: replace the value of existing paths
 - delta: update the value of existing number paths by a delta value
 - insert: insert new items into an object or array (using `-` as array index intends appending to the end)
 - remove
 - move
 - don't update field names starts with `_` as they are readonly, such as `_variable`
 format: |-
 <UpdateVariable>
 <Analysis>$(IN ENGLISH, no more than 80 words)
 - ${calculate time passed: ...}
 - ${decide whether dramatic updates are allowed as it's in a special case or the time passed is more than usual: yes/no}
 - ${analyze every variable based on its corresponding `check`, according only to current reply instead of previous plots: ...}
 </Analysis>
 <JSONPatch>
 [
 { "op": "replace", "path": "${/path/to/variable}", "value": "${new_value}" },
 { "op": "delta", "path": "${/path/to/number/variable}", "value": "${positive_or_negative_delta}" },
 { "op": "insert", "path": "${/path/to/object/new_key}", "value": "${new_value}" },
 { "op": "insert", "path": "${/path/to/array/-}", "value": "${new_value}" },
 { "op": "remove", "path": "${/path/to/object/key}" },
 { "op": "remove", "path": "${/path/to/array/0}" },
 { "op": "move", "from": "${/path/to/variable}", "to": "${/path/to/another/path}" },
 ...
 ]
 </JSONPatch>
 </UpdateVariable>
```

**formattranslated text: **

translated text"translated textoutputformat"translated text. `rule` translated text AI translated textreadtranslated textoutput; `format` translated text AI translated textoutput. translated text: 
- `${description}` → AI translated textdescriptiontranslated textcontent
- `$(translated text)` → AI translated textoutputtranslated textmarktranslated text
- `...` → AI translated textoutput
- translated textcontent(translated text `<UpdateVariable>`, `<Analysis>`)translated textoutput

**Analysis translated text: **

translated textvariableupdatetranslated text. translated text AI translated textoutputtranslated text: 
1. translated text
2. translated text(translated textAffinitytranslated text 100 translated text 0)
3. translated textvariabletranslated text `check` rules, translated text**translated text**(rather thanhistorytranslated text)translated textneedupdate

translated text AI translated text"translated text"translated textupdaterules. translated textupdaterulesentrytranslated textposition. 

**JSON Patch translated text: **

| translated text | translated text | pathexample |
|-----|------|---------|
| `replace` | translated textpathtranslated textcompletetranslated text | `"/Asuna/Affinity"` |
| `delta` | translated text(translated text) | `"/Asuna/Affinity"` |
| `insert` | translated text, translated text(`-`) | `"/protagonist/inventory/translated textitem"` |
| `remove` | translated textpath | `"/protagonist/inventory/translated text"` |
| `move` | translated textpath | `from: "/A"`, `to: "/B"` |

**pathrules: ** translated text `/` translated text, translated textvariabletranslated text, **translated textneed** `stat_data` prefix. translated text `/Asuna/Affinity` rather than `/stat_data/Asuna/Affinity`. 

**AI outputexample: **

```
(translated text...)

<UpdateVariable>
<Analysis>
- Time advanced by 10 minutes (from 10:47 to 10:57).
- Special Case? No, routine plot progression.
- Asuna.Affinity: Displayed strong reaction, warranting increase.
- protagonist.inventory: Mints were placed on her desk. Should be removed.
</Analysis>
<JSONPatch>
[
 { "op": "replace", "path": "/translated text/translated text", "value": "2024-04-08 10:57" },
 { "op": "replace", "path": "/Asuna/Affinity", "value": 40 },
 { "op": "remove", "path": "/protagonist/inventory/translated text" }
]
</JSONPatch>
</UpdateVariable>
```

**World Bookconfiguration: **

| configuration items | translated text |
|-------|----|
| entrytranslated text | `[mvu_update]variableoutputformat`(**must**translated text `[mvu_update]` prefix) |
| status | enabled |
| position | D translated text @D, depth=0(Gemini)/ depth=4(Claude) |
| order | 200 |
| translated text | translated text |

### 3.5 optional: variableoutputformattranslated text AI translated textoutput `<UpdateVariable>` translated text, addedtranslated textentrytranslated text: 

```yaml
---
variableoutputformattranslated text:
 rule: The following must be inserted to the end of reply, and cannot be omitted
 format: |-
 <UpdateVariable>
 ...
 </UpdateVariable>
```

**configurationsame as above, entrytranslated text `[mvu_update]variableoutputformattranslated text`. **

---

## translated text, Phase 3: configurationtranslated text

AI translated textinclude `<UpdateVariable>` translated text, MVU translated text, translated text AI(translated text token, translated text AI translated textupdate). translated text, MVU translated text `<StatusPlaceHolderImpl/>`, translated textneedtranslated text. 

### 4.1 musttranslated text `translated text → translated text` translated text. MVP translated textneedtranslated text: 

**translated text A: hiddenvariableupdate(do not sendtranslated text AI)**

| configuration items | translated text |
|-------|----|
| scriptname | `[do not send]translated textvariableupdate` |
| findRegex | `/<UpdateVariable>[\s\S]*?<\/UpdateVariable>/gs` |
| replaceString | (translated text) |
| translated text | AI output |
| translated text | translated textformatTiptranslated text ✅ |
| minDepth | 4(optional: translated text 2~3 translated text AI reference, translated textupdate) |

**translated text B: hiddenstatus bartranslated text(do not sendtranslated text AI)**

| configuration items | translated text |
|-------|----|
| scriptname | `[do not send]translated text` |
| findRegex | `<StatusPlaceHolderImpl/>` |
| replaceString | (translated text) |
| translated text | AI output |
| translated text | translated textformatTiptranslated text ✅ |
| runOnEdit | true |

**translated text C: status barbeautification(translated text)**

| configuration items | translated text |
|-------|----|
| scriptname | `[translated text]status bar` |
| findRegex | `<StatusPlaceHolderImpl/>` |
| replaceString | (translated text HTML translated textcode—translated textPhase 5) |
| translated text | AI output |
| translated text | translated textformattranslated text ✅ |

**translated text: ** translated text B translated text AI translated text(translated text token), translated text C translated textbeautificationtranslated textstatus bar. translated text, translated text. 

translated textstatus bartranslated text, translated text findRegex translated text `<StatusPlaceHolderImpl/>`. translated text promptOnly translated text, translated text markdownOnly translated textcode. 

### 4.2 optionalbeautificationtranslated text beautificationtranslated text, translated text `<UpdateVariable>` translated text `<details>` translated text: 

```
findRegex: /<UpdateVariable>[\s\S]*?<\/UpdateVariable>/gs
replaceString: <details><summary>variableupdatetranslated text</summary>$1</details>
markdownOnly: true
```

translated text"translated textvariableupdate"translated textcharacter. translated texthiddentranslated textbeautification, translated texthiddentranslated text, beautificationtranslated text. 

---

## translated text, Phase 4: translated text Character Cardtranslated text, translated textvariabletranslated text. 

### translated text: translated text(`<initvar>` translated text)

translated text `<initvar>` translated textcomplete YAML variabletranslated text: 

```text
translated text 2 translated textstory……

<UpdateVariable>
<initvar>
translated text:
 translated text: 2025translated text4translated text7translated text 08:42
 translated text: translated text·2translated textAtranslated text
Asuna:
 Affinity: 15
 translated text:
 translated text: translated text : translated text
 ...
protagonist:
 inventory:
 translated text:
 description: translated text
 quantity: 1
</initvar>
</UpdateVariable>
```

translated text YAML codetranslated text(` ```yaml ... ``` `), translated text. 

### translated text: translated text(JSON Patch)

translated textvariable, translated text JSON Patch translated textmodify: 

```text
translated text 2 translated text……

<UpdateVariable>
<JSONPatch>
[
 { "op": "replace", "path": "/Asuna/Affinity", "value": 50 },
 { "op": "insert", "path": "/protagonist/inventory/translated text", "value": { "description": "translated text", "quantity": 1 } }
]
</JSONPatch>
</UpdateVariable>
```

### translated textrules

```
translated textinclude <initvar> translated text？
├── translated text → usage <initvar> translated textcompletetranslated text(translated text, translated textWorld Booktranslated text [initvar] translated textentry)
└── translated text → usageWorld Booktranslated textdisabledtranslated text [initvar] translated textentry
```

translated textWorld Booktranslated text `[initvar]` entry, changed totranslated text `<initvar>` translated text. translated text. 

> translated text JSON Patch translated text: translated text `[initvar]` translated textentrytranslated text, translated text Patch modify. translated textmusttranslated text `[initvar]` translated text. 

---

## translated text, Phase 5: status bartranslated text

### 6.1 translated text . translated text C translated text replaceString translated text: 

```
💖 Affinity: {{format_message_variable::stat_data.Asuna.Affinity}}
```

translated text HTML translated textbeautification: 

```html
<style>
.stat-bar {
 font-size: 14px; color: #ff69b4;
 border: 1px solid #ff69b4; border-radius: 8px;
 padding: 6px 12px; display: inline-block;
}
</style>
<div class="stat-bar">
💖 Affinity: {{format_message_variable::stat_data.Asuna.Affinity}}
</div>
```

### 6.2 translated text needtranslated text, translated text, translated textstatus bar, usage JS translated text: 

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<style>
 body { margin: 0; padding: 0; }
 .card {
 width: 320px; max-width: 100%;
 background: linear-gradient(145deg, #1a1a2e, #16213e);
 border-radius: 16px; padding: 16px; color: #e0e0e0;
 }
 .row { display: flex; justify-content: space-between; align-items: center; padding: 6px 0; }
 .bar { flex: 1; height: 6px; background: rgba(255,255,255,0.1); border-radius: 3px; margin: 0 10px; }
 .fill { height: 100%; background: linear-gradient(90deg, #ff6b9d, #c44dff); border-radius: 3px; }
</style>
<script type="module">
 function render() {
 const vars = getAllVariables();
 const aff = _.get(vars, 'stat_data.Asuna.Affinity', 0);
 const mood = _.get(vars, 'stat_data.Asuna.translated text', '--');
 $('#aff-val').text(aff);
 $('#aff-bar').css('width', aff + '%');
 $('#mood-val').text(mood);
 }

 async function init() {
 await waitGlobalInitialized('Mvu');
 render();
 eventOn(Mvu.events.VARIABLE_UPDATE_ENDED, () => render());
 }

 $(errorCatched(init));
</script>
</head>
<body>
<div class="card">
 <div class="row">
 <span>Affinity</span>
 <div class="bar"><div id="aff-bar" class="fill" style="width:0%"></div></div>
 <span id="aff-val">--</span>/100
 </div>
 <div class="row">
 <span>translated text</span><span id="mood-val">--</span>
 </div>
</div>
</body>
</html>
```

**translated textrules: **

| translated text | description |
|-----|------|
| `body { margin: 0; padding: 0; }` | musttranslated text. needtranslated text margin |
| variablepathtranslated text `stat_data.` translated text | `_.get(all_variables, 'stat_data.Asuna.Affinity')` |
| musttranslated text `getAllVariables()` | rather thantranslated text |
| musttranslated text `_.get(vars, 'path', 'default value')` | translated textread, translated textpathtranslated text |
| musttranslated text `await waitGlobalInitialized('Mvu')` | translated text MVU translated text |
| musttranslated text `$(errorCatched(init))` | translated text, translated text |
| musttranslated text `VARIABLE_UPDATE_ENDED` | variabletranslated text |

### 6.3 translated textstatus bar

translated textstatus bartranslated textrather thantranslated text, translated text C translated text findRegex changed to: 

```
findRegex: /(.*)<StatusPlaceHolderImpl\/>/s
replaceString: translated textHTML\n$1
```

translated textstatus bartranslated text. 

---

## translated text, translated textvariableprefix

MVU translated textprefixtranslated textvariabletranslated text AI translated text: 

| prefix | AI translated text | AI translated textupdate | translated text |
|-----|---------|----------|---------|
| translated textprefix | ✅ translated text | ✅ translated text | translated textvariable |
| `_` prefix | ✅ translated text | ❌ translated text | translated text, Character name, Worldviewtranslated text |
| `$` prefix | ❌ translated text | ❌ AI translated text(script/Tiptranslated text) | hiddentranslated text, translated texttypemark, scripttranslated text |

**example: **

```yaml
translated text:
 _type: translated text # AI translated textmodify
 $translated text: translated text # AI translated text, translated text EJS/scripttranslated textbranch

Asuna:
 _translated text: 09-30 # translated text
 Affinity: 35 # AI translated text
```

`$` prefixtranslated textvariabletranslated text `{{format_message_variable::stat_data}}` translated text; `_` prefixtranslated textvariabletranslated text JSON Patch pathtranslated text MVU translated textupdate. 

---

## translated text, translated text

MVU translated text. translated text**allconfigurationmusttranslated text**. 

| translated text | MVU ZOD(recommended) | MVU Beta(translated text) |
|-----|----------------|-----------------|
| translated textformat | YAML | JSON(`{"variable": [translated text, "description"]}`) |
| updatetranslated text | JSON Patch(RFC 6902) | `_.set('path[0]', translated text, translated text)` / `_.add('path[0]', delta)` |
| readtranslated text | `{{format_message_variable::stat_data.path}}` | `{{get_message_variable::stat_data}}` + `getvar("stat_data.path[0]")` |
| pathtranslated text | translated text `[0]` translated text | musttranslated text `[0]` translated text |
| EJS translated textusage | `getvar('stat_data.Asuna.Affinity')` | `getvar('stat_data.Asuna.Affinity[0]')` |
| variabletranslated text AI updatepath | `/Asuna/Affinity` | translated text `_.set` format |

> **translated text: ** translated textusage ZOD translated text. Beta translated text. 

---

## translated text, self-checklist

translated text MVU translated text, translated textordertranslated text. 

### variabletranslated textscript

- [ ] translated text `import { registerMvuSchema } from 'https://testingcf.jsdelivr.net/gh/StageDog/tavern_resource/dist/util/mvu_zod.js';` completecorrect
- [ ] translated text `$(() => { registerMvuSchema(Schema); });` completecorrect
- [ ] translated text import translated text `registerMvuSchema`, translated text import `z` translated text `_`
- [ ] translated text `.strict()`, `.passthrough()`, `.optional()`
- [ ] translated text `.transform(v => _.clamp(v, min, max))` rather than `.min()/.max()`
- [ ] default valuetranslated text `.prefault()` rather than `.default()`
- [ ] `.transform()` translated textparameters
- [ ] translated textusage `z.record()` rather than `z.array()`
- [ ] translated textusage `.prefault({})` translated text, translated textallfieldtranslated text `.prefault()`
- [ ] JavaScript translated textcorrect(translated text, translated text)
- [ ] translated text

### [initvar] translated textvariable

- [ ] entrytranslated text `[initvar]variabletranslated text`
- [ ] statustranslated text**disabled**
- [ ] contenttranslated text YAML format, translated textcorrect
- [ ] YAML translated textvariabletranslated textscripttranslated text Zod Schema translated text
- [ ] translated texttypetranslated text Zod translated text
- [ ] translated text

### variable list

- [ ] entrytranslated text `variable list`(translated text `[mvu_update]` prefix)
- [ ] depth=0 translated text 1, order=200
- [ ] contenttranslated text: `<status_current_variable>{{format_message_variable::stat_data}}</status_current_variable>`

### variable update rules

- [ ] entrytranslated text `[mvu_update]` translated text
- [ ] translated textvariabletranslated text `check` field
- [ ] translated textvariabletranslated textrules
- [ ] translated textvariabletranslated text
- [ ] `_` prefixvariabletranslated textrules
- [ ] `type` translated text Zod Schema translated text

### variableoutputformat

- [ ] entrytranslated text `[mvu_update]` translated text
- [ ] `rule` include JSON Patch translated textdescription
- [ ] `format` include `<UpdateVariable>`, `<Analysis>`, `<JSONPatch>` translated text
- [ ] pathtranslated text `stat_data` prefix

### translated text

- [ ] translated text promptOnly translated texthidden `<UpdateVariable>` translated text
- [ ] translated text promptOnly translated texthidden `<StatusPlaceHolderImpl/>`
- [ ] translated text markdownOnly translated text `<StatusPlaceHolderImpl/>` translated textcode

### translated textstatus bar(if any)

- [ ] `body { margin: 0; padding: 0; }` correct
- [ ] variablepathtranslated text `stat_data.` translated text
- [ ] usage `getAllVariables()` + `_.get()`
- [ ] include `await waitGlobalInitialized('Mvu')`
- [ ] include `$(errorCatched(init))`
- [ ] include `eventOn(Mvu.events.VARIABLE_UPDATE_ENDED, ...)` translated text

---

## translated text, common error examples

### error 1: variabletranslated textscripttranslated text import translated text z translated text _

```js
// error
import { z } from 'zod';
import _ from 'lodash';
import { registerMvuSchema } from '...';

// correct: z translated text _ translated text, translated text import registerMvuSchema
import { registerMvuSchema } from 'https://testingcf.jsdelivr.net/gh/StageDog/tavern_resource/dist/util/mvu_zod.js';
```

### error 2: variable listtranslated text D3 translated text

```
variable list depth=3 ✗
```
AI translated textlisttranslated text 3 translated textstatus, translated textupdatetranslated texterror. 

```
variable list depth=0 ✓
```

### error 3: variable listentrytranslated text [mvu_update]

```
entrytranslated text: "[mvu_update]variable list" ✗
```

translated text `[mvu_update]` prefixtranslated text MVU translated textentrytranslated text"translated text"translated textusage, translated text AI translated text. 

```
entrytranslated text: "variable list" ✓
```

### error 4: JSON Patch pathtranslated text stat_data

```json
{ "op": "replace", "path": "/stat_data/Asuna/Affinity", "value": 40 }
```
pathtranslated textvariabletranslated text. `stat_data` translated text, AI translated textneedtranslated text. 

```json
{ "op": "replace", "path": "/Asuna/Affinity", "value": 40 }
```

### error 5: translated textstatus bar body padding translated text 0

```css
body { margin: 0; padding: 10px; } /* ✗ */
```

translated text padding translated textstatus bartranslated text. 

```css
body { margin: 0; padding: 0; }
.card { margin: 8px; } /* ✓ translated text */
```

### error 6: translated text JS translated textvariablepathtranslated text stat_data

```js
_.get(all_variables, 'Asuna.Affinity', 'N/A') // ✗
```

MVU translated textvariabletranslated text `stat_data` translated text, js readtranslated textmusttranslated text. 

```js
_.get(all_variables, 'stat_data.Asuna.Affinity', 'N/A') // ✓
```

### error 7: translated text VARIABLE_UPDATE_ENDED

```js
async function init() {
 await waitGlobalInitialized('Mvu');
 render(); // translated text, variabletranslated textupdate
}
$(errorCatched(init));
```

musttranslated text, variableupdatetranslated text: 

```js
async function init() {
 await waitGlobalInitialized('Mvu');
 render();
 eventOn(Mvu.events.VARIABLE_UPDATE_ENDED, () => render()); // ✓
}
$(errorCatched(init));
```

### error 8: Zod translated text Beta translated text

```
[initvar] translated text YAML ← ZOD translated text
AI outputformattranslated text _.set() ← Beta translated text
```

translated text. translated textformat, updatetranslated text, readpathmusttranslated text. translated text ZOD. 

### error 9: [initvar] entrytranslated textdisabled

```
[initvar]entry enabled: true ✗
```

MVU translated textreaddisabledstatustranslated text `[initvar]` entrytranslated textvariabletranslated text. enabledtranslated textTiptranslated text AI, variabletranslated text. 

### error 10: translated text `_` prefixvariabletranslated textupdaterules

```yaml
variable update rules:
 translated text:
 _type: # ✗ _prefixtranslated text, AI translated textupdate
 check: ...
```

translated textvariabletranslated textneedtranslated textupdaterulestranslated text. 

---

> **translated text: ** 1.0 | **translated textupdate: ** 2026-05-16
