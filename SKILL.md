---
name: mono-color
description: Generate original monochrome editorial print images from any theme, sentence, article idea, object, or reference photo. Always use this skill when the user asks for 单色海报、单色调视觉、蓝色/绿色孔版印刷、risograph、网点照片、复古编辑排版、zine poster, monochrome editorial poster, or asks to use the mono-color style. It preserves a warm paper base, one-ink palette, halftone imagery, large negative space, terse editorial language, and strong serif/grotesk/mono typography while never copying a source composition, wording, logo, or artwork. Produce both the final generation prompt and the generated raster image unless the user explicitly asks for prompt only.
---

# Monocolor Editorial Print

Turn any user theme or image into an original printed editorial artifact with one stable visual language:

> warm paper + one ink + reproduced image + typographic tension + concise human voice

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
- **Words:** exact supplied text, or one invented phrase of 2-8 words plus optional factual microcopy.
- **Image role:** hero photograph, isolated specimen, cropped fragment, texture source, or no supplied image.

For a complex topic, choose one concrete visual metaphor. Do not illustrate every point.

When the user supplies an image, preserve its identity and core factual content. Crop, isolate, enlarge, simplify, or convert it to halftone; do not replace the subject or invent branded details.

## Visual DNA

### 1. Color System

Use exactly one chromatic ink per image over warm uncoated paper.

- **Paper:** ivory, bone, or slightly gray recycled stock; target feeling `#F2F0E8` to `#FAF7ED`.
- **Default ink:** saturated cobalt/ultramarine, visually near `#2148B8`.
- **Alternate ink:** botanical green, visually near `#008A4B`, when the subject is botanical, ecological, archival, or explicitly green.
- The alternate is a subject-driven branch, not a second color. Never place cobalt and green together.
- Let darker ink density create apparent navy/black and lighter halftone density create pale tints. These are one ink, not extra colors.
- Keep the paper visible. Never tint the whole page into a digital monochrome wash.

This constraint makes the work feel mechanically printed rather than color-graded.

### 2. Space and Grid

- Use a flat, front-facing paper canvas with no mockup, frame, desk, or cast shadow.
- Default to a vertical poster between 3:4 and 4:5. Respect a user-specified ratio.
- Keep 25%-55% of the canvas as visibly empty paper.
- Use generous outer margins: 5%-9% of page width.
- Align most elements to one invisible left edge or a simple 2-3 column editorial grid.
- Create one deliberate disruption: a floating word, off-center image, oversized title, circular mark, or tiny annotation.
- Never center every element. Never distribute objects evenly like a template.

Negative space is active pacing, not leftover room.

### 3. Image Treatment

Convert all photographs and illustrations into the selected ink plus paper:

- coarse halftone, risograph grain, cyanotype-like exposure, photocopy breakup, or newspaper screening;
- visible dots at close range, recognizable subject at thumbnail scale;
- clipped highlights where paper shows through and dense shadows where ink pools;
- mild ink bleed, uneven coverage, scan noise, paper fibers, and optional 1-2 mm registration drift;
- medium contrast; avoid glossy photographic depth.

Use one dominant image zone occupying 28%-62% of the page, or 1-3 isolated specimens whose combined area stays in that range. Do not build a scrapbook collage.

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

Choose the layout from the content, not at random:

1. Is there one strong supplied photograph?
   - Yes: choose **image field** or **specimen annotation**.
2. Is the user's phrase itself the main idea?
   - Yes: choose **type-led declaration**.
3. Is the content an event, method, schedule, or factual announcement?
   - Yes: choose **ruled information poster**.
4. Is the subject botanical, collected, or taxonomic?
   - Yes: choose **archival plate** and consider botanical green.
5. Otherwise choose **editorial cover**.

### Layout Families

- **Image field:** large screened image in the middle or lower half; headline separated by open paper; compact footer.
- **Specimen annotation:** 1-3 isolated cutouts with numbered labels, one oversized phrase, and asymmetric empty space.
- **Type-led declaration:** headline controls the page; a smaller screened image interrupts or grounds it.
- **Ruled information poster:** thin one-ink rules form a top or bottom metadata band; the center remains open and expressive.
- **Archival plate:** title, one rectangular image plate, and a disciplined multi-column caption block.
- **Editorial cover:** title near one edge, one dominant image zone, sparse issue-like microcopy, no fake masthead brand.

Do not use the same family for consecutive outputs when prior outputs are visible.

## Prompt Compiler

Write the final prompt in five compact paragraphs, in this order:

1. **Canvas and ink:** ratio, warm paper, exact single ink, flat scanned page.
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

- multiple chromatic inks, gradients, rainbow accents, neon, or full-color photography;
- clean vector-flat digital poster aesthetics;
- beige lifestyle minimalism or monochrome color wash;
- glossy mockups, 3D depth, cinematic lighting, lens blur, hard shadows;
- centered template symmetry, card grids, UI panels, stickers, decorative blobs;
- dense collage, grunge overload, torn-paper scrapbook styling;
- long paragraphs, marketing copy, CTA buttons, logos, URLs, QR codes;
- exact imitation of a supplied poster or recognizable artist signature.

## Generation and Inspection

1. Generate the image with the compiled prompt.
2. Inspect it at full size and thumbnail size.
3. Regenerate once when any of these fail:
   - more than one chromatic ink appears;
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

- Ink: [cobalt or botanical green]
- Layout: [layout family]
- Type: [editorial voice + utility voice]
- Process: [halftone/risograph/cyanotype/photocopy treatment]
- Originality: [one sentence naming the major structural departures from references]
````

## Final Quality Gate

- Is there one warm paper and exactly one chromatic ink?
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