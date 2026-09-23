# ARCHIVE MODULE 3030 — production candidate

This version uses the tested dimensions and replaces the unreliable flex latch with a magnetic drawer detent.

> Private personal project. Please do not publish, share, fork, or redistribute the proposal text or artwork.

## Repository contents

- `models/` — editable OpenSCAD source, assembled reference 3MF, and individual printable STL parts.
- `docs/TRANSMISSION.txt` — final proposal transmission copy.
- `docs/assembly-diagram.html` — interactive exploded, closed, and open assembly sketches.
- `renders/assembly_preview.png` — assembled color preview.
- `history/` — the complete sequence of calibration parts, prototypes, discarded mechanisms, early models, build scripts, renders, and original ZIP packages.
- [`EVOLUTION.md`](EVOLUTION.md) — what changed at each stage and what the physical tests taught us.

## Visual construction

- Black PLA chassis and top lid.
- Iron-gray PLA drawer and armor plate.
- Yellow PETG timeline overlay, secured by four exposed M2 × 8 mm screws.
- Each screw marks a completed archival event: 05.14.2023, 05.28.2023, 10.12.2023, and 08.29.2026.
- The open yellow ring nearest the drawer represents 09.26.2026: a record awaiting its response.
- Red PLA reveal plate inside the drawer.

## Calibrated dimensions

- Drawer clearance: 0.15 mm per side, derived from the successful 0.10 mm short-rail test with 0.05 mm full-length allowance.
- Magnet pockets: 6.10 × 3.20 mm.
- M2 clearance holes: 2.30 mm.
- M2 pilot holes: 1.70 mm.

## Print order

Do not begin with the large chassis.

1. Print `models/drawer_gray.stl` and verify that the magnet seats in its pocket without force.
2. Print `models/chassis_black.stl`. Before adding adhesive, slide the empty drawer through its full travel.
3. Install the two magnets only after checking their attraction direction. Use a tiny amount of thick CA or two-part epoxy.
4. Print `models/lid_black.stl`, `models/armor_gray.stl`, and `models/timeline_yellow.stl`.
5. Stack lid → armor → yellow timeline. Insert the four M2 × 8 mm screws through the completed-event nodes and tighten only until seated. PETG can deform if overtightened.
6. Print `models/reveal_red.stl`, check its reading orientation, and install it in the drawer.
7. Add the folded transmission last.

## Suggested settings

- Chassis: Black PLA, flat bottom on the build plate with the open tray facing upward; 0.20 mm, 4 walls, 20% gyroid, no supports expected.
- Drawer: Iron Gray PLA, flat bottom on the plate, 0.20 mm, 4 walls, 20% gyroid, no supports.
- Lid and armor: flat, 0.16–0.20 mm, 4 walls.
- Yellow timeline: Yellow PETG HF, flat, 0.16 mm, 5 walls, 100% infill, no supports.
- Red reveal: Red PLA, flat, 0.16 mm; ironing optional.

## Important

This is the first full-size production candidate. Test the empty drawer before installing magnets, the red reveal, or the transmission. Keep the four top screws snug rather than tight.
