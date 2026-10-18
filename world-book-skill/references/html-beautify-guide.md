# HTML front-end beautificationwritetranslated text

> translated text MVU variabletranslated textwritestatus bartranslated text, translated text, translated text HTML translated textcode. outputtranslated text `replaceString` fieldtranslated textcomplete HTML translated text. 

## This document covers

>translated text HTML front-end beautificationtranslated textcodegenerate. translated textbeautificationtranslated textconfirm, CSS variabletranslated text, SVG translated text, MVU translated text, translated textscriptconfiguration, translated text/translated text/API translated text. translated textWorld Bookcontent, translated text HTML/CSS/JS codegenerate. 

---

## workflow

### Phase 1: confirmtranslated text generatecodetranslated text, musttranslated textconfirmtranslated text: 

1. **beautificationtranslated text**: translated textstatus barmark(translated text `<StatusPlaceHolderImpl/>`), translated text, translated textneed, translated text(translated text `<start>` mark)？translated text placement configuration. 
2. **Character Cardtranslated text**: translated text, translated text. translated text CSS variabletranslated text. 
3. **translated text**: status bartranslated text(translated text), translated textneedtranslated textstepstranslated text(inputtranslated text, translated text, translated text, translated textconfirmtranslated text). translated text JS translated text. 
4. **translated text**: translated textneedtranslated textWorld Bookentry？translated text AI translated text？translated text 0 translated text HTML translated text？

### Phase 2: translated text needtranslated textrules, translated text"translated text + hidden"translated text: 

| rulestranslated text | translated textfield | description |
|---------|---------|------|
| translated text(translated text) | `markdownOnly: true` | completetranslated text HTML translated text, translated text |
| hiddenoriginal text(AI translated text) | `promptOnly: true` | `replaceString: ""`, translated textmarktranslated text |

translated textrulesusagetranslated text `findRegex`, translated textmarktranslated text UI, translated text. `placement` translated textusage `[1, 2]`, translated textTiptranslated text. `runOnEdit` translated text `true` translated textedittranslated text. 

### Phase 3: generate HTML translated text

outputtranslated textcompletetranslated textinline HTML file, include `<style>` translated text `<script>` translated text. translated text(translated text, translated text, translated text)musttranslated textinlinetranslated text, translated textDependenciestranslated text URL. 

### Phase 4: configurationtranslated textscript JSON

translated text HTML translated text `replaceString` field, translated textCharacter Cardtranslated textformatoutputcompletetranslated text `regex_scripts` configuration. 

---

## detailed specification

### 3.1 CSS variabletranslated text parameterstranslated text `:root` translated text, translated textmodifytranslated textvariabletranslated textrather thantranslated text. 

#### translated textvariabletranslated textrules

usagetranslated text, rather thantranslated textdescriptiontranslated text. variabletranslated text"translated text", translated textis not"translated text". 

```css
:root {
 /* translated text */
 --bg-primary: #0f0d0a;
 --bg-card: #1a1714;
 --bg-card-hover: #231f19;
 --bg-input: #161310;

 /* translated text */
 --text-primary: #e8dcc8;
 --text-secondary: #b5a78e;
 --text-muted: #7d7264;

 /* translated text */
 --accent: #c9a84c;
 --accent-light: #e8d5a0;
 --accent-dark: #8a7230;
 --border: #3d3428;
 --shadow-accent: 0 0 30px rgba(201,168,76,0.08);
}
```

#### translated text

| translated textname | applicable scenarios | backgroundtranslated text | translated text | translated text | translated text | translated text |
|---------|---------|---------|--------|-------|--------|--------|
| translated text | translated text/translated text/translated text | `#0f0d0a` | `#1a1714` | `#e8dcc8` | `#c9a84c` | `#3d3428` |
| translated text | translated text/translated text/translated text | `#0a0a14` | `#12122a` | `#e0e0ff` | `#00f0ff` | `#2a2a4a` |
| translated text | translated text/translated text/translated text | `#0a0608` | `#1a0e12` | `#e8d0d0` | `#c94c4c` | `#3d2828` |
| translated text | translated text/translated text/translated text | `#0a0f0d` | `#141a17` | `#c8e8d0` | `#4cc98a` | `#283d34` |
| translated text | translated text/translated text/translated text | `#f5f7fa` | `#ffffff` | `#2c3e50` | `#3498db` | `#e0e6ed` |

