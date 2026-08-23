#!/usr/bin/env python3
import argparse
import json
import shutil
import subprocess
import sys
from html import escape
from pathlib import Path
from typing import Optional


ROOT = Path(__file__).resolve().parents[1]
SYSTEM_DIR = ROOT / "design-system"
WIDTH = 1800
HEIGHT = 3000
PAPER = "#F5F1E8"
INK = "#242321"
COBALT = "#2148B8"
TERRACOTTA = "#C65F38"
MUTED = "#77736B"
HAIRLINE = "#C8C1B5"


def load(name: str) -> dict:
    with (SYSTEM_DIR / name).open(encoding="utf-8") as source:
        return json.load(source)


def text(x: float, y: float, value: str, size: int, *, family: str = "Avenir Next", weight: int = 400,
         fill: str = INK, anchor: str = "start", style: str = "normal", spacing: float = 0) -> str:
    return (
        f'<text x="{x}" y="{y}" font-family="{escape(family)}" font-size="{size}" '
        f'font-weight="{weight}" font-style="{style}" fill="{fill}" text-anchor="{anchor}" '
        f'letter-spacing="{spacing}">{escape(value)}</text>'
    )


def line(x1: float, y1: float, x2: float, y2: float, *, stroke: str = INK, width: float = 2,
         dash: Optional[str] = None) -> str:
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{width}"{dash_attr}/>'


def rect(x: float, y: float, width: float, height: float, *, fill: str = "none", stroke: str = "none",
         stroke_width: float = 0, radius: float = 0) -> str:
    return (
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"/>'
    )


def section_header(parts: list[str], number: str, title: str, subtitle: str, y: int) -> None:
    parts.append(text(90, y, number, 17, family="Courier New", weight=700, fill=COBALT, spacing=1.2))
    parts.append(text(154, y, title, 34, weight=600))
    parts.append(text(1710, y, subtitle, 16, family="Courier New", fill=MUTED, anchor="end"))
    parts.append(line(90, y + 28, 1710, y + 28, stroke=INK, width=2))


def draw_palette(parts: list[str], colors: dict) -> None:
    inks = colors["inks"]
    columns = 10
    cell_width = 162
    swatch_width = 142
    start_y = 328
    for index, ink in enumerate(inks):
        row, column = divmod(index, columns)
        x = 90 + column * cell_width
        y = start_y + row * 178
        parts.append(rect(x, y, swatch_width, 92, fill=ink["hex"]))
        parts.append(text(x, y + 116, ink["name"].upper(), 13, weight=600))
        short_id = ink["id"].removeprefix("ink_")
        parts.append(text(x, y + 138, short_id, 12, family="Courier New", fill=MUTED))
        parts.append(text(x, y + 158, ink["hex"], 12, family="Courier New", fill=MUTED))


def draw_typography(parts: list[str], typography: dict) -> None:
    samples = [
        ("type_poetic", "SOMEWHERE, SLOWLY", "Bodoni 72", "italic", 44),
        ("type_civic", "OPEN / AFTER DARK", "Helvetica Neue", "normal", 40),
        ("type_archival", "FIELD NOTE 07", "Avenir Next Condensed", "normal", 38),
        ("type_typographic", "STILL OPEN", "Helvetica Neue", "normal", 52),
    ]
    role_map = {role["id"]: role for role in typography["roles"]}
    card_width = 390
    for index, (role_id, sample, family, font_style, size) in enumerate(samples):
        x = 90 + index * 405
        y = 866
        role = role_map[role_id]
        parts.append(text(x, y, f"0{index + 1}", 13, family="Courier New", weight=700, fill=COBALT))
        parts.append(text(x + 40, y, role_id, 13, family="Courier New", fill=MUTED))
        parts.append(line(x, y + 20, x + card_width, y + 20, stroke=HAIRLINE, width=1))
        if role_id == "type_poetic":
            parts.append(text(x, y + 100, "SOMEWHERE,", size, family=family, style=font_style))
            parts.append(text(x + 70, y + 147, "SLOWLY", size, family=family, style=font_style, fill=TERRACOTTA))
        elif role_id == "type_civic":
            parts.append(text(x, y + 105, "OPEN", size, family=family, weight=700))
            parts.append(rect(x + 3, y + 119, 270, 12, fill=COBALT))
            parts.append(text(x + 25, y + 169, "AFTER DARK", 29, family="Avenir Next Condensed", weight=600))
        elif role_id == "type_archival":
            parts.append(text(x, y + 102, sample, size, family=family, weight=500))
            parts.append(line(x, y + 125, x + 340, y + 125, stroke=INK, width=1))
            parts.append(text(x, y + 153, "SPECIMEN / 07 / NORTH", 13, family="Courier New", fill=MUTED))
        else:
            parts.append(text(x - 2, y + 103, "STILL", size, family=family, weight=700))
            parts.append(text(x + 78, y + 162, "OPEN", size, family=family, weight=700, fill=COBALT))
        parts.append(text(x, y + 222, role["name"].upper(), 15, weight=600))
        parts.append(text(x, y + 247, role["scale_ratio"], 12, family="Courier New", fill=MUTED))
        parts.append(text(x, y + 275, role["behavior"][0], 13, fill=MUTED))


