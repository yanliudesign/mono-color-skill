#!/usr/bin/env python3
import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SYSTEM_DIR = ROOT / "design-system"
WIDTH = 1800
HEIGHT = 2400
PAPER = "#F4F0E7"
INK = "#242321"
MUTED = "#77736B"
RULE = "#C8C1B5"
BLUE = "#2148B8"
ROYAL = "#173AE3"
GREEN = "#008A4B"
MINT = "#5EB783"
ORANGE = "#C65F38"
SAFETY = "#E55D2B"
RED = "#C83232"
MAGENTA = "#D51F55"
CYAN = "#159DDA"
PURPLE = "#63365F"


def load(name):
    with (SYSTEM_DIR / name).open(encoding="utf-8") as source:
        return json.load(source)


def text(x, y, value, size, family="Avenir Next", weight=400, fill=INK, anchor="start",
         style="normal", spacing=0, transform=None):
    transform_attr = f' transform="{transform}"' if transform else ""
    return (
        f'<text x="{x}" y="{y}" font-family="{escape(family)}" font-size="{size}" '
        f'font-weight="{weight}" font-style="{style}" fill="{fill}" text-anchor="{anchor}" '
        f'letter-spacing="{spacing}"{transform_attr}>{escape(value)}</text>'
    )


def rect(x, y, width, height, fill="none", stroke="none", stroke_width=0, radius=0, opacity=1):
    return (
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" '
        f'fill="{fill}" fill-opacity="{opacity}" stroke="{stroke}" stroke-width="{stroke_width}"/>'
    )


def line(x1, y1, x2, y2, stroke=INK, width=2, dash=None):
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{width}"{dash_attr}/>'


def image_uri(path):
    return path.resolve().relative_to(ROOT).as_posix()


def image(parts, reference, x, y, width, height, clip_id):
    path = ROOT / reference["file"]
    parts.append(
        f'<defs><clipPath id="{clip_id}"><rect x="{x}" y="{y}" width="{width}" height="{height}"/></clipPath></defs>'
    )
    parts.append(
        f'<image x="{x}" y="{y}" width="{width}" height="{height}" href="{image_uri(path)}" '
        f'preserveAspectRatio="xMidYMid slice" clip-path="url(#{clip_id})"/>'
    )


def board_start(parts, index, title, subtitle, count_label):
    parts.extend([
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
        rect(0, 0, WIDTH, HEIGHT, fill=PAPER),
        text(90, 84, f"MONO-COLOR / SYSTEM {index}", 16, family="Courier New", weight=700, fill=BLUE, spacing=1.5),
        text(90, 166, title, 70, family="Helvetica Neue", weight=700),
        text(1710, 90, "DERIVED FROM 12 REFERENCES", 14, family="Courier New", fill=MUTED, anchor="end"),
        text(1710, 150, count_label, 13, family="Courier New", fill=MUTED, anchor="end"),
        line(90, 212, 1710, 212, width=4),
        text(90, 254, subtitle, 15, family="Courier New", fill=MUTED),
    ])


def section(parts, number, title, y, note=""):
    parts.append(text(90, y, number, 14, family="Courier New", weight=700, fill=BLUE))
    parts.append(text(140, y, title, 27, weight=600))
    if note:
        parts.append(text(1710, y, note, 13, family="Courier New", fill=MUTED, anchor="end"))
    parts.append(line(90, y + 22, 1710, y + 22, width=1))


def source_strip(parts, references, accent):
    y = 2118
    parts.append(text(90, y - 26, "SOURCE INDEX / ALL 12 REFERENCES", 13, family="Courier New", weight=700, fill=accent))
    cell_width = 124
    gap = 11
    for index, reference in enumerate(references):
        x = 90 + index * (cell_width + gap)
        image(parts, reference, x, y, cell_width, 150, f"source-{accent[1:]}-{index}")
        parts.append(rect(x, y, cell_width, 150, stroke=PAPER, stroke_width=3))
        parts.append(rect(x, y + 120, cell_width, 30, fill=INK, opacity=0.82))
        parts.append(text(x + 8, y + 141, reference["id"].upper(), 11, family="Courier New", weight=700, fill=PAPER))
    parts.append(line(90, 2320, 1710, 2320, width=2))
    parts.append(text(90, 2352, "OBSERVABLE GRAMMAR, NOT A COMPOSITION TO TRACE", 11, family="Courier New", fill=MUTED))
    parts.append(text(1710, 2352, "REFERENCE ANALYSIS / V0.2", 11, family="Courier New", fill=MUTED, anchor="end"))
    parts.append("</svg>")


