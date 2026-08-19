<div align="center">

[中文](./README.zh.md) · **English**

# Monocolor Editorial Print

**A one-ink editorial image skill for posters, zines, portraits, and visual field notes.**

[![Version](https://img.shields.io/badge/VERSION-1.0.0-2ea44f?style=flat-square&labelColor=333)](./SKILL.md)
[![Skills](https://img.shields.io/badge/SKILLS-1-2ea44f?style=flat-square&labelColor=333)](./SKILL.md)
[![Stars](https://img.shields.io/github/stars/yanliudesign/monocolor?style=flat-square&label=STARS&color=e37f2c&labelColor=333)](https://github.com/yanliudesign/monocolor/stargazers)

[![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-d97757?style=flat-square&labelColor=1a1a1a&logo=anthropic&logoColor=white)](https://claude.ai/code)
[![SKILL.md](https://img.shields.io/badge/Agent-SKILL.md-214f9b?style=flat-square&labelColor=1a1a1a)](./SKILL.md)

</div>

Turn a theme, sentence, object, or supplied photograph into an original monochrome editorial print. The skill combines warm paper, exactly one chromatic ink, screened imagery, active negative space, and a sharp serif-to-utility type contrast.

It preserves a visual system rather than copying a reference. Every composition is rebuilt around the subject, intent, words, and image role.

## What it does

| System | Direction |
|---|---|
| **Input** | A theme, phrase, object, article idea, or supplied photograph |
| **Palette** | Warm uncoated paper + exactly one cobalt or botanical-green ink |
| **Image** | Halftone, risograph grain, cyanotype exposure, or photocopy breakup |
| **Space** | 25%–55% visible empty paper on an asymmetric editorial grid |
| **Type** | Serif editorial voice + condensed sans or monospaced utility voice |
| **Output** | Generated raster image, exact production prompt, and a short recipe |

## How it works

```text
1  Read the input       →  identify subject, intent, words, and image role
2  Choose the layout    →  image field, specimen, declaration, information, plate, or cover
3  Build one-ink depth  →  use dot density and paper instead of extra colors
4  Compose the page     →  preserve 25%–55% silence and add one deliberate disruption
5  Generate and inspect →  check ink count, identity, hierarchy, texture, and originality
```

## Visual rules

1. **One chromatic ink only.** Cobalt is the default; botanical green is a subject-driven alternative, never a second color.
2. **Paper stays visible.** The result is a printed page, not a digitally tinted monochrome wash.
3. **Mechanical reproduction leads.** Photographs become dots, grain, clipped highlights, ink pooling, and mild registration drift.
4. **Silence has structure.** Empty paper occupies 25%–55% of the canvas and controls pacing.
5. **Type has tension.** The largest text is 5–12 times the microcopy size, using no more than three type voices.
6. **Identity stays intact.** Supplied people, objects, and scenes remain recognizable.
7. **References are grammar, not templates.** At least four structural variables change from every supplied reference.

## Not this

- not a full-color photograph with a monochrome filter
- not a glossy mockup, 3D render, gradient poster, or cinematic scene
- not a centered template, card grid, sticker collage, or decorative blob system
- not dense scrapbook grunge or torn-paper styling
- not marketing copy, invented branding, fake sponsors, URLs, or QR codes
- not a reconstruction of a reference poster or artist signature

## Install

Clone the repository into your Claude Code skills directory:

```bash
git clone https://github.com/yanliudesign/monocolor.git \
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

## Delivery format

One run returns:

1. a generated raster image when image-generation tools are available;
2. the exact production-ready prompt used for generation;
3. a recipe naming the ink, layout family, type pairing, print process, and originality changes.

If image generation is unavailable, the skill returns the production-ready prompt and states the limitation.

## Repository layout

```text
monocolor/
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