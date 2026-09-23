# Printer Calibration Kit V2

Neutral fit checks for a small storage-case project. These files contain no names, dates, or project-specific markings.

## Print now in PLA

1. `slider_reference.stl` — print one, unless you kept the rectangular slider from V1.
2. Print all three rail files. Their filenames give the intended clearance per side:
   - `rail_clearance_030.stl`
   - `rail_clearance_035.stl`
   - `rail_clearance_040.stl`
3. `magnet_sleeve_610.stl` — confirms the selected 6.10 mm slip fit and 3.20 mm pocket depth.
4. `m2_clearance_230.stl` — the M2 screw should pass through freely.
5. `m2_pilot_170.stl` — tests whether the M2 screw can form threads in the printed PLA without splitting it.

Use 0.20 mm layers, four walls, and no supports. The tests are intentionally separate and clearly named in the slicer.

## Report back

- Which rail lets the slider move with one finger but does not rattle: 0.30, 0.35, or 0.40?
- Does the magnet sit fully inside the 6.10 × 3.20 mm sleeve without force?
- Does an M2 screw pass through the 2.30 mm sleeve?
- Can an M2 screw turn into the 1.70 mm pilot sleeve without cracking it?

Do not glue the magnet and do not overtighten the screw.
