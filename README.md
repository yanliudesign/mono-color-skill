# mono-color

An agent skill for creating original monochrome editorial print images with warm paper, one chromatic ink, mechanical print texture, large negative space, and restrained typography.

## Install

Copy this repository into your agent's skills directory:

```sh
git clone https://github.com/yanliudesign/monocolor.git ~/.claude/skills/mono-color
```

Restart or reload your agent so it can discover `SKILL.md`.

## Usage

Ask for a monochrome editorial poster or name the skill directly:

```text
Use mono-color to make a vertical poster about a midnight convenience store.
```

The skill returns an image-generation prompt, a generated raster image when image tools are available, and a short production recipe.

## Contents

- `SKILL.md`: behavior, visual system, prompt compiler, and quality gate
- `evals/evals.json`: representative trigger and output expectations