def typography_board(references):
    parts = []
    board_start(parts, "01", "TYPOGRAPHY SYSTEM", "VOICE / SCALE / ORIENTATION / COLLISION", "6 VOICES · 4 SUPPORT LEVELS · 3 ORIENTATIONS")
    section(parts, "01", "SIX DISPLAY VOICES", 314, "EACH VOICE MAPS TO SPECIFIC SOURCE EVIDENCE")
    voices = [
        ("EDITORIAL SERIF", "somewhere, slowly", "Bodoni 72", "italic", 58, ORANGE, "REF 01 · 02 · 05"),
        ("NEO-GROTESK", "AFTER DARK", "Helvetica Neue", "normal", 58, BLUE, "REF 03 · 10 · 11"),
        ("CONDENSED / MODULAR", "FIELD NOTE 07", "Avenir Next Condensed", "normal", 52, RED, "REF 07 · 09 · 12"),
        ("MONOSPACED DATA", "SYSTEM / 07 / NORTH", "Courier New", "normal", 34, GREEN, "REF 01 · 04 · 06"),
        ("BLACKLETTER ACCENT", "ODD DAYS", "Luminari", "normal", 52, INK, "REF 04 ONLY · USE SPARINGLY"),
        ("HAND-DRAWN NOTE", "circle the useful part", "Bradley Hand", "normal", 43, CYAN, "REF 05 · 06"),
    ]
    for index, voice in enumerate(voices):
        row, column = divmod(index, 2)
        x = 90 + column * 815
        y = 374 + row * 318
        label, sample, family, style, size, color, refs = voice
        parts.append(text(x, y, f"0{index + 1}", 12, family="Courier New", weight=700, fill=BLUE))
        parts.append(text(x + 40, y, label, 14, family="Courier New", weight=700))
        parts.append(text(x + 780, y, refs, 11, family="Courier New", fill=MUTED, anchor="end"))
        parts.append(line(x, y + 18, x + 780, y + 18, stroke=RULE, width=1))
        parts.append(text(x, y + 102, sample, size, family=family, weight=700 if index in {1, 2} else 400, fill=color, style=style))
        if index == 2:
            parts.append(line(x, y + 123, x + 530, y + 123, stroke=color, width=5))
        if index == 5:
            parts.append(f'<ellipse cx="{x + 302}" cy="{y + 86}" rx="245" ry="62" fill="none" stroke="{color}" stroke-width="3" transform="rotate(-4 {x + 302} {y + 86})"/>')
        parts.append(text(x, y + 166, "DISPLAY", 11, family="Courier New", fill=MUTED))
        parts.append(text(x + 105, y + 166, "supporting label / factual tier", 14, family="Avenir Next", fill=INK))
        parts.append(text(x, y + 198, "MICRO", 11, family="Courier New", fill=MUTED))
        parts.append(text(x + 105, y + 198, "01. SOURCE / DATE / LOCATION", 12, family="Courier New", fill=MUTED))

    section(parts, "02", "HIERARCHY AND ORIENTATION", 1380, "SCALE IS THE PRIMARY CONTRAST")
    hierarchy = [
        ("DISPLAY", "7–20×", 72, BLUE),
        ("SUBHEAD", "2–4×", 30, INK),
        ("FACTS", "1×", 16, INK),
        ("MICROCOPY", "0.7×", 11, MUTED),
    ]
    for index, item in enumerate(hierarchy):
        x = 90 + index * 395
        label, ratio, size, color = item
        parts.append(text(x, 1462, ratio, 12, family="Courier New", weight=700, fill=BLUE))
        parts.append(text(x, 1544, "Aa", size, family="Helvetica Neue", weight=700, fill=color))
        parts.append(text(x, 1600, label, 13, family="Courier New", weight=700))
    parts.append(line(90, 1650, 1710, 1650, stroke=RULE, width=1))
    orientation = [
        ("HORIZONTAL", "default reading field", 90),
        ("VERTICAL", "edge anchor or collision", 620),
        ("ROTATED", "movement, never decoration", 1150),
    ]
    for index, (label, note, x) in enumerate(orientation):
        parts.append(text(x, 1710, f"0{index + 1} / {label}", 13, family="Courier New", weight=700, fill=BLUE))
        parts.append(rect(x, 1740, 430, 238, fill="#FAF7EF", stroke=RULE, stroke_width=1))
        if index == 0:
            parts.append(text(x + 28, 1848, "OPEN FIELD", 46, family="Helvetica Neue", weight=700))
            parts.append(text(x + 28, 1890, note, 13, family="Courier New", fill=MUTED))
        elif index == 1:
            parts.append(text(x + 55, 1938, "EDGE TITLE", 38, family="Avenir Next Condensed", weight=700, fill=RED,
                              transform=f"rotate(-90 {x + 55} 1938)"))
            parts.append(rect(x + 135, 1790, 240, 138, fill=BLUE, opacity=0.8))
        else:
            parts.append(text(x + 80, 1900, "MOVE", 55, family="Helvetica Neue", weight=700, fill=BLUE,
                              transform=f"rotate(-18 {x + 80} 1900)"))
            parts.append(text(x + 28, 1950, note, 13, family="Courier New", fill=MUTED))
    source_strip(parts, references, BLUE)
    return "\n".join(parts)


