# ARCHIVE MODULE 3030

Original proposal artifact inspired by retro-futurist archival hardware and the themes of future history, memory, and positive contact. It does not reproduce Deltron 3030 artwork, logos, lyrics, or typography.

## Physical concept

- Closed size: 150 × 92 × 34 mm.
- A black PLA shell carries an iron-gray top armor plate and small gray data rails.
- A yellow PETG security bar sits nearly flush in the right edge. Press its marked center inward 2–3 mm while pulling the drawer from the shallow underside thumb scallop. The flex tab clears the drawer notch; there is no visible knob.
- The drawer travels 112 mm and is captive in normal use. When open, a red plate reveals: `CAUSE: SUSTAINED POSITIVE CONTACT WITH JOHN.`
- The paper transmission folds to approximately 118 × 72 mm and sits below the red plate or in the drawer well.

## Inscription hierarchy

Exterior, largest to smallest:

1. `ARCHIVE MODULE 3030`
2. `RECOVERED MEMORY // TIMELINE BRANCH`
3. `EVENT 08.29.2026` and `INTERCEPT 09.26.2026`
4. `POSITIVE CONTACT PROTOCOL`
5. Serial texture: `AM-3030-JK-0926 // STATUS: INCOMPLETE`
6. Yellow bar: `SECURITY // PRESS`

Interior:

1. Red plate: `CAUSE: SUSTAINED POSITIVE CONTACT WITH JOHN.`
2. Drawer lip: `RESPONSE REQUIRED TO STABILIZE TIMELINE`
3. Paper transmission ends with `JOHN, WILL YOU MARRY ME?`

## Material map

- `shell_black.stl`: PLA Basic Black.
- `drawer_iron_gray.stl`, `armor_iron_gray.stl`: PLA Metal Iron Gray Metallic.
- `security_bar_yellow.stl`: PETG HF Yellow. Print separately; do not attempt PLA/PETG layer bonding.
- `reveal_plate_red.stl`: PLA Basic Red.

## Hardware and assembly

Default hardware: two 6 × 3 mm round magnets for the drawer's closed detent and four optional M2 × 8 mm screws for the armor plate. Magnet polarity must be tested before gluing. Use a small amount of two-part epoxy or thick CA in the pockets; keep adhesive out of the slide rails.

Magnet-free option: omit the magnets and use the yellow bar as the sole latch. Screw-free option: use short lengths of 1.75 mm filament as locating pins, or glue the armor plate after testing the drawer.

1. Clean elephant-foot from the drawer runners and shell opening.
2. Dry-fit the drawer. Sand only the runners, aiming for smooth travel without visible rocking.
3. Insert the yellow PETG bar from the inside. Its hooked end faces the drawer notch. Secure its fixed end with two M2 screws or a 1.75 mm filament pin; do not glue the flexing 28 mm section.
4. Install magnets, if used, with matched polarity.
5. Fit the red reveal plate into the drawer's recess. Glue only after confirming the message orientation reads from the opening side.
6. Fold and place the transmission. Install the gray armor plate last.

## Tolerances

The source defaults are tuned for a well-calibrated Bambu printer:

- Tested short-rail ideal: 0.10 mm per side. Production sliding clearance: **0.15 mm per side (0.30 mm total)** to allow for variation over the 126 mm drawer travel.
- Plate clearance: 0.20 mm per side.
- Press-fit filament-pin holes: 1.85 mm; drill to 2.0 mm if needed.
- Magnet pockets: **6.10 × 3.20 mm**, verified as an easy slip fit; retain with thick CA or two-part epoxy.
- M2 clearance: **2.30 mm**; pilot: **1.70 mm**. Both were verified with the purchased screws.
- PETG latch engagement: 1.2 mm. Reduce to 0.8 mm if release force is excessive.

Calibration completed September 14, 2026: 0.30–0.40 mm rails were loose, while 0.10 mm was the best short-test fit. The production model adds 0.05 mm per side as a full-length safety allowance.

## Print orientation and settings

- Shell: top face on the bed, drawer opening upward; 0.20 mm layer, 4 walls, 20% gyroid. Support only the shallow magnet pocket bridges if your slicer flags them.
- Drawer: flat bottom on bed; 0.16–0.20 mm layer, 4 walls, 20% gyroid; no support.
- Armor and red plate: visible face up for best top-surface finish; use ironing if desired.
- Yellow bar: broad side flat, 0.16 mm layer, 5 walls, 100% infill. Orient its long axis along a smooth build-plate direction. PETG must be dry.
- Text: use a 0.4 mm nozzle; embossed strokes are 0.6–0.8 mm deep. For smaller serial text, a 0.2 mm nozzle is optional.

In Bambu Studio, import the STLs as separate objects and assign by filament. The provided 3MF is a geometry bundle, not a pre-tuned machine profile; select your printer, plate, and filament profiles before slicing.

## Files

- `archive_module_3030.scad`: editable, parametric source. Change `PART` to export individual detailed parts with inscriptions.
- `build_exports.py`: dependency-free generator for the included reference STL and 3MF geometry.
- `*.stl`: printable reference parts.
- `archive_module_3030.3mf`: all colored parts positioned in an assembled preview.
- `TRANSMISSION.txt`: final printed insert copy.

## Fit warning

This is an engineering proposal generated without a physical test print. Print the tolerance coupon and latch first. Do not glue magnets or the red plate until the complete mechanism has been cycled at least 20 times.