def poster_base(parts: list[str], x: float, y: float) -> None:
    parts.append(rect(x, y, 180, 226, fill="#FBF8F0", stroke=INK, stroke_width=1))


def draw_composition_preview(parts: list[str], index: int, x: float, y: float) -> None:
    poster_base(parts, x, y)
    if index == 0:
        parts.append(f'<ellipse cx="{x + 118}" cy="{y + 146}" rx="88" ry="101" fill="{COBALT}"/>')
        parts.append(rect(x + 18, y + 55, 148, 16, fill=INK))
    elif index == 1:
        parts.append(f'<circle cx="{x + 90}" cy="{y + 119}" r="48" fill="{TERRACOTTA}"/>')
        parts.append(line(x + 22, y + 58, x + 67, y + 96, stroke=INK, width=1))
        parts.append(line(x + 117, y + 144, x + 158, y + 178, stroke=INK, width=1))
    elif index == 2:
        parts.append(text(x + 12, y + 78, "BIG", 62, family="Helvetica Neue", weight=700))
        parts.append(text(x + 42, y + 143, "TYPE", 58, family="Helvetica Neue", weight=700, fill=COBALT))
        parts.append(rect(x + 12, y + 184, 78, 18, fill=TERRACOTTA))
    elif index == 3:
        for offset in (52, 90, 128, 166):
            parts.append(line(x + 16, y + offset, x + 164, y + offset, stroke=INK, width=1))
        parts.append(rect(x + 16, y + 18, 95, 22, fill=COBALT))
        parts.append(rect(x + 112, y + 92, 50, 72, fill=TERRACOTTA))
    elif index == 4:
        parts.append(rect(x + 48, y + 51, 84, 112, fill=INK))
        parts.append(line(x + 20, y + 35, x + 60, y + 72, stroke=COBALT, width=2))
        parts.append(line(x + 120, y + 153, x + 159, y + 190, stroke=COBALT, width=2))
        parts.append(text(x + 18, y + 208, "PLATE 04", 11, family="Courier New"))
    elif index == 5:
        parts.append(rect(x + 56, y + 35, 124, 191, fill=COBALT))
        parts.append(rect(x + 14, y + 96, 150, 23, fill=INK))
        parts.append(rect(x + 14, y + 126, 112, 23, fill=INK))
    elif index == 6:
        for row in range(4):
            for column in range(3):
                color = COBALT if (row + column) % 2 == 0 else TERRACOTTA
                parts.append(f'<circle cx="{x + 42 + column * 49}" cy="{y + 48 + row * 44}" r="18" fill="{color}"/>')
        parts.append(rect(x + 18, y + 202, 112, 10, fill=INK))
    elif index == 7:
        parts.append(f'<ellipse cx="{x + 76}" cy="{y + 110}" rx="62" ry="86" fill="{COBALT}"/>')
        parts.append(f'<ellipse cx="{x + 122}" cy="{y + 129}" rx="48" ry="73" fill="{TERRACOTTA}" fill-opacity="0.78"/>')
        parts.append(rect(x + 25, y + 107, 132, 17, fill=INK))
    else:
        parts.append(rect(x + 18, y + 22, 82, 102, fill=COBALT))
        for offset in (143, 163, 183):
            parts.append(line(x + 18, y + offset, x + 158, y + offset, stroke=INK, width=1))
        parts.append(text(x + 113, y + 37, "07", 12, family="Courier New", fill=TERRACOTTA))