#### translated text

usage `clamp(translated text, translated text, translated text)` translated text, translated text. translated text 2% translated text 6% translated text, translated text. 

```css
--fs-xs: clamp(10px, 2vw, 11px);
--fs-sm: clamp(11px, 2.2vw, 12px);
--fs-base: clamp(12px, 2.5vw, 14px);
--fs-md: clamp(13px, 2.8vw, 15px);
--fs-lg: clamp(15px, 3.2vw, 18px);
--fs-xl: clamp(18px, 4vw, 22px);
--fs-2xl: clamp(22px, 5vw, 26px);
--fs-3xl: clamp(26px, 6vw, 32px);
```

#### translated text usagetranslated text clamp, translated text. 

```css
--space-xs: clamp(4px, 1vw, 8px);
--space-sm: clamp(8px, 2vw, 12px);
--space-md: clamp(12px, 3vw, 16px);
--space-lg: clamp(16px, 4vw, 24px);
--space-xl: clamp(20px, 5vw, 32px);
--space-2xl: clamp(24px, 6vw, 40px);
```

#### translated text(translated text)

translated text `env()` translated text, translated text, translated text. translated textvariabletranslated text `0px` translated textdefault value. 

```css
--safe-top: env(safe-area-inset-top, 0px);
--safe-bottom: env(safe-area-inset-bottom, 0px);
--safe-left: env(safe-area-inset-left, 0px);
--safe-right: env(safe-area-inset-right, 0px);
```

### 3.2 translated text

#### translated text

```css
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
html {
 -webkit-text-size-adjust: 100%;
 -webkit-tap-highlight-color: transparent;
}
body {
 background: var(--bg-primary);
 color: var(--text-primary);
 font-family: 'Noto Serif SC', 'Source Han Serif SC', 'SimSun', serif;
 min-height: 100vh;
 min-height: 100dvh;
 display: flex;
 justify-content: center;
 line-height: 1.6;
 overflow-x: hidden;
}
.container {
 position: relative;
 width: 100%;
 max-width: 640px;
 min-height: 100vh;
 min-height: 100dvh;
}
```

#### translated text : 

```css
/* translated text(translated text, translated text360px) */
@media (max-width: 360px) {
 .card-row { grid-template-columns: 1fr 1fr; gap: var(--space-xs); }
 .btn { padding: 10px 20px; }
}

/* translated text(translated text480px, translated text) */
@media (max-height: 480px) and (orientation: landscape) {
 .page { justify-content: flex-start; padding-top: var(--space-md); }
 .page-inner { gap: var(--space-sm); }
 .decorative-svg { display: none; }
 .separator { display: none; }
}

/* translated text(768px translated text) */
@media (min-width: 768px) {
 /* translated text, translated text */
}

/* translated text(1024px translated text) */
@media (min-width: 1024px) {
 .container { max-width: 680px; }
}

/* translated text */
@media (prefers-reduced-motion: reduce) {
 .animated-el { animation: none !important; }
}
```

### 3.3 translated text , translated text: 

1. **translated textusage emoji translated text**: translated text `content: "&#x2764;"` translated text `&#x1F499;` translated text Unicode translated text. translated text, musttranslated textinline SVG translated text. 
2. **translated textusage `vh` translated text**: translated text iframe translated text `vh` translated text(translated textrather than iframe translated text). translated textusage `dvh` translated text. 
3. **translated text**: `@import url('https://fonts.googleapis.com/...')` translated text `<link rel="stylesheet">` translated text, translated text. translated textlist(font-family translated text)musttranslated text. 
4. **translated text**: `background-image: url(...)` translated text `<img src="...">` translated text. translated text CSS translated text, inline SVG translated text. 
5. **translated text `position: absolute` translated text**: translated text. translated text absolute translated text, translated textcontenttranslated textmusttranslated text flex translated text grid. 
6. **translated text `let` / `const` translated text**: translated text WebView, translated textsupport ES6. translated textvariabletranslated textusage `var`, translated textusage `function` translated text. 

### 3.4 translated textbeautificationtranslated textrules

