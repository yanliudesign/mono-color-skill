---
name: mono-color
description: Generate original one-ink or controlled two-ink editorial print images from any theme, sentence, article idea, object, or reference photo. Always use this skill when the user asks for 单色海报、双色印刷、单色调视觉、蓝色/绿色孔版印刷、risograph、网点照片、复古编辑排版、zine poster, monochrome editorial poster, duotone print, or asks to use the mono-color style. It preserves a warm paper base, no more than two printing inks, halftone imagery, active negative space, terse human language, and strong serif/grotesk/mono typography while never copying a source composition, wording, logo, or artwork. Produce both the final generation prompt and the generated raster image unless the user explicitly asks for prompt only.
---

# Monocolor Editorial Print

Turn any user theme or image into an original printed editorial artifact with one stable visual language:

> warm paper + one or two inks + reproduced image + typographic tension + concise human voice

Do not imitate any one reference. Recombine the system below into a new composition every time.

## Default Deliverable

Create:

1. one final image-generation prompt;
2. one generated raster image;
3. a short recipe note naming palette, layout family, type pairing, and print process.

Save generated files under `~/Desktop/Claude skills/mono-color/` when a file path is available. Create the folder if needed. Stop at prompt-only only when the user explicitly asks for it or no image-generation capability is available.

## Input Reading

Extract four things before composing:

- **Subject:** the one person, object, scene, or idea that must remain recognizable.
- **Intent:** poetic observation, announcement, field note, personal statement, cultural poster, or specimen page.
- **Words:** preserve exact supplied text in its original language. When no text is supplied, invent one English display phrase of 2-8 words and preserve it across retries. Omit display text only when the user explicitly requests a text-free image.
- **Image role:** hero photograph, isolated specimen, cropped fragment, texture source, or no supplied image.
- **Representation:** faithful reproduction or abstract symbol extraction. Choose abstract symbol extraction when the user asks for abstract, artistic, loose, experimental, less realistic, or less photographic treatment.

For a complex topic, choose one concrete visual metaphor. Do not illustrate every point.

When the user supplies an image, preserve its identity and core factual content. In faithful reproduction, crop, isolate, enlarge, simplify, or convert it to halftone. In abstract symbol extraction, preserve 2-4 identifying anchors while replacing photographic description with simplified masses, contours, repeated marks, and exposed paper. Never replace the subject or invent branded details.

### Recipe Manifest

Before writing the generation prompt, resolve the input into this manifest. Do not skip fields and do not expose the manifest unless the user asks for process details.

Use the machine-readable catalogs in `design-system/` as the source of truth for palette IDs, typography roles, composition geometry, carrier signals, and controlled print imperfections. Read only the relevant catalog for the current decision. The prose below explains intent; when an exact value differs, the catalog wins.

```yaml
subject: <one recognizable subject>
intent: <one intent from Input Reading>
exact_text: <user text, generated 2-8 word phrase, or none>
text_language: <language of supplied text, otherwise English>
representation: <faithful reproduction or abstract symbol extraction>
ratio: <explicit ratio or 3:4>
carrier: <one carrier ID from design-system/carriers.json or none>
mode: <pure one-ink, chromatic + black, complementary duotone, or overprint duotone>
palette: <one palette ID from design-system/colors.json>
inks: <the palette's named ink or approved pair with exact hex values>
plate_roles: <one explicit role per ink plate>
layout: <one composition ID from design-system/compositions.json>
empty_paper: <explicit percentage>
image_treatment: <one mechanical reproduction process>
type_hierarchy: <one role ID from design-system/typography.json>
disruption: <one deliberate disruption>
imperfection_seed: <stable hash derived from the resolved recipe>
imperfections: <2-3 effect IDs from design-system/imperfections.json>
```

Use these defaults whenever the user has not made the choice:

- ratio: `3:4`;
- representation: `faithful reproduction`, unless the user asks for abstract, artistic, loose, experimental, less realistic, or less photographic treatment;
- text language: English for all invented display text, labels, and microcopy;
- paper: warm ivory `#F5F1E8`;
- mode and ink: pure one-ink cobalt `#2148B8`, unless the subject maps directly to another named one-ink palette below;
- empty paper: `35%`;
- image treatment: coarse halftone;
- type hierarchy: Poetic for reflective language, Civic for events, Archival for specimens, and Typographic when the supplied phrase is the subject;
- disruption: one off-center image crop; use one oversized word instead when there is no image.
- imperfections: choose 2-3 effects using a stable hash of subject, exact text, palette, and layout; preserve the same seed across retries.

