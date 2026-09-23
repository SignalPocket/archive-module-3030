# Latch-and-Catch Test V3

This miniature assembly tests the proven 1.80 mm Yellow PETG flexure against a real drawer catch before the full Archive Module is printed. The parts contain no proposal text.

Assembly references: `assembly-isometric.svg` and `assembly-top-view.svg`.

## Print

- `latch_test_jig_black.stl` — Black PLA Basic, 0.20 mm, four walls, 20% infill.
- `catch_slider_gray.stl` — Iron Gray Metallic PLA, 0.20 mm, four walls, 20% infill.
- `security_flexure_180_yellow.stl` — Yellow PETG HF, 0.16 mm, five walls, 100% infill.

Print every part in the supplied orientation. No supports.

## Assemble

1. Let the PETG cool completely.
2. Slide the gray part into the black jig with its raised side rail facing the jig's wide right-hand opening.
3. Stand the yellow flexure vertically against the outside of the jig's right wall. The 10 mm-thick anchor end goes into the rectangular mounting cradle; the hooked free end points inward through the wall opening.
4. For this test only, retain the anchor with painter's tape or a small clamp. Do not glue it.
5. Slide the gray part inward until the yellow hook drops into the gap in its raised side rail.

## Operate

This prototype uses an **outward pull release**: pull the center of the yellow security bar outward approximately 2 mm while gently drawing the gray slider out. Release the bar and confirm it returns straight.

Repeat 20 times. A passing result means:

- the hook reliably enters the catch;
- the slider cannot move outward while latched;
- approximately 2 mm of outward movement releases it;
- the yellow bar returns without whitening or remaining bent;
- the gray slider still moves freely in the black guide.

Do not force the slider or flex the yellow bar more than necessary. Report any accidental release, scraping, cracking, or excessive force before printing the final module.
