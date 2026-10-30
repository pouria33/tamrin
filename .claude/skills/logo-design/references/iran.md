# Iranian brands & Persian-script logos

Read this whenever the brand is Iranian, targets Iranian or Persian-speaking audiences (Iran, the diaspora,
Afghanistan/Dari, Tajikistan), needs a Persian (Farsi) name or wordmark, or the user writes in Persian.
Everything in SKILL.md still applies; this file adds what changes.

## 1. Language and chat

- If the user writes in Persian, reply in Persian — explanations, the brief, concept names, the checkpoint message
  and the guidelines. Keep file names, commands, HEX codes and font names in Latin, inside backticks or on their own
  line: mixing Latin runs into RTL sentences scrambles the word order in many viewers.
- Use correct Persian characters: `ی` (U+06CC) and `ک` (U+06A9), not Arabic `ي`/`ك`; Persian digits `۰۱۲۳۴۵۶۷۸۹`
  (U+06F0–U+06F9; note ۴ ۵ ۶ differ from Arabic-Indic ٤ ٥ ٦); and the zero-width non-joiner (نیم‌فاصله, U+200C) in
  words like «می‌شود» and «برنامه‌ها».
- Dates in guidelines and handover notes: give the Solar Hijri (Jalali) date, with the Gregorian date beside it for
  international use.

Checkpoint message in Persian (same shape as SKILL.md):

```markdown
<تصویر مرور مفهوم‌ها>

### الف — <نام>  ·  <نوع نشانه>   ← پیشنهاد من
**ایده:** <یک جمله>
**چرا مناسب است:** <۲–۳ مورد مرتبط با صفت‌ها، مخاطب و رقبا در بریف>

### ب — … / ### ج — …

**پیشنهاد من:** <یک یا دو جمله، همراه با یک ریسک صادقانه برای هر مفهوم>
**قدم بعد:** یکی را انتخاب کنید (یا بگویید از هر کدام چه چیزی را دوست دارید). می‌خواهید کیت کامل لوگو را برای آن آماده کنم؟
پالت رنگ با نسخه‌های تک‌رنگ و معکوس، لاک‌آپ افقی و عمودی (فارسی و لاتین)، نسخهٔ اندازهٔ کوچک، فاویکون و آیکون اپ، بُرد ارائه با ماکاپ، و راهنمای یک‌صفحه‌ای استفاده.
```

## 2. Extra discovery questions

Add these to the brief (fast track: fold the first two into your five questions):

1. **Names in both scripts** — the exact Persian spelling *and* the Latin spelling. Is the Latin a transliteration
   (Digikala), a translation, or a different name? Which one leads?
2. **Market** — domestic Iran, the diaspora, export, or all? This decides which script is primary.
3. **Tone** — contemporary/tech, heritage/craft, or a deliberate mix?
4. **Channels** — app stores (Cafe Bazaar, Myket, Google Play, App Store), Instagram/Telegram avatars, shop signage,
   packaging, a `.ir` website.

## 3. Script strategy

| Situation | Primary mark | Notes |
|---|---|---|
| Domestic consumer brand | Persian wordmark (+ symbol) | Latin lockup as secondary for the app stores and international use |
| Tech/startup, mixed audience | Script-neutral symbol + bilingual lockups | The symbol carries recognition across both scripts |
| Diaspora / export | Latin wordmark + Persian secondary | A Persian detail in the symbol can carry the heritage |
| Heritage, food, craft, culture | Persian calligraphic or Kufic wordmark | Pair with a calm Latin companion |

When the brand is Iranian, make at least one of the three concepts a Persian-script direction (wordmark, letterform or
Kufic monogram) unless the user rules it out. Ownable Persian lettering is one of the strongest options available.

## 4. Persian letterforms

**Structure** (vs. Latin `references/typography.md`):
- Cursive, right to left. Most letters take four contextual forms (isolated, initial, medial, final). Seven never
  join to the following letter — `ا د ذ ر ز ژ و` — so words break into clusters; plan spacing around those gaps.
- Proportions are set by the **baseline**, the **tooth height** (the short vertical strokes of `س ش ب`), tall
  **ascenders** (`ا ل ک گ ط`) and deep **descenders/bowls** (`ی ن ر ز و ج ع م`). There's no x-height; match the tooth
  height to the Latin x-height optically in bilingual lockups.
- **Dots (نقطه) carry meaning**: `ب پ ت ث` and `ج چ ح خ` differ only by dots. Dots that merge, vanish or drift at small
  sizes turn the name into a different word. Make them solid, about stroke-width or larger, clearly separated, and
  run the 16/32 px test from SKILL.md Phase 5 with the dots specifically in mind.