Explicit user choices override defaults unless they violate the two-ink limit or the originality firewall. For identical inputs, resolve the same manifest; do not vary palette, layout, percentages, or process merely for novelty. This stabilizes the design procedure while image-generation details may still vary.

Resolve generic color words consistently: blue to Cobalt, green to Botanical Green, orange to Terracotta Orange, red to Signal Red, purple to Aubergine, and black to Charcoal. For generic green + black, use Mint Green + Charcoal. For generic blue + orange, use Cobalt + Terracotta. Exact named inks always take precedence over these aliases.

## Visual DNA

### 1. Color System

Default to one ink. Use two inks only when the content needs information separation, object contrast, or visible overprint tension. The paper substrate does not count as an ink.

- **Paper:** ivory, bone, or slightly gray recycled stock; target feeling `#F2F0E8` to `#FAF7ED`.
- **Plate limit:** use one printing plate by default and never more than two ink plates.
- **Ink density:** darker coverage may appear near-black and sparse halftones may appear pale. These are density changes, not extra inks.
- **Paper exposure:** keep the paper visible. Never tint the whole page into a digital monochrome wash.

#### One-Ink Palette

- **Cobalt / Ultramarine:** `#2148B8`, the default for technology, knowledge, cities, music, and cultural subjects.
- **Royal Blue:** `#2058D4`, a brighter branch for youth culture, fashion, movement, and energetic editorial pages.
- **Botanical Green:** `#008A4B`, for botanical, ecological, archival, and explicitly green subjects.
- **Mint Green:** `#5EB783`, for observation journals, soft natural subjects, and quiet editorial photography.
- **Terracotta Orange:** `#C65F38`, for classical art, food, travel, summer, and tactile objects.
- **Signal Red:** `#C83232`, for declarations, music, events, and civic or public-culture subjects.
- **Aubergine:** `#63365F`, for literature, cinema, night, and intimate cultural subjects.
- **Charcoal:** `#30343A`, for architecture, photography, research, and restrained publications.

#### Two-Ink Recipes

Use a known pair rather than improvising arbitrary colors:

- **Powder Blue + Signal Red:** `#9EB8D3` + `#C83232` for guides, announcements, and information-heavy editorial pages.
- **Cobalt + Terracotta:** `#2148B8` + `#C65F38` for travel, summer, food, and lifestyle subjects.
- **Botanical Green + Oxblood:** `#008A4B` + `#8F3434` for plants, natural wine, bookstores, and archives.
- **Charcoal + Signal Red:** `#30343A` + `#C83232` for architecture, exhibitions, reports, and conceptual work.
- **Electric Blue + Carbon:** `#173AE3` + `#242321` for high-contrast cultural events and image-led editorial pages.
- **Mint Green + Charcoal:** `#5EB783` + `#302D2E` for journals, essays, observations, and long-form reading.
- **Ultramarine + Safety Orange:** `#263E99` + `#E55D2B` for movement, objects, youth culture, and active urban subjects.
- **Cyan + Brick Red:** `#159DDA` + `#B64032` for repeated products, exhibitions, and playful information systems.
- **Tangerine + Slate Blue:** `#E46C2D` + `#4773A5` for markets, festivals, illustrated notices, and large typographic compositions.

#### Print Modes

1. **Pure one-ink:** one ink carries image, typography, and rules through density changes. This remains the default.
2. **Chromatic ink + black:** the chromatic plate carries the photograph or dominant graphic; carbon or charcoal carries long text and precision labels.
3. **Complementary duotone:** one dominant ink occupies 70%-85% of the printed area; the accent ink occupies 15%-30% and has a specific role such as dates, annotations, or selected objects.
4. **Overprint duotone:** two plates may overlap. The darker mixed appearance in overlap zones is a physical consequence of two inks and does not count as a third ink.

Assign each plate a role before composing. Never scatter two colors as arbitrary decoration. These constraints keep the result mechanically printed rather than digitally color-graded.

### 2. Space and Grid

- Use a flat, front-facing paper canvas with no mockup, frame, desk, or cast shadow.
- Default to a `3:4` vertical poster. Respect a user-specified ratio.
- Keep 25%-55% of the canvas as visibly empty paper.
- Use generous outer margins: 5%-9% of page width.
- Align most elements to one invisible left edge or a simple 2-3 column editorial grid.
- Create one deliberate disruption: a floating word, off-center image, oversized title, circular mark, or tiny annotation.
- Never center every element. Never distribute objects evenly like a template.