translated textbeautificationtranslated text `(.*)<StatusPlaceHolderImpl/>` translated text AI translated text HTML translated text. translated textrulestranslated text. 

#### rules 1: translated textmusttranslated text

AI translated text markdown translated text, translated text `<br>` translated textrather than `<p>` translated text. translated text CSS translated text `p` translated text, `<br>` translated text. translated text: translated text `white-space` translated text `line-height`, translated text `<p>` translated text, translated text. 

```css
.global-chat-wrapper {
 white-space: pre-wrap;
 word-wrap: break-word;
 line-height: 1.8;
}
.global-chat-wrapper p {
 margin: 0 0 12px 0;
}
```

`white-space: pre-wrap` translated text. `line-height` translated text, translated textDependencies `<p>` translated text. 

#### rules 2: translated textmusttranslated text `<StatusPlaceHolderImpl/>`

translated textbeautificationtranslated text findRegex translated text `$1` translated text, replaceString translated textmusttranslated text `<StatusPlaceHolderImpl/>`, translated textstatus bartranslated text. 

```
# correct: $1 translated text
findRegex: /(.*)<StatusPlaceHolderImpl\/>/gs
replaceString: <style>...</style><div class="wrapper">$1<StatusPlaceHolderImpl/></div>

# error: translated text
findRegex: /(.*)<StatusPlaceHolderImpl\/>/gs
replaceString: <style>...</style><div class="wrapper">$1</div>
```

#### rules 3: status bar CSS translated textmusttranslated text

status bar HTML translated text `<!DOCTYPE html>` translated text, translated text iframe translated text. status bartranslated text `* { margin: 0; padding: 0 }` translated text iframe translated text, translated text. translated textbeautification CSS translated text DOM translated text, translated textrules **translated text `*`**, musttranslated text class translated text: 

```css
/* translated textbeautification: translated text class translated text */
.global-chat-wrapper, .global-chat-wrapper * {
 box-sizing: border-box;
}

/* status bar(iframe translated text): translated text, translated text */
body { margin: 0; padding: 0; }
```

#### rules 4: status barvariabletranslated text iframe translated text, JS translated text `getAllVariables()` pathtranslated text. status bartranslated text MVU variabletranslated textusagetranslated text `{{format_message_variable::stat_data.path}}` translated text HTML, rather thantranslated text JS translated text `getAllVariables() + _.get()` read. translated text, translated text iframe translated text. 

```html
<!-- translated text: translated text -->
<span>{{format_message_variable::stat_data.Character name.Affinity}}</span>

<!-- translated text: translated textneedtranslated text JS + eventOn translated text -->
```

### 3.5 translated text

#### inline SVG translated text `<svg>` translated text HTML. translated textwritetranslated text JS translated text, translated textgenerate SVG translated text, translated text HTML translated text `<svg>` translated text. 

```javascript
function makeIcon(pathData, vb) {
 vb = vb || '0 0 24 24';
 return '<svg viewBox="' + vb + '" fill="none" stroke="currentColor" ' +
 'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" ' +
 'style="width:32px;height:32px;color:var(--accent);opacity:0.8;">' +
 pathData + '</svg>';
}
```

#### translated text SVG(translated text)

translated text SVG translated text, translated text: 
- translated text → translated text(translated text)
- translated text → translated text
- translated text → translated text
- translated text → translated text
- translated text → translated text SVG translated textusage clamp translated text, translated texthiddentranslated text. 

#### translated text usagetranslated text, translated text SVG translated text: 

```html
<svg class="separator" viewBox="0 0 400 20" aria-hidden="true">
 <line x1="60" y1="10" x2="180" y2="10" stroke="var(--accent)" stroke-width="0.5" opacity="0.3"/>
 <circle cx="200" cy="10" r="2" fill="none" stroke="var(--accent)" stroke-width="0.5" opacity="0.4"/>
 <line x1="220" y1="10" x2="340" y2="10" stroke="var(--accent)" stroke-width="0.5" opacity="0.3"/>
</svg>
```

### 3.6 translated textscriptconfigurationtranslated text

#### translated text status bartranslated text, completetranslated textconfigurationtranslated text: 

