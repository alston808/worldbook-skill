# scenariorouter

> translated texttype, translated textreadtranslated text reference file. musttranslated textreadtranslated textfiletranslated texttypereadtranslated textreferencefile, translated text. 

---

## translated text: translated text **original**translated text**derivative**: 

| translated text | original | derivative |
|------|------|------|
| translated textsource | translated textoriginal text, translated text | light novel/translated textunpack/translated text |
| translated text | type 1 / 3 | type 2(translated textextracttranslated text) |
| translated text | Plan translated text | translated text |

> **translated texttypetranslated textread `references/card-generator-guide.md`, translated textscripttranslated textcompletetranslated text, config.json formattranslated text. translated text, translated textusagescript, translated textSillyTaverntranslated textWorld Book/Character Cardjsonformat**

---

## translated texttypetranslated text

### type 1: originalCharacter Card

trigger keywords: translated text, Character Card, charactertranslated text, generatecharacter, translated textcharacter, translated textcharacter

needreadtranslated text reference: 
- `references/character-card-guide.md` — Character Cardwrite(World Bookentry + greeting)
- `references/character-guide.md` — characterentrytranslated text
- `references/world-building-guide.md` — Worldviewtranslated text
- `references/world-book-guide.md` — World Bookentry conversion
- `references/config-guide.md` — configurationrules
- `references/position-guide.md` — translated textposition
- `references/card-generator-guide.md` — scriptusagetranslated text user request MVU → additional readtranslated text `references/mvu-guide.md`
translated textuser request EJS → additional readtranslated text `references/ejs-guide.md`(EJS Dependencies MVU, translated textconfirm MVU)
translated textuser request HTML beautification → additional readtranslated text `references/html-beautify-guide.md`

translated text → forbidden-word scan → translated text `references/writing-optimization-guide.md`

---

### type 2: derivativeextract → Character Card / World Book

trigger keywords: light novel, translated text, translated textCharacter Card, translated textoriginal text, translated text, translated text, extract, translated text, translated text, translated text, original text, translated text

needreadtranslated text reference: 
- `references/information-extraction-guide.md` — information extractiontranslated text(translated text, translated text)
- `references/card-generator-guide.md` — scriptusagetranslated text(translated text, generate JSON translated textmusttranslated text)
- extracttranslated text: 
 - translated textcharactertranslated text → additional read `references/character-card-guide.md` + `references/character-guide.md`
 - translated textWorldviewtranslated text → additional read `references/world-building-guide.md` + `references/world-book-guide.md`
 - translated textitem/ability → additional read `references/world-book-guide.md`(itementrytranslated text)
- `references/config-guide.md`
- `references/position-guide.md`

translated text → forbidden-word scan → translated text `references/writing-optimization-guide.md`

---

### type 3: translated textWorldviewtranslated text + World Book

trigger keywords: Worldview, translated text, rulestranslated text, translated text, translated text, factiontranslated text, geographytranslated text, translated textrules

needreadtranslated text reference: 
- `references/world-building-guide.md` — Worldviewtranslated text(translated text)
- `references/world-book-guide.md` — World Bookentry conversion(translated text)
- `references/config-guide.md`
- `references/position-guide.md`
- `references/card-generator-guide.md` — scriptusagetranslated text

---

### type 4: item / ability / equipment

trigger keywords: translated text, translated text, equipment, translated text, ability, translated text, translated text, item, translated text, translated text, translated text

needreadtranslated text reference: 
- `references/world-book-guide.md` — itementrywritetranslated text
- `references/world-building-guide.md` — itemtranslated textWorldviewbackground
- `references/config-guide.md`
- `references/position-guide.md`
- `references/card-generator-guide.md` — scriptusagetranslated text

---

### type 5: translated textextract / translated text

trigger keywords: translated text, translated text, translated text, translated text, translated text, translated text

needreadtranslated text reference: 
- `references/information-extraction-guide.md` — translated textoriginal textextracttranslated texttraits
- `references/writing-optimization-guide.md` — forbidden-word scan
- `references/config-guide.md`
- `references/position-guide.md`
- `references/card-generator-guide.md`

extracttranslated textoutputtranslated textWorld Bookentry, translated text. 

---

### type 6: story / chapterextract

trigger keywords: storytranslated text, chapter, translated textstory, extractchapter, translated textextract, translated text

needreadtranslated text reference: 
- `references/information-extraction-guide.md` — translated textchapterline number, translated textchapter
- `references/world-book-guide.md` — story/chapterentryformattranslated textconfiguration
- `references/config-guide.md`
- `references/position-guide.md`
- `references/card-generator-guide.md`

translated textWorld Bookentry, translated text, scanDepth=2. translated textmusttranslated textchapteroriginal text. 

---

### type 7: modifytranslated textWorld Book

trigger keywords: modify, update, edit, translated textentry, translated textentry, translated text

needreadtranslated text reference: 
- translated text `python scripts/query.py <World Bookpath> --brief` translated textentry
- translated textmodifytranslated textcontenttype, readtranslated text reference(referencetype 1-4)
- `references/config-guide.md`

---

### type 8: MVU ZOD variable system

trigger keywords: MVU, ZOD, variable, Affinitytranslated text, translated text

needreadtranslated text reference: 
- `references/mvu-guide.md`
- `references/config-guide.md`
- `references/position-guide.md`

---

### type 9: EJS dynamic content

trigger keywords: EJS, dynamic content, translated textphase, translated text, translated text

needreadtranslated text reference: 
- `references/ejs-guide.md`
- `references/mvu-guide.md` — EJS musttranslated text MVU translated text
- `references/config-guide.md`
- `references/position-guide.md`

---

### type 10: HTML front-end beautification

trigger keywords: beautification, HTML, translated text, status bar, translated text, UI, translated text

needreadtranslated text reference: 
- `references/html-beautify-guide.md`
- translated text MVU status bar → additional read `references/mvu-guide.md`

---

### type 11: forbidden-word scan / translated text

trigger keywords: self-check, translated textforbidden words, translated text, translated text, translated text

needreadtranslated text reference: 
- `references/writing-optimization-guide.md`

---

## translated text

```
translated textinput → translated textoriginal/derivative
 ├─ original → Character Card？ → type1 → character-card-guide.md → forbidden-word scan
 │ World Book？ → type3 → world-building-guide.md → world-book-guide.md
 │ translated text？ → type5 → information-extraction-guide.md
 │ chapter？ → type6 → information-extraction-guide.md → world-book-guide.md
 │
 └─ derivative → type2 → information-extraction-guide.md
 → extracttranslated text: 
 ├─ charactertranslated text → character-card-guide.md
 ├─ Worldview → world-building-guide.md → world-book-guide.md
 ├─ item → world-book-guide.md
 ├─ translated text → World Bookentry
 └─ chapter → world-book-guide.md
 → forbidden-word scan → writing-optimization-guide.md
```

---

## translated text

1. translated text reference, translated text. translated text
2. translated texttypetranslated textmusttranslated text `config-guide.md`, `position-guide.md` translated text **`card-generator-guide.md`(translated textscriptparameters, config.json format, translated textfile, translated textcorrecttranslated textscript), translated text, translated textSillyTaverntranslated textCharacter Card/World BookformatJSON**
3. derivativetranslated textmusttranslated text `information-extraction-guide.md`
4. modifytranslated text `query.py --brief` translated text, translated text
5. translated textmusttranslated text `writing-optimization-guide.md` translated textforbidden-word scan
6. MVU/EJS/HTML translated textenabled, translated text
7. EJS Dependencies MVU, translated text EJS translated textmusttranslated textconfirm MVU translated textenabled
