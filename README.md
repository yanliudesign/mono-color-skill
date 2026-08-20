<div align="center">

[中文](./README.zh.md) · **English**

# Monocolor Editorial Print

**A one-ink and controlled two-ink editorial image skill for posters, zines, portraits, packaging, and visual field notes.**

[![Version](https://img.shields.io/badge/VERSION-1.1.0-2ea44f?style=flat-square&labelColor=333)](./SKILL.md)
[![Skills](https://img.shields.io/badge/SKILLS-1-2ea44f?style=flat-square&labelColor=333)](./SKILL.md)
[![Stars](https://img.shields.io/github/stars/yanliudesign/mono-color-skill?style=flat-square&label=STARS&color=e37f2c&labelColor=333)](https://github.com/yanliudesign/mono-color-skill/stargazers)

[![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-d97757?style=flat-square&labelColor=1a1a1a&logo=anthropic&logoColor=white)](https://claude.ai/code)
[![SKILL.md](https://img.shields.io/badge/Agent-SKILL.md-214f9b?style=flat-square&labelColor=1a1a1a)](./SKILL.md)

</div>

Turn a theme, sentence, object, or supplied photograph into an original editorial print. The skill defaults to one ink and opens a controlled two-ink branch when the content needs information separation, object contrast, or overprint tension. Warm paper, screened imagery, active negative space, and sharp typographic contrast keep both modes inside one recognizable visual system.

It preserves a visual system rather than copying a reference. Every composition is rebuilt around the subject, intent, words, and image role.

## What it does

| System | Direction |
|---|---|
| **Input** | A theme, phrase, object, article idea, or supplied photograph |
| **Palette** | Warm uncoated paper + one ink by default, or one of nine controlled two-ink recipes |
| **Modes** | Pure one-ink, chromatic + black, complementary duotone, or overprint duotone |
| **Image** | Halftone, risograph grain, cyanotype exposure, or photocopy breakup |
| **Space** | 25%–55% visible empty paper on an asymmetric editorial grid |
| **Type** | Serif editorial voice + condensed sans or monospaced utility voice |
| **Output** | Generated raster image, exact production prompt, and a short recipe |

## How it works

```text
1  Read the input       →  identify subject, intent, words, and image role
2  Choose the layout    →  image, specimen, declaration, object field, overprint, journal, or cover
3  Assign the plates    →  default to one ink; give each plate a clear role when using two
4  Compose the page     →  preserve 25%–55% silence and add one deliberate disruption
5  Generate and inspect →  check ink count, identity, hierarchy, texture, and originality
```

## Ink system

**One-ink palette:** Cobalt, Royal Blue, Botanical Green, Mint Green, Terracotta Orange, Signal Red, Aubergine, and Charcoal.

| Swatch | Ink | Hex |
|---|---|---|
| ![Cobalt](https://img.shields.io/badge/■■■■-2148B8?style=flat-square&labelColor=2148B8&color=2148B8) | Cobalt / Ultramarine | `#2148B8` |
| ![Royal Blue](https://img.shields.io/badge/■■■■-2058D4?style=flat-square&labelColor=2058D4&color=2058D4) | Royal Blue | `#2058D4` |
| ![Botanical Green](https://img.shields.io/badge/■■■■-008A4B?style=flat-square&labelColor=008A4B&color=008A4B) | Botanical Green | `#008A4B` |
| ![Mint Green](https://img.shields.io/badge/■■■■-5EB783?style=flat-square&labelColor=5EB783&color=5EB783) | Mint Green | `#5EB783` |
| ![Terracotta Orange](https://img.shields.io/badge/■■■■-C65F38?style=flat-square&labelColor=C65F38&color=C65F38) | Terracotta Orange | `#C65F38` |
| ![Signal Red](https://img.shields.io/badge/■■■■-C83232?style=flat-square&labelColor=C83232&color=C83232) | Signal Red | `#C83232` |
| ![Aubergine](https://img.shields.io/badge/■■■■-63365F?style=flat-square&labelColor=63365F&color=63365F) | Aubergine | `#63365F` |
| ![Charcoal](https://img.shields.io/badge/■■■■-30343A?style=flat-square&labelColor=30343A&color=30343A) | Charcoal | `#30343A` |

**Two-ink recipes:** Powder Blue + Signal Red, Cobalt + Terracotta, Botanical Green + Oxblood, Charcoal + Signal Red, Electric Blue + Carbon, Mint Green + Charcoal, Ultramarine + Safety Orange, Cyan + Brick Red, and Tangerine + Slate Blue.

| Swatches | Two-ink recipe | Hex |
|---|---|---|
| ![Powder Blue](https://img.shields.io/badge/■-9EB8D3?style=flat-square&labelColor=9EB8D3&color=9EB8D3) ![Signal Red](https://img.shields.io/badge/■-C83232?style=flat-square&labelColor=C83232&color=C83232) | Powder Blue + Signal Red | `#9EB8D3` + `#C83232` |
| ![Cobalt](https://img.shields.io/badge/■-2148B8?style=flat-square&labelColor=2148B8&color=2148B8) ![Terracotta](https://img.shields.io/badge/■-C65F38?style=flat-square&labelColor=C65F38&color=C65F38) | Cobalt + Terracotta | `#2148B8` + `#C65F38` |
| ![Botanical Green](https://img.shields.io/badge/■-008A4B?style=flat-square&labelColor=008A4B&color=008A4B) ![Oxblood](https://img.shields.io/badge/■-8F3434?style=flat-square&labelColor=8F3434&color=8F3434) | Botanical Green + Oxblood | `#008A4B` + `#8F3434` |
| ![Charcoal](https://img.shields.io/badge/■-30343A?style=flat-square&labelColor=30343A&color=30343A) ![Signal Red](https://img.shields.io/badge/■-C83232?style=flat-square&labelColor=C83232&color=C83232) | Charcoal + Signal Red | `#30343A` + `#C83232` |
| ![Electric Blue](https://img.shields.io/badge/■-173AE3?style=flat-square&labelColor=173AE3&color=173AE3) ![Carbon](https://img.shields.io/badge/■-242321?style=flat-square&labelColor=242321&color=242321) | Electric Blue + Carbon | `#173AE3` + `#242321` |
| ![Mint Green](https://img.shields.io/badge/■-5EB783?style=flat-square&labelColor=5EB783&color=5EB783) ![Charcoal](https://img.shields.io/badge/■-302D2E?style=flat-square&labelColor=302D2E&color=302D2E) | Mint Green + Charcoal | `#5EB783` + `#302D2E` |
| ![Ultramarine](https://img.shields.io/badge/■-263E99?style=flat-square&labelColor=263E99&color=263E99) ![Safety Orange](https://img.shields.io/badge/■-E55D2B?style=flat-square&labelColor=E55D2B&color=E55D2B) | Ultramarine + Safety Orange | `#263E99` + `#E55D2B` |
| ![Cyan](https://img.shields.io/badge/■-159DDA?style=flat-square&labelColor=159DDA&color=159DDA) ![Brick Red](https://img.shields.io/badge/■-B64032?style=flat-square&labelColor=B64032&color=B64032) | Cyan + Brick Red | `#159DDA` + `#B64032` |
| ![Tangerine](https://img.shields.io/badge/■-E46C2D?style=flat-square&labelColor=E46C2D&color=E46C2D) ![Slate Blue](https://img.shields.io/badge/■-4773A5?style=flat-square&labelColor=4773A5&color=4773A5) | Tangerine + Slate Blue | `#E46C2D` + `#4773A5` |

In two-ink work, the dominant plate normally carries 70%–85% of the printed area. The accent plate carries 15%–30% and must have a specific job such as dates, annotations, selected objects, or overprint intersections. Paper is not a third color, and the darker color created where two plates overlap is not a third ink.

## Visual rules

1. **No more than two printing inks.** One ink is the default; two inks require distinct plate roles and a subject-driven reason.
2. **Paper stays visible.** The result is a printed page, not a digitally tinted monochrome wash.
3. **Mechanical reproduction leads.** Photographs become dots, grain, clipped highlights, ink pooling, and mild registration drift between plates.
4. **Silence has structure.** Empty paper occupies 25%–55% of the canvas and controls pacing.
5. **Type has tension.** The largest text is 5–12 times the microcopy size, using no more than three type voices.
6. **Identity stays intact.** Supplied people, objects, and scenes remain recognizable.
7. **References are grammar, not templates.** At least four structural variables change from every supplied reference.

## Not this

- not a full-color photograph with a monochrome filter
- not arbitrary two-color decoration or more than two printing plates
- not a glossy mockup, 3D render, gradient poster, or cinematic scene
- not a centered template, card grid, sticker collage, or decorative blob system
- not dense scrapbook grunge or torn-paper styling
- not marketing copy, invented branding, fake sponsors, URLs, or QR codes
- not a reconstruction of a reference poster or artist signature

## Install

Clone the repository into your Claude Code skills directory:

```bash
git clone https://github.com/yanliudesign/mono-color-skill.git \
	~/.claude/skills/mono-color
```

Restart Claude Code after installation. Other agent environments can load [`SKILL.md`](./SKILL.md) as the skill entry point.

## Try it

```text
Use mono-color to make a vertical poster about a midnight convenience store.
The exact headline is “still open”.
```

```text
Turn this portrait into a cobalt one-ink editorial zine cover.
Keep the person's identity and expression.
```

```text
Create a botanical-green risograph field note about ferns.
The title is “field note 07”.
```

```text
Create an Ultramarine + Safety Orange overprint poster about city cycling.
Let the bicycle and oversized title cross in selected areas.
```

```text
Turn this product into a Cyan + Brick Red repeated-object cover.
Keep one open zone for the title and factual microcopy.
```

## Delivery format

One run returns:

1. a generated raster image when image-generation tools are available;
2. the exact production-ready prompt used for generation;
3. a recipe naming the print mode, exact ink palette, layout family, type pairing, print process, and originality changes.

If image generation is unavailable, the skill returns the production-ready prompt and states the limitation.

## Repository layout

```text
mono-color-skill/
├── SKILL.md          # Trigger rules, visual system, workflow, and quality gate
├── README.md         # English documentation
├── README.zh.md      # 中文说明
└── evals/
		└── evals.json    # Representative trigger and output expectations
```

## Originality

This skill extracts system-level qualities such as palette, print process, spacing, hierarchy, and communication tone. It does not copy a reference's composition, wording, labels, logos, border system, or distinctive arrangement.

When a user supplies a photograph, the subject is preserved as content while the crop, screening, grid, type placement, and metadata treatment are newly constructed.

---

Created by [Dreameryanyan](https://www.linkedin.com/in/yanliudesign/) · [LinkedIn](https://www.linkedin.com/in/yanliudesign/) · [X](https://x.com/yanliudreamer)