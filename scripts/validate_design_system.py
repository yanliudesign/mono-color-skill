#!/usr/bin/env python3
import json
import re
import struct
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SYSTEM_DIR = ROOT / "design-system"
HEX_COLOR = re.compile(r"^#[0-9A-F]{6}$")
RATIO = re.compile(r"^[1-9][0-9]*:[1-9][0-9]*$")
EXPECTED_FILES = {
    "colors.json",
    "typography.json",
    "compositions.json",
    "carriers.json",
    "imperfections.json",
    "rhythm.json",
}
EXPECTED_BOARDS = {
    "mono-color-design-system-board.png": (1800, 3000),
    "reference-system-v2-typography.png": (4629, 5211),
    "reference-system-v2-color.png": (4614, 5220),
    "reference-system-v2-layout.png": (4611, 5220),
    "reference-system-v2-style.png": (4608, 5211),
}
EXPECTED_REFERENCES = {
    *(f"reference-{index:02d}.png" for index in range(1, 11)),
    "reference-11.jpg",
    "reference-12.jpg",
}


def fail(message: str) -> None:
    print(f"design-system validation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def load(name: str) -> dict:
    path = SYSTEM_DIR / name
    if not path.exists():
        fail(f"missing {name}")
    with path.open(encoding="utf-8") as source:
        data = json.load(source)
    if data.get("schema_version") != 1:
        fail(f"{name} must use schema_version 1")
    return data


def require_unique(items: list[dict], label: str) -> set[str]:
    ids = [item.get("id") for item in items]
    if any(not isinstance(item_id, str) or not item_id for item_id in ids):
        fail(f"every {label} needs a non-empty id")
    if len(ids) != len(set(ids)):
        fail(f"{label} ids must be unique")
    return set(ids)


def png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as image:
        header = image.read(24)
    if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        fail(f"{path.name} must be a valid PNG")
    return struct.unpack(">II", header[16:24])


actual_files = {path.name for path in SYSTEM_DIR.glob("*.json")}
if actual_files != EXPECTED_FILES:
    fail(f"expected catalog files {sorted(EXPECTED_FILES)}, found {sorted(actual_files)}")

for board_name, expected_dimensions in EXPECTED_BOARDS.items():
    board_path = ROOT / "examples" / board_name
    if not board_path.exists():
        fail(f"missing generated board {board_name}")
    if png_dimensions(board_path) != expected_dimensions:
        fail(f"{board_name} must be {expected_dimensions[0]}x{expected_dimensions[1]}")

missing_references = [
    name for name in sorted(EXPECTED_REFERENCES)
    if not (ROOT / "examples" / name).is_file()
]
if missing_references:
    fail(f"missing visual references {missing_references}")

colors = load("colors.json")
typography = load("typography.json")
compositions = load("compositions.json")
carriers = load("carriers.json")
imperfections = load("imperfections.json")
rhythm = load("rhythm.json")

substrates = colors.get("substrates", [])
substrate_ids = require_unique(substrates, "substrate")
if len(substrates) < 3:
    fail("colors need at least white, gray, and pale-beige substrates")
for substrate in substrates:
    if not HEX_COLOR.fullmatch(substrate.get("hex", "")) or substrate.get("counts_as_ink") is not False:
        fail(f"{substrate['id']} must use an uppercase hex color and must not count as ink")
    if not substrate.get("use_for"):
        fail(f"{substrate['id']} needs selection guidance")

inks = colors.get("inks", [])
ink_ids = require_unique(inks, "ink")
if any(not HEX_COLOR.fullmatch(ink.get("hex", "")) for ink in inks):
    fail("every ink must use an uppercase hex color")

palettes = colors.get("palettes", [])
palette_ids = require_unique(palettes, "palette")
defaults = colors.get("defaults", {})
if defaults.get("substrate_id") not in substrate_ids:
    fail("color defaults must reference a known substrate")
if defaults.get("style_direction") != "contemporary editorial":
    fail("contemporary editorial must be the default style direction")
if defaults.get("palette_id") not in palette_ids:
    fail("color defaults must reference a known palette")
if defaults.get("mode") != "controlled two-ink":
    fail("color defaults must select controlled two-ink mode")
if defaults.get("dominant_percent") != [70, 85] or defaults.get("accent_percent") != [15, 30]:
    fail("color defaults must preserve the 70-85 / 15-30 plate ratio")
for palette in palettes:
    palette_inks = palette.get("ink_ids", [])
    if not 1 <= len(palette_inks) <= 2:
        fail(f"{palette['id']} must reference one or two inks")
    unknown = set(palette_inks) - ink_ids
    if unknown:
        fail(f"{palette['id']} references unknown inks {sorted(unknown)}")
    if palette.get("mode") == "pure one-ink" and len(palette_inks) != 1:
        fail(f"{palette['id']} one-ink mode must reference exactly one ink")
    if palette.get("mode") != "pure one-ink" and len(palette_inks) != 2:
        fail(f"{palette['id']} two-ink mode must reference exactly two inks")

roles = typography.get("roles", [])
require_unique(roles, "typography role")
for role in roles:
    if not role.get("display") or not role.get("support") or not role.get("behavior"):
        fail(f"{role['id']} needs display, support, and behavior rules")

layouts = compositions.get("compositions", [])
require_unique(layouts, "composition")
for composition in layouts:
    subject_range = composition.get("dominant_subject_percent", [])
    paper_range = composition.get("empty_paper_percent", [])
    if len(subject_range) != 2 or not 0 < subject_range[0] <= subject_range[1] <= 100:
        fail(f"{composition['id']} has an invalid subject range")
    if len(paper_range) != 2 or not 0 < paper_range[0] <= paper_range[1] <= 100:
        fail(f"{composition['id']} has an invalid paper range")
    if composition.get("manual_gesture_limit") != 1:
        fail(f"{composition['id']} must allow exactly one manual gesture family")

carrier_items = carriers.get("carriers", [])
require_unique(carrier_items, "carrier")
for carrier in carrier_items:
    ratios = carrier.get("ratios", [])
    if not ratios or any(not RATIO.fullmatch(ratio) for ratio in ratios):
        fail(f"{carrier['id']} has an invalid ratio")
    if not carrier.get("required_signals") or not carrier.get("forbidden_signals"):
        fail(f"{carrier['id']} needs required and forbidden visual signals")

selection = imperfections.get("selection", {})
if selection.get("contemporary_effect_count") != [0, 2] or selection.get("material_effect_count") != [2, 3] or selection.get("preserve_across_retries") is not True:
    fail("imperfections must select 0-2 effects for contemporary work and 2-3 for material or vintage work")
if not selection.get("seed_strategy"):
    fail("imperfections need a deterministic seed strategy")
imperfection_items = imperfections.get("effects", [])
require_unique(imperfection_items, "imperfection")
if len(imperfection_items) < 5:
    fail("imperfections need at least five controlled effect families")
for imperfection in imperfection_items:
    ranges = [value for key, value in imperfection.items() if key.endswith("_percent") or key.endswith("_mm")]
    if len(ranges) != 1 or len(ranges[0]) != 2 or not 0 < ranges[0][0] <= ranges[0][1]:
        fail(f"{imperfection['id']} needs one valid effect range")
    if not imperfection.get("applies_to"):
        fail(f"{imperfection['id']} needs an application boundary")
if len(imperfections.get("guardrails", [])) < 5:
    fail("imperfections need readability and structural guardrails")

profiles = rhythm.get("profiles", [])
profile_ids = require_unique(profiles, "rhythm profile")
if rhythm.get("default_profile") not in profile_ids:
    fail("rhythm default_profile must reference a known profile")
if len(rhythm.get("focal_events", [])) < 5 or len(rhythm.get("release_devices", [])) < 5:
    fail("rhythm needs meaningful focal-event and release-device catalogs")
if len(rhythm.get("optional_unresolved_edges", [])) < 4:
    fail("rhythm needs at least four optional unresolved-edge behaviors")
for profile in profiles:
    paper_range = profile.get("empty_paper_percent", [])
    if len(paper_range) != 2 or not 0 < paper_range[0] <= paper_range[1] <= 100:
        fail(f"{profile['id']} has an invalid empty-paper range")
    if profile.get("focal_event_count") != 1 or profile.get("release_zone_count") != 1:
        fail(f"{profile['id']} must select one focal event and one release zone")
    if profile.get("unresolved_edge") != "optional":
        fail(f"{profile['id']} must keep unresolved edges optional")
    if not profile.get("default_for") or not profile.get("subject_behavior") or not profile.get("energy_distribution"):
        fail(f"{profile['id']} needs routing, energy-distribution, and subject-behavior rules")
if len(rhythm.get("failure_signals", [])) < 5:
    fail("rhythm needs at least five observable failure signals")
if len(rhythm.get("guardrails", [])) < 5:
    fail("rhythm needs at least five guardrails")
print(
    "Validated mono-color design system: "
    f"{len(inks)} inks, {len(palettes)} palettes, {len(roles)} type roles, "
    f"{len(layouts)} compositions, {len(carrier_items)} carriers, "
    f"{len(imperfection_items)} imperfections, {len(profiles)} rhythm profiles."
)