Negative space is active pacing, not leftover room.

### Reference-Derived Composition Grammar

The reference set shares an object-and-type construction, not a generic retro mood. Build every page from these four moves:

1. **One object dominates.** Use one person, animal, ordinary object, or repeated specimen as the visual anchor. Let it occupy 45%-80% of the page and crop it decisively at one or more edges when scale creates tension. Do not spread several small atmospheric props across the page.
2. **Type collides with the object.** Let one headline cross, cover, split around, or align tightly against the dominant image. Keep enough contrast for the words to remain readable. Do not place every line in a detached safe zone above the image.
3. **Paper cuts through the image.** Use clipped highlights, irregular cutout gaps, halftone fade-outs, or plate knockouts so exposed paper becomes a visible shape inside the composition, not only an outer margin.
4. **One manual gesture interrupts the system.** Choose one circled fact, hand-drawn line, registration mark, tiny symbol, rotated label, or ruled data strip. Use one gesture family only; multiple doodle styles turn the page into scrapbook decoration.

Choose one dominant object and one dominant typographic event before adding secondary information. If either is missing, simplify rather than filling the page with mood-setting decoration.

### 3. Image Treatment

Convert all photographs and illustrations into the selected ink plate or plates plus paper:

- coarse halftone, risograph grain, cyanotype-like exposure, photocopy breakup, or newspaper screening;
- visible dots at close range, recognizable subject at thumbnail scale;
- clipped highlights where paper shows through and dense shadows where ink pools;
- mild ink bleed, uneven coverage, scan noise, paper fibers, and optional 1-2 mm registration drift between plates;
- medium contrast; avoid glossy photographic depth.

#### Abstract Looseness

When `representation` is `abstract symbol extraction`, transform the supplied image into a small visual vocabulary instead of applying a stylized filter to the whole photograph:

1. Name 2-4 **identity anchors** that make the subject recognizable, such as a square sail, curved hull, mast, and wave direction. Preserve their relationship, not their photographic detail.
2. Convert the anchors into **one dominant mass**, **one structural contour**, and **one repeated rhythm**. Use flat plate shapes, broken hand-drawn lines, short strokes, dots, or paper cutouts; omit incidental scenery and fine surface description.
3. Let paper replace at least 35% of the source scene. Crop one anchor at a page edge and allow one type or line element to cross it. Abstraction must create active space, not merely blur or posterize the photo.
4. Keep the abstract geometry deterministic. Apply looseness through slightly irregular contours, uneven repeated marks, and the recipe's 2-3 controlled print imperfections; do not randomly move anchors between retries.
5. Stop before the subject becomes generic. At thumbnail scale, at least two identity anchors must still communicate the original subject without relying on the caption.

For complementary duotone abstraction, assign the dominant ink to structure and rhythm, and reserve the accent ink for one identity anchor or one annotation. Do not distribute the accent evenly across the page.

#### Controlled Chance

Keep composition, wording, palette, and hierarchy deterministic. Introduce looseness only in the reproduction layer by selecting 2-3 effects from `design-system/imperfections.json` with the resolved recipe's stable seed.

- Let uneven ink density, dry-edge breakup, halftone drift, registration drift, or one broken manual gesture create the analog variation.
- Apply variation to large type, image plates, solid shapes, or the single gesture family; never distort microcopy or factual text.
- Keep all effect values inside the catalog ranges. The same resolved input must reproduce the same marks and offsets.
- In one-ink work, registration drift may appear only as a pale second impression of the same ink. It does not add another color.
- Do not use controlled chance to move the dominant object, change line breaks, alter the grid, or compensate for an unresolved composition.

Use one dominant image zone occupying 45%-80% of the page, 1-3 isolated specimens whose combined area stays in that range, or one repeated object system. A ruled information poster may reduce the image zone to 32%-55% only when real supplied information needs the space. Dense overlap is allowed only in the **overprint collage** family; it must still read as two printing plates rather than scrapbook decoration.

### 4. Typography

Build tension with two voices, never more than three:

- **Editorial voice:** high-contrast old-style or transitional serif, with optional italic for intimate or poetic language.
- **Utility voice:** condensed grotesk, geometric sans, typewriter, or monospaced caps for labels, dates, credits, and coordinates.

Choose one hierarchy:

- **Poetic:** large serif phrase + tiny monospaced annotations.
- **Civic:** bold condensed sans headline + small factual footer.
- **Archival:** restrained serif title + ruled metadata table + specimen captions.
- **Typographic:** oversized words become the main image; photograph becomes supporting evidence.