def color_board(references):
    parts = []
    board_start(parts, "02", "COLOR SYSTEM", "PAPER / PLATES / DENSITY / OVERPRINT", "8 DOMINANT INKS · 6 PAIRS · 1–2 PLATE LIMIT")
    section(parts, "01", "PAPER AND DOMINANT INKS", 314, "PAPER REMAINS AN ACTIVE THIRD COLOR")
    papers = [("WARM IVORY", "#F4F0E7"), ("COOL WHITE", "#F7F7F4"), ("PALE PINK", "#F5E4DF")]
    for index, (name, color) in enumerate(papers):
        x = 90 + index * 245
        parts.append(rect(x, 360, 220, 94, fill=color, stroke=RULE, stroke_width=1))
        parts.append(text(x, 480, name, 12, family="Courier New", weight=700))
        parts.append(text(x, 502, color, 11, family="Courier New", fill=MUTED))
    swatches = [
        ("COBALT", BLUE, "CITY / MUSIC"), ("BOTANICAL", GREEN, "NATURE / ARCHIVE"),
        ("TERRACOTTA", ORANGE, "TACTILE / CLASSICAL"), ("SIGNAL RED", RED, "EVENT / DECLARATION"),
        ("ROYAL BLUE", ROYAL, "YOUTH / MOVEMENT"), ("MINT", MINT, "JOURNAL / SOFT PHOTO"),
        ("AUBERGINE", PURPLE, "NIGHT / LITERATURE"), ("CHARCOAL", INK, "RESEARCH / PHOTO"),
    ]
    for index, (name, color, use) in enumerate(swatches):
        row, column = divmod(index, 4)
        x = 825 + column * 220
        y = 352 + row * 188
        parts.append(rect(x, y, 194, 94, fill=color))
        parts.append(text(x, y + 122, name, 12, family="Courier New", weight=700))
        parts.append(text(x, y + 145, use, 10, family="Courier New", fill=MUTED))

    section(parts, "02", "PROVEN TWO-INK PAIRS", 780, "SECOND PLATE MUST HAVE A DISTINCT ROLE")
    pairs = [
        ("COBALT + TERRACOTTA", BLUE, ORANGE, "TRAVEL / SUMMER", "REF 09 LOGIC"),
        ("CYAN + CORAL", CYAN, "#E25B5B", "ILLUSTRATION / MARKET", "REF 06"),
        ("POWDER BLUE + RED", "#9EB8D3", RED, "INFORMATION / FASHION", "REF 07"),
        ("ROYAL BLUE + BLACK", ROYAL, INK, "CULTURE / COLLAGE", "REF 05 · 08"),
        ("MAGENTA + TEAL", MAGENTA, "#008B82", "FOOD / PUBLIC EVENT", "REF 11"),
        ("VIOLET + ORANGE", "#5524D8", "#F1882A", "INSTITUTION / SPECIMEN", "REF 12"),
    ]
    for index, pair in enumerate(pairs):
        row, column = divmod(index, 3)
        x = 90 + column * 540
        y = 830 + row * 296
        label, first, second, use, refs = pair
        parts.append(rect(x, y, 224, 150, fill=first))
        parts.append(rect(x + 112, y, 224, 150, fill=second, opacity=0.78))
        parts.append(text(x, y + 184, label, 13, family="Courier New", weight=700))
        parts.append(text(x, y + 208, use, 11, family="Courier New", fill=MUTED))
        parts.append(text(x + 500, y + 208, refs, 10, family="Courier New", fill=BLUE, anchor="end"))

    section(parts, "03", "DENSITY IS NOT A NEW COLOR", 1472, "ONE PLATE CREATES A FULL TONAL RANGE")
    densities = [20, 35, 50, 70, 85, 100]
    for index, density in enumerate(densities):
        x = 90 + index * 270
        parts.append(rect(x, 1528, 232, 188, fill=BLUE, opacity=density / 100))
        parts.append(text(x, 1748, f"{density}%", 12, family="Courier New", weight=700))
    parts.append(text(90, 1812, "PLATE ROLE", 11, family="Courier New", fill=MUTED))
    parts.append(text(250, 1812, "20–35% atmosphere · 50–70% image · 85–100% display and rules", 15, family="Avenir Next"))
    parts.append(line(90, 1850, 1710, 1850, stroke=RULE, width=1))
    parts.append(text(90, 1906, "LIMIT", 11, family="Courier New", fill=MUTED))
    parts.append(text(250, 1906, "Never exceed two physical ink plates; the paper substrate does not count.", 15))
    parts.append(text(90, 1952, "OVERPRINT", 11, family="Courier New", fill=MUTED))
    parts.append(text(250, 1952, "Show one visible collision where both plates remain legible.", 15))
    source_strip(parts, references, RED)
    return "\n".join(parts)


