# ARCHIVE MODULE 3030 — design evolution

This repository intentionally preserves the false starts as well as the final production candidate. They document how the object moved from a general hidden-compartment concept to a calibrated, modular proposal artifact designed around the actual printer, materials, magnets, and screws.

## 01 — Initial printer calibration

Folder: `history/01-printer-calibration/`

The first neutral-looking prints tested the unknown physical interfaces without revealing the proposal project:

- Magnet-fit coupon
- Storage-case rail and slider
- Corrected rail
- Cable-clip flex test

Physical result: the magnet fit the smallest ring, while the original rail channels were all loose or incompatible with the test block. That ruled out relying on nominal CAD dimensions alone.

## 02 — Focused hardware calibration

Folder: `history/02-printer-calibration-v2/`

The second set isolated each critical interface:

- 6.10 mm magnet sleeve
- 2.30 mm M2 clearance hole
- 1.70 mm M2 pilot hole
- 0.30, 0.35, and 0.40 mm rail-clearance samples

Physical result: the magnet pocket was good, both screw interfaces worked, and every rail option remained too loose.

## 03 — Fine rail calibration

Folder: `history/03-printer-calibration-v3/`

The third set narrowed rail clearance to 0.10, 0.15, 0.20, and 0.25 mm per side.

Physical result: 0.10 mm was the best test fit and still slid easily. The full-length production drawer uses 0.15 mm per side to allow for the much longer contact surface.

## 04 — Yellow PETG flexure study

Folder: `history/04-petg-flexure/`

Three small thickness samples explored whether the yellow security element could work as a bending spring. The test established printable PETG thicknesses, but it did not validate the complete release mechanism.

## 05 — Latch-and-catch prototype

Folder: `history/05-latch-catch-test/`

This version attempted a yellow flexure, a gray catch slider, and a black test jig. It includes both top and isometric explanatory sketches.

Decision: the jig did not accurately reproduce the intended assembled motion, so the mechanical latch was abandoned rather than risking the real box. The reliable solution became a magnetic drawer detent with hidden underside thumb access.

## 06 — First complete Archive Module concept

Folder: `history/06-first-full-concept/`

This was the first complete modular design language:

- Black shell
- Iron-gray armor and drawer
- Yellow security bar
- Red reveal plate
- Initial transmission
- Early tolerance coupon

It established the overall artifact, inscription hierarchy, separate-material construction, and secret red-message reveal.

## 07 — Final production candidate

Folder: `history/07-final-production-candidate/`

The final design incorporates the physical test results:

- 0.15 mm drawer clearance per side
- 6.10 × 3.20 mm magnet pockets
- 2.30 mm M2 clearance holes
- 1.70 mm M2 pilot holes
- Magnetic closed detent instead of a flex latch
- Four exposed M2 screws as completed-event nodes
- Separate yellow PETG timeline leading to an open fifth ring
- Red interior plate reading `CAUSE: SUSTAINED POSITIVE CONTACT WITH JOHN.`

The four fastened nodes represent 05.14.2023, 05.28.2023, 10.12.2023, and 08.29.2026. The open node represents 09.26.2026, awaiting its response.

## Original packages and supporting work

- `history/00-original-packages/` preserves the ZIP bundles exactly as delivered.
- `history/supporting-work/` preserves generation/export helpers used during development.
- The clean current production files remain in the repository's top-level `models/`, `docs/`, and `renders/` folders.

## 08 — Approved model revision

Folder: `history/08-approved-model-v2/`

The approved revision adds:

- Parameterized stretched retro-futurist title lettering
- Black PLA title geometry aligned for direct AMS printing on the iron-gray armor
- Year-over-day archive codes engraved around each yellow event circle
- Full-height drawer end cap so no red is visible while closed
- Widened concealed underside grip with five traction grooves
- Magnet pockets facing along the drawer's direction of travel
- LEGO-style assembly guide and final closed/reveal sketch

This stage is the approved basis for the first full-size physical print.
