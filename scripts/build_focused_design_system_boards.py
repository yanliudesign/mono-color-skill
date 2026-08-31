#!/usr/bin/env python3
import shutil
import subprocess
import sys
from pathlib import Path

from build_design_system_board import (
    COBALT,
    HAIRLINE,
    INK,
    MUTED,
    PAPER,
    ROOT,
    TERRACOTTA,
    WIDTH,
    draw_carrier_icon,
    draw_composition_preview,
    line,
    load,
    rect,
    text,
)


BOARD_HEIGHT = 2400
OUTPUTS = {
    "typography": ROOT / "examples" / "visual-system-typography.png",
    "color": ROOT / "examples" / "visual-system-color.png",
    "layout": ROOT / "examples" / "visual-system-layout.png",
    "style": ROOT / "examples" / "visual-system-style.png",
}


def header(parts: list[str], number: str, title: str, summary: str) -> None:
    parts.extend([
        text(90, 82, f"MONO-COLOR / SYSTEM {number}", 17, family="Courier New", weight=700, fill=COBALT, spacing=1.8),
        text(90, 164, title, 68, family="Helvetica Neue", weight=700),
        text(1710, 82, "GENERATED FROM CURRENT CATALOGS", 14, family="Courier New", fill=MUTED, anchor="end"),
        text(1710, 150, summary, 14, family="Courier New", fill=MUTED, anchor="end"),
        line(90, 210, 1710, 210, stroke=INK, width=4),
    ])


def footer(parts: list[str], source: str) -> None:
    parts.extend([
        line(90, BOARD_HEIGHT - 92, 1710, BOARD_HEIGHT - 92, stroke=INK, width=2),
        text(90, BOARD_HEIGHT - 54, f"SOURCE: {source}", 12, family="Courier New", fill=MUTED),
        text(1710, BOARD_HEIGHT - 54, "SYSTEM GRAMMAR, NOT A COMPOSITION TO TRACE", 12, family="Courier New", fill=MUTED, anchor="end"),
    ])


def svg(parts: list[str]) -> str:
    return "".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{BOARD_HEIGHT}" viewBox="0 0 {WIDTH} {BOARD_HEIGHT}">',
        rect(0, 0, WIDTH, BOARD_HEIGHT, fill=PAPER),
        *parts,
        "</svg>",
    ])


def build_typography() -> str:
    roles = load("typography.json")["roles"]
    samples = [
        ("somewhere, slowly", "Bodoni 72", "italic", 46),
        ("AFTER DARK", "Helvetica Neue", "normal", 48),
        ("FIELD NOTE 07", "Avenir Next Condensed", "normal", 44),
        ("07 / NORTH", "Courier New", "normal", 40),
        ("EDGE TITLE", "Helvetica Neue", "normal", 44),
        ("circle the useful part", "Bodoni 72", "italic", 38),
        ("STILL OPEN", "Helvetica Neue", "normal", 56),
    ]
    parts: list[str] = []
    header(parts, "01", "TYPOGRAPHY SYSTEM", f"{len(roles)} ROLES / ONE DISPLAY SKELETON PER IMAGE")
    parts.append(text(90, 278, "DISPLAY / SUPPORT / SCALE / BEHAVIOR", 15, family="Courier New", fill=MUTED))
    card_width = 780
    for index, (role, sample) in enumerate(zip(roles, samples)):
        row, column = divmod(index, 2)
        x = 90 + column * 820
        y = 338 + row * 470
        value, family, style, size = sample
        parts.append(text(x, y, f"0{index + 1}", 14, family="Courier New", weight=700, fill=COBALT))
        parts.append(text(x + 48, y, role["name"].upper(), 20, weight=600))
        parts.append(text(x + card_width, y, role["scale_ratio"], 13, family="Courier New", fill=MUTED, anchor="end"))
        parts.append(line(x, y + 26, x + card_width, y + 26, stroke=HAIRLINE, width=1))
        parts.append(text(x, y + 132, value, size, family=family, style=style, weight=700 if style == "normal" else 400, fill=COBALT if index in (1, 4, 6) else INK))
        parts.append(text(x, y + 208, "DISPLAY", 11, family="Courier New", fill=MUTED))
        parts.append(text(x + 116, y + 208, role["display"], 13))
        parts.append(text(x, y + 248, "SUPPORT", 11, family="Courier New", fill=MUTED))
        parts.append(text(x + 116, y + 248, role["support"], 13))
        parts.append(text(x, y + 298, role["behavior"][0], 13, fill=MUTED))
        parts.append(text(x, y + 326, role["behavior"][1], 13, fill=MUTED))
    footer(parts, "design-system/typography.json")
    return svg(parts)