Rules:

- Use one dramatic scale jump: largest text is 5-12 times the microcopy size.
- Prefer lowercase for intimate statements and uppercase for public declarations.
- Keep display copy to 2-8 words and all other copy sparse.
- Default all invented words to natural English, even when the user's request is written in another language. Preserve user-supplied wording exactly and do not translate it unless asked.
- Use exact readable wording only when the user supplies it or it carries the concept. Otherwise use plausible microtype as texture and do not invent organizations, URLs, sponsors, or event facts.
- No gradient type, outline effects, drop shadows, inflated 3D letters, or generic luxury-fashion spacing.

### 5. Communication Tone

Write like an independent cultural poster, field journal, or community print notice:

- terse, observant, romantic, and free-spirited without becoming sentimental;
- human and specific rather than inspirational;
- quiet confidence, dry wit, or factual clarity;
- no sales language, CTA, hype, productivity slogans, or brand manifesto voice.

For summer, movement, travel, leisure, music, and night subjects, make romantic freedom the default emotional register. Express it through a physical sensation, an open direction, an unhurried gesture, or a small relationship between subject and space. Favor fresh English fragments such as an observation or invitation, never a generic motivational slogan. For factual, civic, scientific, or archival subjects, let clarity override this romantic default.

If text must be invented, prefer an English observation, plain declaration, object label, or small contradiction. Never reuse wording visible in reference images or repeat a stock phrase across unrelated outputs.

For romantic, intimate, nostalgic, or poetic prompts, express feeling through one observable relationship: two figures sharing one edge, an object carrying signs of use, a crop that implies closeness, or a small distance between forms. Do not default to string lights, wine glasses, fluttering fabric, stars, flowers, sunset silhouettes, or cinematic haze. Those props describe a romance category; a specific relationship creates romance while preserving the reference set's graphic directness.

## Composition Decision Flow

Choose the layout from the content, not at random. Walk this list from top to bottom and use the first matching rule unless the user explicitly requests a layout:

1. Is the content an event, method, schedule, or factual announcement?
   - Yes: choose **ruled information poster**.
2. Is the subject botanical, collected, or taxonomic?
   - Yes: choose **archival plate** and consider botanical green.
3. Is one ordinary object explicitly requested as a repeated rhythm?
   - Yes: choose **object field**.
4. Does the concept explicitly depend on two images, colors, or type layers physically crossing?
   - Yes: choose **overprint collage** and use overprint duotone.
5. Is there one supplied portrait or scene photograph?
   - Yes, and representation is faithful reproduction: choose **image field**.
   - Yes, and representation is abstract symbol extraction: choose **editorial cover** by default; choose **overprint collage** only when two extracted layers must physically cross.
6. Are there 1-3 supplied isolated objects intended for labels or comparison?
   - Yes: choose **specimen annotation**.
7. Is the user's phrase itself the main visual subject?
   - Yes: choose **type-led declaration**.
8. Is the content reflective, dated, or essay-like with a primary photograph and readable text?
   - Yes: choose **editorial journal**.
9. Otherwise choose **editorial cover**.

### Layout Families

- **Image field:** large screened image crossing at least one page edge; headline overlaps or locks tightly to it; compact footer.
- **Specimen annotation:** 1-3 isolated cutouts with numbered labels, one oversized phrase, and asymmetric empty space.
- **Type-led declaration:** headline controls the page; a smaller screened image interrupts or grounds it.
- **Ruled information poster:** one dominant screened object or scene is crossed by a headline; thin one-ink rules form one metadata band and the date remains subordinate.
- **Archival plate:** title, one rectangular image plate, and a disciplined multi-column caption block.
- **Editorial cover:** title near one edge, one dominant image zone, sparse issue-like microcopy, no fake masthead brand.
- **Object field:** one recognizable object repeated at varied scale, crop, or angle to form a printed rhythm; keep one open zone for title and facts.
- **Overprint collage:** two ink plates carry separate object, image, geometric, or typographic layers and cross in selected zones; use overlap deliberately, not everywhere.
- **Editorial journal:** one primary screened photograph, a strong title or date, and 2-3 disciplined text columns with enough size and contrast for real reading.

## Prompt Compiler

Write the final prompt in five compact paragraphs, in this order:

1. **Canvas and ink:** ratio, warm paper, exact one- or two-ink palette, print mode, plate roles, and flat scanned page.
2. **Original composition:** chosen layout family, margins, empty-space percentage, grid, dominant object scale and edge crop, and one manual gesture.
3. **Subject:** what appears; for faithful reproduction, describe preservation, crop, size, halftone treatment, and paper exposure; for abstract symbol extraction, name the 2-4 identity anchors, dominant mass, structural contour, repeated rhythm, omitted detail, and where exposed paper cuts through the scene.
4. **Typography and words:** hierarchy, type voices, exact short display text, and the explicit overlap, crossing, split, or tight alignment between headline and dominant object; include a ruled data strip only when needed.
5. **Material and avoids:** dots, fibers, bleed, misregistration, plus the hard negative constraints and any topic-specific cliches to exclude.

Describe only visible outcomes. Do not mention reference artists, studios, sample posters, or “in the style of.”

## Originality Firewall

The reference is evidence for a visual grammar, never a layout to trace.

Before generation, change at least four of these from any supplied reference:

- subject and crop;
- layout family;
- headline wording;
- headline location;
- image shape or count;
- grid structure;
- type pairing;
- metadata treatment;
- ratio;
- disruption device.

Never reproduce a reference's exact object arrangement, line breaks, labels, dates, logos, border system, or distinctive slogan. Never include fake signatures or publication marks. If the user's source image contains protected or branded material, transform only the user's provided material and avoid presenting the result as an official artifact.

## Hard Avoids

Always exclude:

- more than two printing inks, unassigned accent colors, gradients, rainbow accents, neon, or full-color photography;
- clean vector-flat digital poster aesthetics;
- beige lifestyle minimalism or monochrome color wash;
- glossy mockups, 3D depth, cinematic lighting, lens blur, hard shadows;
- centered template symmetry, card grids, UI panels, stickers, decorative blobs;
- scrapbook collage, uncontrolled overlap, grunge overload, or torn-paper styling;
- long paragraphs, marketing copy, CTA buttons, logos, URLs, QR codes;
- exact imitation of a supplied poster or recognizable artist signature.

## Generation and Inspection

1. Generate the image with the compiled prompt.
2. Inspect it at full size and thumbnail size.
3. Regenerate once when any of these fail:
   - a one-ink composition shows a second ink, or a two-ink composition shows a third printing ink;
   - a two-ink composition lacks clear plate roles or uses the accent across more than 30% without a subject-driven reason;
   - the page reads as digitally color-graded rather than physically printed;
   - empty paper falls outside 25%-55%;
   - the subject is unrecognizable;
   - typography lacks a clear 5x or greater scale jump;
   - long text is garbled or invented branding appears;
   - the composition closely follows a supplied reference.
4. If exact text renders incorrectly after one retry, generate a text-light base image and state that typography should be overlaid in a layout tool. Do not pretend distorted text is correct.

## Output Format

````markdown
**生成图**

![Monocolor editorial print](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[prompt used for generation]
```

**本次配方**

- Mode: [pure one-ink / chromatic + black / complementary duotone / overprint duotone]
- Ink: [exact one- or two-ink palette and hex values]
- Layout: [layout family]
- Type: [editorial voice + utility voice]
- Process: [halftone/risograph/cyanotype/photocopy treatment]
- Originality: [one sentence naming the major structural departures from references]
````

## Final Quality Gate

- Is there one warm paper and no more than two printing inks?
- If there are two inks, does each plate have a clear role and does the accent remain controlled?
- Does 25%-55% of the page remain visibly empty?
- Is the image reproduced through dots or mechanical print texture rather than a color filter?
- Does one object occupy 45%-80% of the page, except for a justified information-heavy layout?
- Does the headline visibly cross, cover, split around, or lock tightly to the dominant object?
- Does exposed paper form a visible shape inside the image through highlights, gaps, fade-outs, or knockouts?
- Is there exactly one manual gesture family rather than several decorative doodle styles?
- Does the type hierarchy use a 5x-12x scale jump and no more than three type voices?
- Is the language terse, specific, and non-commercial?
- Is the user's supplied subject preserved?
- Are at least four structural features different from every supplied reference?
- Did the run generate an image unless prompt-only was requested?

## Example Triggers

- “用 mono-color 做一张关于夏天散步的海报。”
- “把这张咖啡照片变成蓝色网点编辑封面。”
- “做一个绿色植物主题的孔版印刷 poster。”
- “沿用之前那套单色、留白、复古印刷的视觉。”
- “Make this portrait into a one-ink editorial zine cover.”
- “用蓝橙双色叠印做一张城市骑行活动视觉。”
- “把这个产品做成重复物件构图的双色孔版印刷封面。”
- “用绿色照片和黑色正文做一页观察日志。”