```json
{
 "id": "uuid-v4-xxxx-001",
 "scriptName": "[UI]status bartranslated text",
 "findRegex": "/<StatusPlaceHolderImpl\\/>/g",
 "replaceString": "<!DOCTYPE html>\n<html lang=\"zh-CN\">\n...completeHTML...\n</html>",
 "trimStrings": [],
 "placement": [1, 2],
 "disabled": false,
 "markdownOnly": true,
 "promptOnly": false,
 "runOnEdit": true,
 "substituteRegex": 0,
 "minDepth": null,
 "maxDepth": null
}
```

```json
{
 "id": "uuid-v4-xxxx-002",
 "scriptName": "[UI]status barhidden(AI)",
 "findRegex": "/<StatusPlaceHolderImpl\\/>/g",
 "replaceString": "",
 "trimStrings": [],
 "placement": [1, 2],
 "disabled": false,
 "markdownOnly": false,
 "promptOnly": true,
 "runOnEdit": true,
 "substituteRegex": 0,
 "minDepth": null,
 "maxDepth": null
}
```

#### fielddescription

| field | display rules | prompt rules | description |
|------|-------------|-------------|------|
| `markdownOnly` | `true` | `false` | marktranslated text |
| `promptOnly` | `false` | `true` | marktranslated textTiptranslated text |
| `placement` | `[1, 2]` | `[1, 2]` | translated textrulesusagetranslated text |
| `runOnEdit` | `true` | `true` | edittranslated text |
| `replaceString` | complete HTML | `""` translated text | translated text UI, translated text |
| `findRegex` | translated text | translated text | translated textmark |

#### findRegex translated textrules

translated text slash translated text(`/pattern/flags`). translated textinclude `/` translated text, musttranslated text `\/`. translated text XML translated text: 

```
/<StatusPlaceHolderImpl\/>/g
```

### 3.7 MVU variabletranslated text . MVU translated text MvuData translated text `initialized_lorebooks` translated textfield. translated text `stat_data` translated text payload translated text, translated textfield, translated text MVU translated textvariable, translated textalltranslated text. 

**translated text: **

1. readcompletetranslated text
2. translated text `stat_data` translated text
3. translated textcompletetranslated text

```javascript
// === correcttranslated text ===
var fullData = Mvu.getMvuData({ type: 'message', message_id: 0 }) || {};
fullData.stat_data = myStatData;
await Mvu.replaceMvuData(fullData, { type: 'message', message_id: 0 });

// === errortranslated text(translated text) ===
var payload = { stat_data: myStatData };
await Mvu.replaceMvuData(payload, { type: 'message', message_id: 0 });
```

translated textneedtranslated textcompletetranslated text: 

```javascript
await createChatMessages([{
 role: 'user',
 message: openingText,
 data: fullData
}]);
```

### 3.8 translated text HTML translated text

| translated text | replaceString | translated text | description |
|------|--------------|---------|------|
| inline HTML | complete `<!DOCTYPE html>...` | status bartranslated text, translated text | translated text, translated text CSS/JS translated text |
| translated text CDN | `<script>$('body').load('https://cdn.example.com/ui.html')</script>` | translated text UI | HTML translated textCharacter Cardtranslated text, translated textDependencies CDN translated text |
| translated text | `""` | translated text AI hiddenmark | translated textcontent, translated text |
| translated text | `<details><summary>translated text</summary>$1</details>` | variableChangelog | translated text, defaulttranslated text |

**translated text: **
- status bar → inline HTML(translated text, translated text)
- translated text → inline HTML(need JS translated text, translated texthidden)
- translated text AI hiddentranslated textrules → translated text
- translated text / variabletranslated text → translated text

### 3.9 translated text(translated text)

translated textincludetranslated textsteps(translated text, translated text, translated text), usagetranslated text. translated text, translated text class translated text. 

```javascript
var currentPage = 0;
var TOTAL_PAGES = 8;

function goToPage(n) {
 if (n < 0 || n >= TOTAL_PAGES) return;
 var allPages = document.querySelectorAll('.page');
 for (var i = 0; i < allPages.length; i++) {
 allPages[i].classList.remove('active');
 }
 currentPage = n;
 var target = document.getElementById('page-' + n);
 if (target) target.classList.add('active');
 window.scrollTo(0, 0);
 document.documentElement.scrollTop = 0;
 document.body.scrollTop = 0;
 refreshStepDots();
 if (n === TOTAL_PAGES - 1) renderSummary();
}
```