def layout_preview(parts, index, x, y, width=210, height=280):
    parts.append(rect(x, y, width, height, fill="#FBF8F0", stroke=INK, stroke_width=1))
    if index == 0:
        parts.append(f'<ellipse cx="{x + 137}" cy="{y + 178}" rx="104" ry="122" fill="{BLUE}"/>')
        parts.append(rect(x + 18, y + 54, 165, 18, fill=INK))
    elif index == 1:
        parts.append(rect(x + 24, y + 58, 162, 150, fill=GREEN))
        parts.append(rect(x + 24, y + 224, 46, 20, fill=INK))
        parts.append(rect(x + 78, y + 224, 46, 20, fill=INK))
        parts.append(rect(x + 132, y + 224, 54, 20, fill=INK))
    elif index == 2:
        for vertical in (52, 105, 158):
            parts.append(line(x + vertical, y, x + vertical, y + height, stroke=RULE, width=1))
        for horizontal in (68, 136, 204):
            parts.append(line(x, y + horizontal, x + width, y + horizontal, stroke=RULE, width=1))
        parts.append(rect(x + 72, y + 76, 138, 116, fill=BLUE, opacity=0.72))
        parts.append(rect(x + 5, y + 136, 195, 25, fill=INK))
    elif index == 3:
        parts.append(f'<circle cx="{x + 106}" cy="{y + 88}" r="70" fill="{ORANGE}"/>')
        parts.append(rect(x + 12, y + 196, 188, 70, fill=ORANGE, opacity=0.58))
        for offset in range(0, 180, 16):
            parts.append(line(x + 12 + offset, y + 24, x + 12 + offset, y + 252, stroke=RED, width=1, dash="2 5"))
    elif index == 4:
        for row in range(3):
            parts.append(f'<ellipse cx="{x + 100}" cy="{y + 42 + row * 98}" rx="92" ry="46" fill="{INK}"/>')
        parts.append(f'<path d="M {x + 18} {y + 18} C {x + 170} {y + 35}, {x + 26} {y + 210}, {x + 196} {y + 255}" fill="none" stroke="{BLUE}" stroke-width="3"/>')
    elif index == 5:
        parts.append(f'<path d="M {x + 32} {y + 128} Q {x + 105} {y + 20} {x + 180} {y + 132} Q {x + 110} {y + 260} {x + 32} {y + 128}" fill="{RED}"/>')
        parts.append(rect(x + 36, y + 126, 138, 18, fill=BLUE))
        parts.append(rect(x + 22, y + 176, 62, 58, fill=BLUE, opacity=0.55))
    elif index == 6:
        parts.append(rect(x + 52, y + 40, 120, 152, fill="#9EB8D3"))
        parts.append(text(x + 48, y + 174, "STYLE", 36, family="Avenir Next Condensed", weight=700, fill=RED,
                          transform=f"rotate(-90 {x + 48} {y + 174})"))
        parts.append(rect(x + 18, y + 214, 78, 13, fill=RED))
        parts.append(rect(x + 108, y + 214, 70, 13, fill=RED))
    elif index == 7:
        parts.append(f'<ellipse cx="{x + 108}" cy="{y + 142}" rx="72" ry="116" fill="{BLUE}"/>')
        parts.append(rect(x + 28, y + 96, 160, 32, fill=INK, opacity=0.8))
        parts.append(text(x + 184, y + 238, "EDGE", 15, family="Courier New", weight=700, fill=BLUE,
                          transform=f"rotate(-90 {x + 184} {y + 238})"))
    else:
        widths = [46, 38, 52, 42, 48]
        cursor = x
        for column, block_width in enumerate(widths):
            parts.append(rect(cursor, y + (column % 2) * 42, block_width, height - (column % 2) * 42, fill=GREEN, opacity=0.74))
            cursor += block_width - 3
        parts.append(rect(x + 12, y + 110, 166, 44, fill=PAPER))


