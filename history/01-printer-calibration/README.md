# Printer Calibration Kit

These deliberately ordinary-looking parts test the fit assumptions used by a larger storage-case project without revealing its purpose.

## Print order

1. `magnet_fit_coupon.stl` in any spare PLA. Test a 6 × 3 mm magnet in the three pockets. Start with the loosest pocket and do not force the magnet below the surface.
2. `storage_case_rail_corrected.stl` in Black PLA Basic. Reuse the existing `storage_case_slider.stl`; there is no need to print the slider again. The three channels reproduce 0.30, 0.35, and 0.40 mm per-side sliding clearances.
3. `cable_clip_flex_test.stl` in Yellow PETG HF. This uses the same thickness and flex length as the concealed release bar but looks like a cable-management clip.

## Suggested settings

- PLA tests: 0.20 mm layer height, 4 walls, 20% gyroid.
- Yellow PETG clip: 0.16 mm layer height, 5 walls, 100% infill, broad face on the plate.
- No supports should be needed.

## Reading the tests

- The best rail lane moves smoothly under finger pressure but does not rattle when shaken.
- For the magnet coupon, choose the smallest pocket that accepts the magnet with firm thumb pressure. Use the looser pocket if adhesive will be added.
- The yellow clip should deflect approximately 2–3 mm and return without whitening, cracking, or remaining bent. Test gradually; do not fold it sharply.

Record which rail lane and magnet pocket work best before printing the larger project.
