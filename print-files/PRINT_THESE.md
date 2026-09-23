# Plate-ready print files

These are separate print jobs. Do not print the assembled reference 3MF in `models/`.

1. `01_chassis_black.3mf` — Black PLA
2. `02_drawer_gray.3mf` — Iron Gray Metallic PLA
3. `03_lid_black.3mf` — Black PLA
4. `04_armor_gray_black_ams.3mf` — one aligned multipart object: Iron Gray PLA armor plus Black PLA lettering
5. `05_timeline_yellow_petg.3mf` — Yellow PETG HF; print separately from all PLA parts
6. `06_reveal_red.3mf` — Red PLA

## Armor color assignment

When Bambu Studio opens job 04, it should show one object containing two parts. Assign:

- `Armor — Iron Gray PLA` → iron-gray spool
- `Top text — Black PLA` → black spool

Do not auto-arrange the two armor parts independently. They share the same origin and are already registered.

## Before printing

- Confirm every part is sitting flat on the plate.
- Confirm the lid and armor each show four event-screw holes. The rear edge is retained by two clips built into the chassis.
- Use 0.20 mm layers and four walls for the chassis and drawer.
- Use 0.16–0.20 mm layers for the lid and armor.
- Use 0.16 mm, five walls, and 100% infill for the yellow timeline.
- Print the drawer before the chassis and test its magnet pocket before using adhesive.
