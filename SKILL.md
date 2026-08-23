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
- **Words:** exact supplied text, or no display text when none is requested. If the user explicitly asks for invented copy, choose one phrase of 2-8 words before building the manifest and preserve it across retries.
- **Image role:** hero photograph, isolated specimen, cropped fragment, texture source, or no supplied image.

For a complex topic, choose one concrete visual metaphor. Do not illustrate every point.

When the user supplies an image, preserve its identity and core factual content. Crop, isolate, enlarge, simplify, or convert it to halftone; do not replace the subject or invent branded details.

### Recipe Manifest

Before writing the generation prompt, resolve the input into this manifest. Do not skip fields and do not expose the manifest unless the user asks for process details.

```yaml
subject: <one recognizable subject>
intent: <one intent from Input Reading>
exact_text: <user text, generated 2-8 word phrase, or none>
ratio: <explicit ratio or 3:4>
mode: <pure one-ink, chromatic + black, complementary duotone, or overprint duotone>
inks: <named ink or approved pair with exact hex values>
plate_roles: <one explicit role per ink plate>
layout: <one layout family>
empty_paper: <explicit percentage>
image_treatment: <one mechanical reproduction process>
type_hierarchy: <one hierarchy>
disruption: <one deliberate disruption>
```

Use these defaults whenever the user has not made the choice:

- ratio: `3:4`;
- paper: warm ivory `#F5F1E8`;
- mode and ink: pure one-ink cobalt `#2148B8`, unless the subject maps directly to another named one-ink palette below;
- empty paper: `35%`;
- image treatment: coarse halftone;
- type hierarchy: Poetic for reflective language, Civic for events, Archival for specimens, and Typographic when the supplied phrase is the subject;
- disruption: one off-center image crop; use one oversized word instead when there is no image.

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

### 3. Image Treatment

Convert all photographs and illustrations into the selected ink plate or plates plus paper:

- coarse halftone, risograph grain, cyanotype-like exposure, photocopy breakup, or newspaper screening;
- visible dots at close range, recognizable subject at thumbnail scale;
- clipped highlights where paper shows through and dense shadows where ink pools;
- mild ink bleed, uneven coverage, scan noise, paper fibers, and optional 1-2 mm registration drift between plates;
- medium contrast; avoid glossy photographic depth.

Use one dominant image zone occupying 28%-62% of the page, 1-3 isolated specimens whose combined area stays in that range, or one repeated object system. Dense overlap is allowed only in the **overprint collage** family; it must still read as two printing plates rather than scrapbook decoration.

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
- Use exact readable wording only when the user supplies it or it carries the concept. Otherwise use plausible microtype as texture and do not invent organizations, URLs, sponsors, or event facts.
- No gradient type, outline effects, drop shadows, inflated 3D letters, or generic luxury-fashion spacing.

### 5. Communication Tone

Write like an independent cultural poster, field journal, or community print notice:

- terse, direct, observant, slightly poetic;
- human and specific rather than inspirational;
- quiet confidence, dry wit, or factual clarity;
- no sales language, CTA, hype, productivity slogans, or brand manifesto voice.

If text must be invented, prefer forms such as a plain declaration, an object label, a date-like note, or a small contradiction. Never reuse wording visible in reference images.

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
   - Yes: choose **image field**.
6. Are there 1-3 supplied isolated objects intended for labels or comparison?
   - Yes: choose **specimen annotation**.
7. Is the user's phrase itself the main visual subject?
   - Yes: choose **type-led declaration**.
8. Is the content reflective, dated, or essay-like with a primary photograph and readable text?
   - Yes: choose **editorial journal**.
9. Otherwise choose **editorial cover**.

### Layout Families

- **Image field:** large screened image in the middle or lower half; headline separated by open paper; compact footer.
- **Specimen annotation:** 1-3 isolated cutouts with numbered labels, one oversized phrase, and asymmetric empty space.
- **Type-led declaration:** headline controls the page; a smaller screened image interrupts or grounds it.
- **Ruled information poster:** thin one-ink rules form a top or bottom metadata band; the center remains open and expressive.
- **Archival plate:** title, one rectangular image plate, and a disciplined multi-column caption block.
- **Editorial cover:** title near one edge, one dominant image zone, sparse issue-like microcopy, no fake masthead brand.
- **Object field:** one recognizable object repeated at varied scale, crop, or angle to form a printed rhythm; keep one open zone for title and facts.
- **Overprint collage:** two ink plates carry separate object, image, geometric, or typographic layers and cross in selected zones; use overlap deliberately, not everywhere.
- **Editorial journal:** one primary screened photograph, a strong title or date, and 2-3 disciplined text columns with enough size and contrast for real reading.

## Prompt Compiler

Write the final prompt in five compact paragraphs, in this order:

1. **Canvas and ink:** ratio, warm paper, exact one- or two-ink palette, print mode, plate roles, and flat scanned page.
2. **Original composition:** chosen layout family, margins, empty-space percentage, grid, and one deliberate disruption.
3. **Subject:** what appears, how a supplied image is preserved/cropped, image size, and halftone treatment.
4. **Typography and words:** hierarchy, type voices, exact short display text, placement, rules/table if used.
5. **Material and avoids:** dots, fibers, bleed, misregistration, plus the hard negative constraints.

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
- Is there one dominant zone and one deliberate disruption?
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