#### stepstranslated text position: 

```css
.step-indicator {
 position: fixed;
 bottom: calc(var(--space-md) + var(--safe-bottom));
 left: 50%;
 transform: translateX(-50%);
 display: flex;
 gap: clamp(4px, 1vw, 8px);
 z-index: 10;
 padding: 4px 8px;
 border-radius: 12px;
 background: rgba(15,13,10,0.8);
 backdrop-filter: blur(4px);
 -webkit-backdrop-filter: blur(4px);
}
.step-dot {
 width: clamp(5px, 1.2vw, 7px);
 height: clamp(5px, 1.2vw, 7px);
 border-radius: 50%;
 background: var(--border);
 transition: background 0.3s, box-shadow 0.3s;
}
.step-dot.active { background: var(--accent); box-shadow: 0 0 8px rgba(201,168,76,0.4); }
.step-dot.done { background: var(--accent-dark); }
```

### 3.10 translated text musttranslated text: 
- `min-height: 44px`(translated text)
- `touch-action: manipulation`(disabledtranslated text, translated text 300ms translated text)

translated text: 

```css
.scroll-area {
 overflow-y: auto;
 -webkit-overflow-scrolling: touch;
 overscroll-behavior: contain;
 max-height: 60vh;
 max-height: 60dvh;
}
```

### 3.11 translated textconfirmtranslated text

```javascript
function onConfirm() {
 var btn = document.getElementById('btn-confirm');
 btn.disabled = true;
 btn.textContent = 'translated text...';

 if (typeof getCharWorldbookNames === 'undefined') {
 alert('translated text');
 btn.disabled = false;
 btn.textContent = 'confirm';
 return;
 }

 var charWB = getCharWorldbookNames('current');
 var wbName = charWB.primary;
 if (!wbName) {
 alert('translated textWorld Book');
 btn.disabled = false;
 btn.textContent = 'confirm';
 return;
 }

 var statData = buildStatData();
 var existingData = Mvu.getMvuData({ type: 'message', message_id: 0 }) || {};
 existingData.stat_data = statData;

 createChatMessages([{
 role: 'user',
 message: openingText,
 data: existingData
 }], { refresh: 'all' }).then(function() {
 return Mvu.replaceMvuData(existingData, { type: 'message', message_id: 0 });
 }).then(function() {
 btn.textContent = 'translated text';
 btn.style.borderColor = '#10b981';
 btn.style.color = '#10b981';
 setChatMessages([{
 message_id: 0,
 message: 'translated text'
 }], { refresh: 'affected' });
 }).catch(function(err) {
 alert('translated text: ' + (err.message || String(err)));
 btn.disabled = false;
 btn.textContent = 'confirm';
 });
}
```

### 3.12 translated text API translated text

| API translated text | translated text |
|---------|------|
| `Mvu.getMvuData(option)` | read MVU completetranslated text(translated textfield) |
| `Mvu.replaceMvuData(data, option)` | translated text MVU translated text |
| `createChatMessages(messages, option)` | translated text |
| `setChatMessages(messages, option)` | modifytranslated textcontent |
| `getCharWorldbookNames('current')` | translated textCharacter Cardtranslated textWorld Booktranslated text |
| `deleteWorldbookEntries(wbName, filter)` | translated textWorld Bookentry |
| `createWorldbookEntries(wbName, entries)` | translated textWorld Bookentry |
| `generate({ user_input, should_stream })` | translated text AI generatetranslated text |
| `getLastMessageId()` | translated text |
| `waitGlobalInitialized('Mvu')` | translated text MVU translated text |

### 3.13 translated text HTML translated text, translated textneedtranslated text. 

#### translated text , translated text, translated text SVG, translated text, translated text. 

#### translated textinput

translated text `<input>` translated text placeholder Tip, translated text, translated textTip. 

#### translated text

Grid translated text, translated textdescriptiontranslated text. translated text(translated text, backgroundtranslated text), translated text. 

#### translated text