def draw_compositions(parts: list[str], compositions: dict) -> None:
    for index, composition in enumerate(compositions["compositions"]):
        row, column = divmod(index, 3)
        x = 90 + column * 540
        y = 1438 + row * 290
        draw_composition_preview(parts, index, x, y)
        label_x = x + 206
        parts.append(text(label_x, y + 28, f"0{index + 1}", 13, family="Courier New", weight=700, fill=COBALT))
        parts.append(text(label_x, y + 58, composition["layout"].upper(), 15, weight=600))
        parts.append(text(label_x, y + 88, composition["id"], 11, family="Courier New", fill=MUTED))
        subject = composition["dominant_subject_percent"]
        paper = composition["empty_paper_percent"]
        parts.append(text(label_x, y + 124, f"SUBJECT  {subject[0]}-{subject[1]}%", 12, family="Courier New"))
        parts.append(text(label_x, y + 148, f"PAPER    {paper[0]}-{paper[1]}%", 12, family="Courier New"))
        parts.append(text(label_x, y + 184, composition["title_relation"], 12, fill=MUTED))


def draw_carrier_icon(parts: list[str], index: int, x: float, y: float) -> None:
    if index == 0:
        parts.append(rect(x + 32, y + 12, 94, 126, fill="#FBF8F0", stroke=INK, stroke_width=2))
        parts.append(f'<circle cx="{x + 39}" cy="{y + 19}" r="4" fill="{TERRACOTTA}"/>')
        parts.append(f'<circle cx="{x + 119}" cy="{y + 19}" r="4" fill="{TERRACOTTA}"/>')
        parts.append(rect(x + 46, y + 36, 66, 56, fill=COBALT))
    elif index == 1:
        parts.append(f'<path d="M {x + 12} {y + 32} Q {x + 48} {y + 20} {x + 80} {y + 39} L {x + 80} {y + 138} Q {x + 48} {y + 120} {x + 12} {y + 132} Z" fill="#FBF8F0" stroke="{INK}" stroke-width="2"/>')
        parts.append(f'<path d="M {x + 148} {y + 32} Q {x + 112} {y + 20} {x + 80} {y + 39} L {x + 80} {y + 138} Q {x + 112} {y + 120} {x + 148} {y + 132} Z" fill="#FBF8F0" stroke="{INK}" stroke-width="2"/>')
        parts.append(line(x + 80, y + 39, x + 80, y + 138, stroke=TERRACOTTA, width=3))
    elif index == 2:
        parts.append(rect(x + 45, y + 6, 72, 142, fill="#FBF8F0", stroke=INK, stroke_width=3, radius=10))
        parts.append(rect(x + 52, y + 28, 58, 92, fill=COBALT))
        parts.append(f'<circle cx="{x + 81}" cy="{y + 136}" r="4" fill="{INK}"/>')
    elif index == 3:
        parts.append(rect(x + 20, y + 12, 124, 124, fill=TERRACOTTA, stroke=INK, stroke_width=2))
        parts.append(f'<circle cx="{x + 82}" cy="{y + 74}" r="36" fill="none" stroke="{PAPER}" stroke-width="10"/>')
        parts.append(f'<circle cx="{x + 82}" cy="{y + 74}" r="5" fill="{INK}"/>')
    elif index == 4:
        parts.append(f'<path d="M {x + 36} {y + 31} L {x + 101} {y + 10} L {x + 137} {y + 39} L {x + 137} {y + 127} L {x + 71} {y + 147} L {x + 36} {y + 118} Z" fill="#FBF8F0" stroke="{INK}" stroke-width="2"/>')
        parts.append(line(x + 71, y + 59, x + 137, y + 39, stroke=TERRACOTTA, width=3))
        parts.append(line(x + 71, y + 59, x + 71, y + 147, stroke=INK, width=2))
    elif index == 5:
        parts.append(f'<path d="M {x + 50} {y + 18} L {x + 21} {y + 47} L {x + 45} {y + 70} L {x + 45} {y + 141} L {x + 117} {y + 141} L {x + 117} {y + 70} L {x + 141} {y + 47} L {x + 112} {y + 18} L {x + 98} {y + 38} Q {x + 81} {y + 50} {x + 64} {y + 38} Z" fill="#FBF8F0" stroke="{INK}" stroke-width="2"/>')
        parts.append(rect(x + 62, y + 75, 38, 30, fill=COBALT))
    else:
        parts.append(rect(x + 18, y + 31, 70, 104, fill="#FBF8F0", stroke=INK, stroke_width=2))
        parts.append(rect(x + 72, y + 12, 72, 104, fill="#FBF8F0", stroke=INK, stroke_width=2))
        parts.append(rect(x + 85, y + 28, 46, 53, fill=COBALT))
        parts.append(line(x + 100, y + 123, x + 144, y + 123, stroke=TERRACOTTA, width=3))