- **Kashida (کشیده)** — stretching a connection — can balance a wordmark's width or build a long horizontal for a
  symbol. Use at most one, at a natural point (after `ب س ک ل`, never inside a cluster that doesn't join). Several
  stretches in one word look amateur.
- `<text>` is even riskier than in Latin: a renderer without proper text shaping draws disconnected isolated letters.
  Construct the letters as paths and check the render.

**Styles** to choose from:
- **Naskh** — the readable book hand. A safe base for modern wordmarks.
- **Nastaliq (نستعلیق)** — the Persian calligraphic style: sloping, hanging, elegant. Strong for heritage, poetry,
  tea, saffron and fashion brands. Fragile at small sizes, so pair it with a simple symbol or a Naskh small-size cut.
  Persian Nastaliq isn't the same as Urdu Nastaliq fonts; don't treat them as interchangeable.
- **Square (bannā'i) Kufic** — letters built on a square grid, as in Isfahan and Yazd tilework. A perfect match for
  the skill's geometric SVG method: draw it with `rect` cells on an exact grid. Great for monograms, app icons and
  tech brands; check that the word is still legible to a Persian reader.
- **Modern geometric/sans Persian** — monoline, simplified joins; the default for apps and startups.
- Avoid Shekasteh and dense Thuluth-style compositions for logos: they're illegible to most readers at small sizes.

**Fonts** for study and lockups (check the licence allows logo use):
- Open licences (SIL OFL): Vazirmatn, Estedad, Sahel, Samim, Lalezar (display), and Noto Naskh Arabic. IranNastaliq is free to
  download for Nastaliq studies; read its licence before using it in a mark. Vazirmatn's Latin and Persian are designed together and suit bilingual lockups.
- Commercial: IRANSans, Yekan Bakh, Dana, Peyda (Fontiran and similar foundries). Many Iranian apps use these; a
  custom wordmark helps you stand apart from them.
- As always, a finished mark is modified or drawn letterforms as paths, not a font set in type.

## 5. Bilingual lockups

- At the same point size, Persian looks smaller and lighter than Latin. Scale the Persian up (often 110–130 %) until
  stroke weight and visual height match, then judge by eye.
- **Horizontal**: put the symbol on the **right** of a Persian wordmark (reading starts there) and on the left of a
  Latin one. With both scripts in one line, put the symbol between them or build two separate lockups.
- **Stacked**: symbol on top; Persian wordmark below, then Latin. Centre all three, or keep the edges consistent:
  Persian right-aligned and Latin left-aligned on the same frame.
- Deliver separate Persian-only, Latin-only and bilingual lockups; don't force both scripts everywhere.
- Mirroring: an RTL interface flips directional icons. Check that the symbol doesn't depend on a left-to-right reading
  (an arrow pointing "forward" to the right reads as "back" in RTL). See `references/visual-techniques.md`.

## 6. Iranian visual vocabulary

Rich sources for fresh forms. Use them as a source of geometry and attitude, not as decoration pasted on.

- **Girih (گره)** — interlaced strapwork on five- and ten-fold geometry (the girih tile set: decagon, pentagon,
  hexagon, bowtie, rhombus). Angles are multiples of 36° (and 18°), so audit with
  `python3 scripts/svg_audit.py --girih mark.svg` to stop real girih angles being flagged as near-misses.
  A single girih star or one knot can be a mark; the full pattern belongs in the identity system as a pattern.
- **Shamseh (شمسه)** — the sun medallion of book covers and ceilings: radial, centred, very logo-shaped.
- **Eslimi (اسلیمی) and Khatai (ختایی)** — arabesque spirals and stylised blossoms. Simplify hard; one curl can be
  enough.
- **Boteh (بته جقه)** — the paisley teardrop of termeh fabric. Very recognisable, so it needs a fresh twist.
- **Architecture** — the pointed arch (طاق), muqarnas, iwan, domes of Isfahan, windcatchers (بادگیر) of Yazd, the
  arch-and-court rhythm of caravanserais.
- **Nature and symbols** — cypress (سرو: resilience), pomegranate (انار: Yalda, abundance), the Simorgh, the
  nightingale and rose (گل و بلبل), the Persian garden (چهارباغ: four quadrants around water), carpet medallions and
  borders.
- **Persepolis and ancient motifs** — lamassu, the griffin/Homa, the lotus. Strong but heavily used by tourism and
  heritage brands, so check the category.

Clichés to treat with care: generic domes for anything Iranian, Azadi Tower for Tehran, the Faravahar on general
products, a carpet border wrapped around a logo, a teapot for every café.

## 7. Colour

Starting points (adjust for contrast and the category, see `references/color.md`):

| Name | Approx. HEX | Associations |
|---|---|---|
| Persian blue / lapis (لاجوردی) | `#1C39BB` | tile domes, depth, trust |
| Turquoise (فیروزه‌ای) | `#30A8B8` | Isfahan tiles, Neyshabur turquoise, protection, luck |
| Saffron (زعفرانی) | `#F4A300` | warmth, food, luxury |
| Pomegranate (اناری) | `#B0213A` | Yalda, abundance, passion |
| Persian green | `#00A693` | gardens, renewal, Nowruz |
| Brick / khesht (آجری) | `#B5643C` | earth, desert architecture, craft |

- Green–white–red together read as the national flag and state; avoid that combination unless the brand intends it.
- Pure black is tied to mourning (Muharram). It's fine as the one-colour version, but think twice before making it the
  brand's colour story for a consumer product.

## 8. Cultural and legal checks

- **Avoid in commercial marks**: the word Allah, Quranic verses, other sacred calligraphy (they end up on packaging
  and in the bin, which offends); the official national emblem; the lion-and-sun (historical but politically loaded
  today); the Faravahar outside cultural or Zoroastrian contexts. Political symbols in general.
- **Gestures and animals**: a thumbs-up has traditionally been rude in Iran; an owl (جغد) is a bad omen in popular
  culture; avoid pigs and anything that suggests alcohol, which is also prohibited in advertising; dogs are sensitive
  for food brands.
- **People**: depictions of women in logos and ads face regulatory rules (hijab). Mascots and figurative marks are
  simpler without human figures.
- **Number 13** — unlucky (Sizdah Bedar). Avoid it in names or as a visible device.
- **Names and signage**: Iranian rules have restricted foreign-language words in shop signage and brand names. Have a
  Persian name or a Persian wordmark ready for the storefront and check the current regulations.
- **Trademark**: Iranian registration goes through the Industrial Property office (اداره کل مالکیت صنعتی). As in
  SKILL.md, recommend a professional search; also search Cafe Bazaar and Myket for name collisions.

## 9. Delivery extras for the kit

- **App stores**: Cafe Bazaar (کافه‌بازار) and Myket (مایکت) ask for a 512 × 512 PNG icon; check their current specs.
  Most Iranian users are on Android, so check the icon under circle and squircle launcher masks. The
  `maskable-512.png` from `export_variants.py --web-icons` keeps the mark inside the safe zone.
- **Social avatars**: Instagram, Telegram, Eitaa, Rubika and Bale crop to a circle. Test the symbol in a circle at
  40–48 px.
- **Website**: the e-Namad (اینماد) trust badge sits in the footer of Iranian online shops. Make sure the logo works
  next to it in the footer mockup.
- **Guidelines**: include the Persian and Latin lockups, minimum sizes for the Persian wordmark (dots set the limit),
  the font licences, and Persian copy with the Jalali date.

## 10. Video channels (YouTube, Aparat)

Many Iranian brands and creators live on video: YouTube for the diaspora and international reach (it's filtered
inside Iran, so domestic viewers often arrive through a VPN), and **Aparat (آپارات)** for a domestic audience. Plan for
both when the brand publishes video.

**Build the kit** from the finished symbol and a horizontal lockup:

```bash
python3 scripts/channel_kit.py brand-symbol.svg --lockup brand-fa-horizontal.svg --bg "#1C39BB" --pattern khatam --png
```

This writes the avatar (800×800, mark kept inside the circle crop), a 2560×1440 banner with the logo in the 1235×338
area visible on every device, a guide version with the TV / desktop / safe-area outlines, and a 150×150 watermark.
`--pattern khatam` adds a faint eight-point-star (khatam, خاتم) lattice, a quiet Iranian texture that keeps the logo
area clear. Render and look at the guide version before delivery.

- **Which lockup**: on Aparat, use the Persian lockup. On YouTube, use Latin or bilingual for an international
  channel and Persian for a diaspora channel that speaks Persian. Keep the symbol identical on both platforms so
  viewers recognise it.
- **Aparat sizes**: Aparat's profile image and cover crop differently from YouTube's, and its specs change, so check
  the current upload guidance. The avatar works as is; crop the cover from the banner master and keep the logo
  centred.
- **Avatar**: the channel name sits next to it in Persian or Latin, so the avatar should be the symbol only, not a
  shrunken wordmark. Test it at 48 px and 98 px in a circle.
- **Watermark**: it sits in the corner of every video. Use the simplest form of the mark and check it over both light
  and dark footage.
- **Thumbnails** (1280×720) are part of the system:
  - Fix one Persian display face (e.g. Lalezar, or the bold weight of the brand's Persian font), one accent colour
    and one position for the logo.
  - Persian text reads right to left, so anchor the headline on the right and the face or subject on the left.
  - Persian headlines need extra line height for dots and descenders. Keep them to 2–4 words, and check them at
    phone size (about 160 px wide).
  - Render thumbnail text with a tool that shapes Persian correctly, and look at the result.