Flex wrap translated text, translated textoptionaltranslated text. translated text, supporttranslated text. translated textlist. 

#### translated textconfirmtranslated text , translated textlisttranslated text: translated textfieldtranslated text(translated text, translated text), translated text(translated text, translated text). translated text"translated textmodify"translated text"confirmtranslated text"translated text. 

### 3.14 translated text iframe translated text, usagetranslated text: 

```javascript
document.addEventListener('DOMContentLoaded', init);
if (document.readyState !== 'loading') init();
```

### 3.15 outputformattranslated text

outputmusttranslated textcomplete HTML codetranslated text, marktranslated text `html`. codetranslated text: 

```
/* === translated textvariable === */
/* === translated text === */
/* === translated text === */
/* === translated text === */
// === translated textstatus ===
// === translated text ===
// === translated text ===
// === translated textconfirm ===
// === translated text ===
```

---

## self-checklist

generatecodetranslated text, translated text 10 translated text: 

1. [ ] CSS variabletranslated textinclude: 5 translated textvariable, 8 translated text(xs translated text 3xl), 6 translated text(xs translated text 2xl), 4 translated text safe-area variable？
2. [ ] translated text `<svg>` inlinetranslated text, translated text emoji translated text Unicode translated text？
3. [ ] translated textallusage `dvh` rather than `vh`？`min-height` translated text `vh` translated text `dvh` translated text？
4. [ ] translated text URL translated text. translated text `<link>`, translated text `@import`, translated text `url()` translated text, translated text `<img src="http...">`？
5. [ ] translated textDependencies flex / grid, translated text `position: absolute` translated text？
6. [ ] translated text JavaScript variabletranslated textusage `var` translated text, translated textusage `function` translated text, translated text `let`/`const`/`=>`？
7. [ ] MVU variabletranslated text"translated textreadcompletetranslated text → translated text stat_data → translated textcompletetranslated text"translated text？
8. [ ] translated textgeneratetranslated textconfiguration. display rules(markdownOnly: true)translated text prompt rules(promptOnly: true, replaceString: "")？
9. [ ] translated text `min-height: 44px` translated text `touch-action: manipulation`？
10. [ ] translated textalltranslated text(max-360 / max-height-480-landscape / min-768 / min-1024 / prefers-reduced-motion)？

---

## translated texterror

### error 1: translated text payload translated text

```javascript
// ❌ translated text initialized_lorebooks translated textfield
var payload = { stat_data: statData };
Mvu.replaceMvuData(payload, { type: 'message', message_id: 0 });
```

translated text: translated text `getMvuData` translated textcompletetranslated text, translated text `stat_data` translated text. 

### error 2: createChatMessages translated text data fieldtranslated text

```javascript
// ❌ translated text data translated textfield, MVU translated text
createChatMessages([{ role: 'user', message: text }]);
```

translated text: translated textcompletetranslated text `data` field. 

### error 3: translated text MVU translated textpathformat

MVU beta translated textpathmusttranslated text `[0]` translated text(translated text `stat_data.character.Affinity[0]`), translated text Zod translated textusage JSON Patch translated textpath(translated text `/character/Affinity`). translated textformattranslated textCharacter Cardtranslated text. confirmCharacter Cardusagetranslated text MVU translated textpathtranslated text. 

### error 4: translated text

```json
// ❌ translated text / translated text slash translated text
"findRegex": "/<StatusPlaceHolderImpl/>/g"

// ✅ correcttranslated text
"findRegex": "/<StatusPlaceHolderImpl\\/>/g"
```

### error 5: promptOnly rulestranslated text replaceString

hiddenrulestranslated textoriginal texttranslated text AI translated text. translated text `replaceString` is nottranslated text, translated textcontenttranslated text prompt translated text, translated text token translated text. hiddenrulestranslated textusage `"replaceString": ""`. 

### error 6: translated text reduced-motion

translated text"translated text"translated text. translated text `@media (prefers-reduced-motion: reduce)` translated textdisabledtranslated text, translated text. 

### error 7: translated text

HTML filetranslated text. translated text API(`Mvu`, `getCharWorldbookNames` translated text)translated text, musttranslated text `typeof` translated text `'undefined'`, translated textTiprather thantranslated text. 