def layout_board(references):
    parts = []
    board_start(parts, "03", "LAYOUT SYSTEM", "ANCHOR / CROP / GRID / ORIENTATION / PAPER", "9 PATTERNS · 25–55% ACTIVE PAPER · 1 HERO")
    section(parts, "01", "NINE COMPOSITION PATTERNS", 314, "RECOMBINE THE LOGIC; DO NOT TRACE THE SOURCE")
    patterns = [
        ("EDGE-CROPPED HERO", "REF 01 · 09 · 11", "one object occupies 60–80%"),
        ("FRAMED IMAGE FIELD", "REF 02", "image 70%; credits form a footer"),
        ("RULED COLLISION GRID", "REF 03", "title crosses image and grid cells"),
        ("ARCHIVAL AXIS", "REF 04", "one geometric anchor above a specimen"),
        ("REPEATED OBJECT PATH", "REF 05", "objects repeat; one line connects them"),
        ("CENTRAL OVERPRINT", "REF 06 · 12", "two plates meet in one specimen"),
        ("VERTICAL TITLE FRAME", "REF 07", "title rotates beside a narrow image"),
        ("DIAGONAL HYBRID", "REF 08", "hero tilts; metadata holds the edges"),
        ("FRAGMENTED PHOTO FIELD", "REF 10", "paper knockouts split image columns"),
    ]
    for index, pattern in enumerate(patterns):
        row, column = divmod(index, 3)
        x = 90 + column * 540
        y = 366 + row * 548
        layout_preview(parts, index, x, y)
        parts.append(text(x + 240, y + 30, f"0{index + 1}", 12, family="Courier New", weight=700, fill=BLUE))
        parts.append(text(x + 240, y + 62, pattern[0], 14, weight=600))
        parts.append(text(x + 240, y + 91, pattern[1], 11, family="Courier New", fill=RED))
        parts.append(text(x + 240, y + 132, pattern[2], 13, fill=MUTED))
        parts.append(line(x + 240, y + 160, x + 500, y + 160, stroke=RULE, width=1))
        parts.append(text(x + 240, y + 194, "ANCHOR", 10, family="Courier New", fill=MUTED))
        parts.append(text(x + 330, y + 194, ["edge", "frame", "grid", "axis", "path", "center", "side", "diagonal", "field"][index], 12, family="Courier New"))
        parts.append(text(x + 240, y + 222, "TITLE", 10, family="Courier New", fill=MUTED))
        parts.append(text(x + 330, y + 222, ["split", "above", "crossing", "small", "spanning", "corner", "vertical", "rotated", "embedded"][index], 12, family="Courier New"))
        parts.append(text(x + 240, y + 250, "PAPER", 10, family="Courier New", fill=MUTED))
        parts.append(text(x + 330, y + 250, ["25–40%", "20–35%", "35–50%", "30–45%", "25–40%", "35–55%", "35–50%", "30–50%", "20–40%"][index], 12, family="Courier New"))
    source_strip(parts, references, GREEN)
    return "\n".join(parts)