def build_color() -> str:
    colors = load("colors.json")
    parts: list[str] = []
    header(parts, "02", "COLOR SYSTEM", f"{len(colors['inks'])} INKS / {len(colors['palettes'])} PALETTES / TWO-PLATE LIMIT")
    parts.append(text(90, 290, "01  SUBSTRATES", 24, weight=600))
    parts.append(line(90, 316, 1710, 316, stroke=INK, width=2))
    for index, substrate in enumerate(colors["substrates"]):
        x = 90 + index * 540
        parts.append(rect(x, 360, 490, 126, fill=substrate["hex"], stroke=HAIRLINE, stroke_width=1))
        parts.append(text(x, 520, substrate["name"].upper(), 15, weight=600))
        parts.append(text(x, 548, substrate["hex"], 12, family="Courier New", fill=MUTED))
    parts.append(text(90, 646, "02  INK LIBRARY", 24, weight=600))
    parts.append(line(90, 672, 1710, 672, stroke=INK, width=2))
    for index, ink in enumerate(colors["inks"]):
        row, column = divmod(index, 7)
        x = 90 + column * 232
        y = 714 + row * 202
        parts.append(rect(x, y, 202, 112, fill=ink["hex"]))
        parts.append(text(x, y + 140, ink["name"].upper(), 13, weight=600))
        parts.append(text(x, y + 164, ink["hex"], 11, family="Courier New", fill=MUTED))
    parts.append(text(90, 1380, "03  CONTROLLED PALETTES", 24, weight=600))
    parts.append(line(90, 1406, 1710, 1406, stroke=INK, width=2))
    ink_map = {ink["id"]: ink for ink in colors["inks"]}
    for index, palette in enumerate(colors["palettes"]):
        row, column = divmod(index, 5)
        x = 90 + column * 324
        y = 1452 + row * 330
        palette_inks = [ink_map[ink_id] for ink_id in palette["ink_ids"]]
        swatch_width = 280 / len(palette_inks)
        for swatch_index, ink in enumerate(palette_inks):
            parts.append(rect(x + swatch_index * swatch_width, y, swatch_width, 150, fill=ink["hex"]))
        parts.append(text(x, y + 184, palette["id"].removeprefix("palette_").upper(), 13, weight=600))
        parts.append(text(x, y + 212, palette["mode"].upper(), 11, family="Courier New", fill=MUTED))
        parts.append(text(x, y + 240, " + ".join(ink["name"] for ink in palette_inks), 12, fill=COBALT))
    footer(parts, "design-system/colors.json")
    return svg(parts)


def build_layout() -> str:
    compositions = load("compositions.json")["compositions"]
    parts: list[str] = []
    header(parts, "03", "LAYOUT SYSTEM", f"{len(compositions)} COMPOSITIONS / ONE FOCAL EVENT / ONE RELEASE ZONE")
    parts.append(text(90, 278, "SUBJECT MASS / ACTIVE PAPER / ANCHOR / TITLE RELATION", 15, family="Courier New", fill=MUTED))
    for index, composition in enumerate(compositions):
        row, column = divmod(index, 3)
        x = 90 + column * 540
        y = 344 + row * 615
        draw_composition_preview(parts, index, x, y)
        parts.append(text(x + 210, y + 25, f"0{index + 1}", 13, family="Courier New", weight=700, fill=COBALT))
        parts.append(text(x + 210, y + 55, composition["layout"].upper(), 16, weight=600))
        parts.append(text(x + 210, y + 87, composition["id"], 11, family="Courier New", fill=MUTED))
        parts.append(text(x + 210, y + 128, f"SUBJECT  {composition['dominant_subject_percent'][0]}-{composition['dominant_subject_percent'][1]}%", 12, family="Courier New"))
        parts.append(text(x + 210, y + 154, f"PAPER    {composition['empty_paper_percent'][0]}-{composition['empty_paper_percent'][1]}%", 12, family="Courier New"))
        parts.append(text(x + 210, y + 180, f"ANCHORS  {' / '.join(composition['anchors'])}", 12, family="Courier New"))
        parts.append(text(x, y + 275, composition["title_relation"], 13, fill=MUTED))
        parts.append(line(x, y + 305, x + 490, y + 305, stroke=HAIRLINE, width=1))
    footer(parts, "design-system/compositions.json")
    return svg(parts)


