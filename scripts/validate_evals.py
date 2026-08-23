#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVALS_PATH = ROOT / "evals" / "evals.json"
ALLOWED_MODES = {
    "pure one-ink",
    "chromatic + black",
    "complementary duotone",
    "overprint duotone",
}
ALLOWED_LAYOUTS = {
    "image field",
    "specimen annotation",
    "type-led declaration",
    "ruled information poster",
    "archival plate",
    "editorial cover",
    "object field",
    "overprint collage",
    "editorial journal",
}
HEX_COLOR = re.compile(r"^#[0-9A-F]{6}$")
RATIO = re.compile(r"^[1-9][0-9]*:[1-9][0-9]*$")


def fail(message: str) -> None:
    print(f"eval validation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


with EVALS_PATH.open(encoding="utf-8") as eval_file:
    data = json.load(eval_file)

if data.get("skill_name") != "mono-color" or data.get("schema_version") != 1:
    fail("unexpected skill_name or schema_version")

evals = data.get("evals")
if not isinstance(evals, list) or len(evals) < 11:
    fail("at least 11 evaluation cases are required")

ids = [case.get("id") for case in evals]
if len(ids) != len(set(ids)):
    fail("evaluation ids must be unique")

for case in evals:
    label = f"case {case.get('id', '?')}"
    for field in ("prompt", "expected_output", "assertions", "files"):
        if field not in case:
            fail(f"{label} is missing {field}")

    assertions = case["assertions"]
    required = {
        "ratio",
        "mode",
        "ink_hexes",
        "plate_roles",
        "layout",
        "exact_text",
        "generates_image",
        "must_not",
    }
    if set(assertions) != required:
        fail(f"{label} assertions must contain exactly {sorted(required)}")
    if not RATIO.fullmatch(assertions["ratio"]):
        fail(f"{label} has an invalid ratio")
    if assertions["mode"] not in ALLOWED_MODES:
        fail(f"{label} has an unknown mode")
    if assertions["layout"] not in ALLOWED_LAYOUTS:
        fail(f"{label} has an unknown layout")

    inks = assertions["ink_hexes"]
    roles = assertions["plate_roles"]
    if not 1 <= len(inks) <= 2 or any(not HEX_COLOR.fullmatch(ink) for ink in inks):
        fail(f"{label} must use one or two uppercase hex inks")
    if len(inks) != len(roles):
        fail(f"{label} must assign one role to each ink plate")
    expected_ink_count = 1 if assertions["mode"] == "pure one-ink" else 2
    if len(inks) != expected_ink_count:
        fail(f"{label} ink count does not match its mode")
    if not assertions["must_not"]:
        fail(f"{label} needs at least one negative assertion")

print(f"Validated {len(evals)} mono-color evaluation cases.")