def style_sample(parts, index, x, y, width=350, height=260):
    parts.append(rect(x, y, width, height, fill="#FBF8F0", stroke=RULE, stroke_width=1))
    if index == 0:
        for row in range(12):
            for column in range(17):
                radius = 2 + (column / 16) * 7
                parts.append(f'<circle cx="{x + 18 + column * 19}" cy="{y + 18 + row * 19}" r="{radius}" fill="{BLUE}"/>')
    elif index == 1:
        for offset in range(-120, 520, 14):
            parts.append(line(x + offset, y + 20, x + offset + 180, y + 240, stroke=RED, width=1))
        parts.append(f'<ellipse cx="{x + 180}" cy="{y + 130}" rx="112" ry="86" fill="none" stroke="{RED}" stroke-width="5"/>')
    elif index == 2:
        parts.append(f'<ellipse cx="{x + 148}" cy="{y + 124}" rx="118" ry="96" fill="{BLUE}"/>')
        parts.append(f'<ellipse cx="{x + 212}" cy="{y + 140}" rx="88" ry="78" fill="{ORANGE}" fill-opacity="0.72"/>')
    elif index == 3:
        for row in range(13):
            for column in range(18):
                gray = 48 + ((row * 17 + column * 29) % 80)
                parts.append(rect(x + column * 20, y + row * 20, 21, 21, fill=f"rgb({gray},{gray},{gray})", opacity=0.18))
        parts.append(rect(x + 28, y + 34, 204, 138, fill=INK, opacity=0.58))
    elif index == 4:
        for size in range(0, 115, 12):
            parts.append(rect(x + 58 - size / 4, y + 42 + size, 170 + size / 2, 14, fill=ORANGE, opacity=max(0.08, 0.9 - size / 130)))
        parts.append(f'<circle cx="{x + 178}" cy="{y + 82}" r="57" fill="{ORANGE}"/>')
    elif index == 5:
        for column in range(6):
            block_width = 42 + (column % 3) * 13
            parts.append(rect(x + column * 56, y + (column % 2) * 24, block_width, 230 - (column % 2) * 24, fill=GREEN, opacity=0.7))
        parts.append(rect(x + 40, y + 92, 250, 54, fill=PAPER))
    elif index == 6:
        parts.append(f'<path d="M {x + 30} {y + 168} C {x + 88} {y + 22}, {x + 230} {y + 238}, {x + 320} {y + 78}" fill="none" stroke="{CYAN}" stroke-width="4"/>')
        parts.append(f'<ellipse cx="{x + 214}" cy="{y + 104}" rx="92" ry="46" fill="none" stroke="{CYAN}" stroke-width="3" transform="rotate(-8 {x + 214} {y + 104})"/>')
        parts.append(text(x + 98, y + 120, "NOTE", 28, family="Bradley Hand", fill=CYAN))
    else:
        for offset in range(18, 330, 28):
            parts.append(line(x + offset, y + 25, x + offset, y + 220, stroke=RED, width=1, dash="2 6"))
        parts.append(rect(x + 26, y + 28, 130, 20, fill=RED))
        parts.append(text(x + 26, y + 86, "SYSTEM / 07", 16, family="Courier New", weight=700, fill=RED))
        parts.append(rect(x + 26, y + 178, 296, 48, stroke=RED, stroke_width=2))


