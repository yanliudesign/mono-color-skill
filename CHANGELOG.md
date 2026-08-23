# Changelog

All notable changes to this project are documented in this file.

## Unreleased

### Changed

- Added an abstract-looseness path for supplied photos: requests for less realism now extract 2-4 identity anchors into deterministic masses, contours, rhythms, paper cutouts, and bounded print imperfections instead of applying a photographic duotone filter.
- Added deterministic controlled chance: each recipe selects 2-3 bounded print imperfections with a stable seed while preserving composition and readability.
- Added a machine-readable imperfection catalog and a relaxed-print poster example with dry-edge breakup, halftone drift, a pale second impression, and one broken gesture.
- Added four 1800×2400 reference-derived visual-system boards for typography, color, layout, and reproduction style, plus a reproducible board generator.
- Added a structured evidence map covering typography, color, layout, style, and signature moves across all 12 source references.
- Added a generated 1800×3000 PNG reference board that presents all design-system catalogs as one visual index.
- Added a machine-readable visual design system for colors, typography roles, composition geometry, and physical carriers, with cross-reference validation in CI.
- Invented headlines, labels, and microcopy now default to English while exact user-supplied wording stays in its original language.
- Summer, movement, travel, leisure, music, and night subjects now default to a romantic, free-spirited tone grounded in physical relationships and open space.
- Added a summer-cycling regression case for English copy and freer romantic direction.
- Refined the composition grammar from all 12 visual references: one dominant object, type-image collision, paper knockouts, and one controlled manual gesture.
- Romantic prompts now use a specific observable relationship instead of generic atmospheric props.
- Added a rooftop-party regression case for romantic one-ink event posters.

## 1.2.0 - 2026-08-22

### Added

- A recipe manifest that resolves inputs before prompt compilation.
- Deterministic defaults for ratio, paper, empty space, palette aliases, image treatment, typography, and layout selection.
- Ten structured evaluation cases with positive and negative assertions.
- An evaluation schema, local validator, and GitHub Actions workflow.

### Changed

- Layout selection now uses first-match priority instead of ambiguous branches.
- Consecutive outputs no longer change layout solely for novelty.
- Unrequested display copy is no longer invented by default.

## 1.1.0

- Added controlled two-ink modes, palette recipes, layout families, and expanded usage examples.