def draw_carriers(parts: list[str], carriers: dict) -> None:
    for index, carrier in enumerate(carriers["carriers"]):
        x = 90 + index * 230
        y = 2685
        draw_carrier_icon(parts, index, x, y)
        parts.append(text(x, y + 177, carrier["name"].upper(), 13, weight=600))
        parts.append(text(x, y + 201, carrier["id"].removeprefix("carrier_"), 11, family="Courier New", fill=MUTED))
        parts.append(text(x, y + 225, " / ".join(carrier["ratios"]), 11, family="Courier New", fill=COBALT))


def build_svg() -> str:
    colors = load("colors.json")
    typography = load("typography.json")
    compositions = load("compositions.json")
    carriers = load("carriers.json")

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
        rect(0, 0, WIDTH, HEIGHT, fill=PAPER),
        text(90, 92, "MONO-COLOR", 18, family="Courier New", weight=700, fill=COBALT, spacing=2),
        text(90, 168, "VISUAL SYSTEM", 72, family="Helvetica Neue", weight=700),
        text(1710, 94, "REFERENCE BOARD / V0.1", 15, family="Courier New", fill=MUTED, anchor="end"),
        text(1710, 156, "19 INKS · 4 TYPE ROLES · 9 COMPOSITIONS · 7 CARRIERS", 14, family="Courier New", fill=MUTED, anchor="end"),
        line(90, 214, 1710, 214, stroke=INK, width=4),
    ]

    section_header(parts, "01", "INK LIBRARY", "SOLID PLATES / WARM PAPER", 276)
    draw_palette(parts, colors)
    section_header(parts, "02", "TYPOGRAPHIC ROLES", "DISPLAY / SUPPORT / BEHAVIOR", 802)
    draw_typography(parts, typography)
    section_header(parts, "03", "COMPOSITION GRAMMAR", "SUBJECT MASS / PAPER / COLLISION", 1374)
    draw_compositions(parts, compositions)
    section_header(parts, "04", "PHYSICAL CARRIERS", "FORMAT MUST REMAIN VISIBLE", 2618)
    draw_carriers(parts, carriers)
    parts.extend([
        line(90, 2940, 1710, 2940, stroke=INK, width=2),
        text(90, 2972, "SOURCE: design-system/*.json", 12, family="Courier New", fill=MUTED),
        text(1710, 2972, "ONE OR TWO INKS. ACTIVE PAPER. ONE CONTROLLED GESTURE.", 12, family="Courier New", fill=MUTED, anchor="end"),
        "</svg>",
    ])
    return "".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser(description="Export the mono-color visual system as one PNG board.")
    parser.add_argument("--output", type=Path, default=ROOT / "examples" / "mono-color-design-system-board.png")
    parser.add_argument("--width", type=int, default=WIDTH)
    args = parser.parse_args()

    renderer = shutil.which("rsvg-convert")
    if renderer is None:
        print("rsvg-convert is required to export the board", file=sys.stderr)
        raise SystemExit(1)

    output = args.output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    scale = args.width / WIDTH
    subprocess.run(
        [renderer, "--format=png", f"--width={args.width}", f"--height={int(HEIGHT * scale)}", "--output", str(output)],
        input=build_svg().encode("utf-8"),
        check=True,
    )
    print(f"Exported {output} ({args.width}x{int(HEIGHT * scale)})")


if __name__ == "__main__":
    main()