def style_board(references):
    parts = []
    board_start(parts, "04", "STYLE SYSTEM", "IMAGE MECHANICS / PAPER / GESTURE / IMPERFECTION", "8 PROCESSES · 1 GESTURE FAMILY · ANALOG OUTPUT")
    section(parts, "01", "EIGHT REPRODUCTION MECHANICS", 314, "THE STYLE COMES FROM PROCESS, NOT RETRO PROPS")
    processes = [
        ("COARSE HALFTONE", "REF 01 · 05 · 11", "dots remain visible at viewing size"),
        ("LINE ENGRAVING", "REF 06 · 09 · 12", "contours are built from irregular lines"),
        ("VISIBLE OVERPRINT", "REF 06 · 09", "plates overlap with transparent tension"),
        ("PHOTOCOPY GRAIN", "REF 01 · 03 · 04", "paper and image carry uneven noise"),
        ("PIXEL DISSOLVE", "REF 04", "solid image breaks into square debris"),
        ("PAPER KNOCKOUT", "REF 10", "blank paper cuts active silhouettes"),
        ("MANUAL ANNOTATION", "REF 05 · 06", "one loop, arrow, or speech bubble family"),
        ("ARCHIVAL OVERLAY", "REF 03 · 04 · 07", "rules and data index the image"),
    ]
    for index, process in enumerate(processes):
        row, column = divmod(index, 4)
        x = 90 + column * 405
        y = 372 + row * 570
        style_sample(parts, index, x, y)
        parts.append(text(x, y + 298, f"0{index + 1} / {process[0]}", 13, family="Courier New", weight=700))
        parts.append(text(x, y + 327, process[1], 11, family="Courier New", fill=BLUE))
        parts.append(text(x, y + 363, process[2], 12, fill=MUTED))

    section(parts, "02", "MATERIAL QUALITY GATE", 1548, "IMPERFECT DOES NOT MEAN UNCONTROLLED")
    gates = [
        ("PAPER", "visible fiber or tooth; never a flat digital wash"),
        ("EDGES", "slight bleed, soft registration, or dry-ink breakup"),
        ("IMAGE", "one mechanical treatment only; preserve recognition"),
        ("GESTURE", "exactly one family: loop, arrow, underline, or ruled grid"),
        ("AVOID", "gradients, glossy 3D, cinematic haze, sticker decoration"),
    ]
    for index, (label, rule) in enumerate(gates):
        y = 1612 + index * 82
        parts.append(text(90, y, f"0{index + 1}", 11, family="Courier New", weight=700, fill=RED))
        parts.append(text(145, y, label, 13, family="Courier New", weight=700))
        parts.append(text(330, y, rule, 15))
        parts.append(line(90, y + 27, 1710, y + 27, stroke=RULE, width=1))
    source_strip(parts, references, ORANGE)
    return "\n".join(parts)


def export(svg, output, renderer, width):
    output.parent.mkdir(parents=True, exist_ok=True)
    height = int(HEIGHT * width / WIDTH)
    with tempfile.NamedTemporaryFile(suffix=".svg", dir=ROOT) as source:
        source.write(svg.encode("utf-8"))
        source.flush()
        subprocess.run(
            [renderer, "--format=png", f"--width={width}", f"--height={height}", "--output", str(output), source.name],
            check=True,
        )
    print(f"Exported {output} ({width}x{height})")


def main():
    parser = argparse.ArgumentParser(description="Build four visual-system boards from all twelve references.")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "examples")
    parser.add_argument("--width", type=int, default=WIDTH)
    args = parser.parse_args()
    renderer = shutil.which("rsvg-convert")
    if renderer is None:
        print("rsvg-convert is required", file=sys.stderr)
        raise SystemExit(1)

    references = load("reference-analysis.json")["references"]
    boards = {
        "visual-system-typography.png": typography_board(references),
        "visual-system-color.png": color_board(references),
        "visual-system-layout.png": layout_board(references),
        "visual-system-style.png": style_board(references),
    }
    output_dir = args.output_dir.expanduser().resolve()
    for filename, svg in boards.items():
        export(svg, output_dir / filename, renderer, args.width)


if __name__ == "__main__":
    main()