def build_style() -> str:
    imperfections = load("imperfections.json")
    carriers = load("carriers.json")["carriers"]
    parts: list[str] = []
    header(parts, "04", "STYLE SYSTEM", f"{len(imperfections['effects'])} CONTROLLED IMPERFECTIONS / {len(carriers)} PHYSICAL CARRIERS")
    parts.append(text(90, 290, "01  REPRODUCTION MECHANICS", 24, weight=600))
    parts.append(line(90, 316, 1710, 316, stroke=INK, width=2))
    effects = imperfections["effects"]
    for index, effect in enumerate(effects):
        x = 90 + index * 324
        y = 366
        parts.append(rect(x, y, 282, 248, fill="#FBF8F0", stroke=HAIRLINE, stroke_width=1))
        if index == 0:
            for level in range(7):
                parts.append(rect(x + 20 + level * 36, y + 34, 28, 126, fill=COBALT, stroke="none"))
                parts.append(rect(x + 20 + level * 36, y + 34, 28, 126 * (6 - level) / 7, fill=PAPER))
        elif index == 1:
            parts.append(rect(x + 35, y + 42, 210, 110, fill=TERRACOTTA))
            for gap in range(10):
                parts.append(rect(x + 35 + gap * 23, y + 40, 8, 8 + (gap % 3) * 5, fill=PAPER))
        elif index == 2:
            for row in range(8):
                for column in range(12):
                    radius = 2 + ((row + column) % 5)
                    parts.append(f'<circle cx="{x + 24 + column * 21}" cy="{y + 34 + row * 20}" r="{radius}" fill="{COBALT}"/>')
        elif index == 3:
            parts.append(f'<circle cx="{x + 126}" cy="{y + 101}" r="72" fill="{COBALT}"/>')
            parts.append(f'<circle cx="{x + 158}" cy="{y + 103}" r="62" fill="{TERRACOTTA}" fill-opacity="0.74"/>')
        else:
            parts.append(f'<path d="M {x + 24} {y + 130} Q {x + 104} {y + 30} {x + 244} {y + 112}" fill="none" stroke="{COBALT}" stroke-width="7" stroke-dasharray="110 24 70"/>')
        parts.append(text(x, y + 286, f"0{index + 1} / {effect['name'].upper()}", 13, weight=600))
        parts.append(text(x, y + 314, " / ".join(effect["applies_to"][:2]), 11, family="Courier New", fill=MUTED))
    parts.append(text(90, 820, "02  PHYSICAL CARRIERS", 24, weight=600))
    parts.append(line(90, 846, 1710, 846, stroke=INK, width=2))
    for index, carrier in enumerate(carriers):
        x = 90 + index * 230
        y = 910
        draw_carrier_icon(parts, index, x, y)
        parts.append(text(x, y + 180, carrier["name"].upper(), 13, weight=600))
        parts.append(text(x, y + 207, " / ".join(carrier["ratios"]), 11, family="Courier New", fill=COBALT))
        parts.append(text(x, y + 235, carrier["required_signals"][0], 11, fill=MUTED))
    parts.append(text(90, 1320, "03  MATERIAL QUALITY GATE", 24, weight=600))
    parts.append(line(90, 1346, 1710, 1346, stroke=INK, width=2))
    checks = [
        ("PAPER", "Substrate remains visible and active; never a flat digital wash."),
        ("EDGES", "Use bounded bleed, dry-edge breakup, or controlled registration drift."),
        ("IMAGE", "Apply one mechanical treatment while preserving recognition."),
        ("GESTURE", "Select exactly one family: loop, arrow, underline, or ruled grid."),
        ("LIMIT", "Never create an additional ink color or damage factual text."),
    ]
    for index, (label, description) in enumerate(checks):
        y = 1410 + index * 145
        parts.append(text(90, y, f"0{index + 1}", 13, family="Courier New", weight=700, fill=TERRACOTTA))
        parts.append(text(150, y, label, 14, family="Courier New", weight=700))
        parts.append(text(330, y, description, 17))
        parts.append(line(90, y + 38, 1710, y + 38, stroke=HAIRLINE, width=1))
    footer(parts, "design-system/imperfections.json + carriers.json")
    return svg(parts)


def main() -> None:
    renderer = shutil.which("rsvg-convert")
    if renderer is None:
        print("rsvg-convert is required to export the boards", file=sys.stderr)
        raise SystemExit(1)
    builders = {
        "typography": build_typography,
        "color": build_color,
        "layout": build_layout,
        "style": build_style,
    }
    for name, build in builders.items():
        output = OUTPUTS[name]
        subprocess.run(
            [renderer, "--format=png", f"--width={WIDTH}", f"--height={BOARD_HEIGHT}", "--output", str(output)],
            input=build().encode("utf-8"),
            check=True,
        )
        print(f"Exported {output} ({WIDTH}x{BOARD_HEIGHT})")


if __name__ == "__main__":
    main()