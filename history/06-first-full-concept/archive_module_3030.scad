// ARCHIVE MODULE 3030 — editable OpenSCAD source
// Original industrial future-archive geometry; no protected artwork reproduced.
PART = "assembly"; // assembly, shell, drawer, armor, bar, red_plate, tolerance_test
$fn = 48;

L=150; W=92; H=34; wall=3;
slide_clearance=0.15; // tested 0.10; +0.05 safety for the 126 mm full travel
plate_clearance=0.20;
magnet_d=6.10; magnet_depth=3.20;
m2_clearance=2.30; m2_pilot=1.70;
drawer_L=126; drawer_W=W-2*wall-2*slide_clearance; drawer_H=23;

module label(txt, size=5, depth=.8) {
  linear_extrude(depth) text(txt, size=size, font="Liberation Sans:style=Bold", halign="center", valign="center");
}
module shell(){
  difference(){
    difference(){ rounded_box([L,W,H],3); translate([wall,wall,wall]) cube([L-wall+1,W-2*wall,H-2*wall]); }
    translate([L-5,8,8]) cube([8,W-16,drawer_H+2]);
    translate([L-22,W/2-10,-.1]) scale([1,1,.35]) cylinder(r=10,h=5);
    translate([L-36,W-3,13]) cube([30,5,9]);
  }
  translate([L/2,W/2,H]) label("ARCHIVE MODULE 3030",7);
  translate([L/2,W/2-10,H]) label("RECOVERED MEMORY // TIMELINE BRANCH",3.1);
  translate([33,10,H]) label("EVENT 08.29.2026",2.7);
  translate([L-36,W-10,H]) label("INTERCEPT 09.26.2026",2.7);
}
module drawer(){
  difference(){
    union(){ cube([drawer_L,drawer_W,3]); cube([drawer_L,3,drawer_H]); translate([0,drawer_W-3,0]) cube([drawer_L,3,drawer_H]); cube([3,drawer_W,drawer_H]); }
    translate([15,10,2]) cube([100,drawer_W-20,2]);
    translate([drawer_L-21,drawer_W-1,10]) cube([10,3,5]);
  }
  translate([drawer_L-2,drawer_W/2,10]) rotate([90,0,90]) label("RESPONSE REQUIRED",2.6,.8);
}
module armor(){
  difference(){ rounded_box([116,58,2.4],2); for(x=[8,108],y=[8,50]) translate([x,y,-1]) cylinder(d=m2_clearance,h=5); }
  translate([58,29,2.4]) label("POSITIVE CONTACT PROTOCOL",4,.7);
  translate([58,17,2.4]) label("AM-3030-JK-0926 // STATUS: INCOMPLETE",2.6,.7);
}
module security_bar(){
  union(){ cube([34,8,3]); translate([27,-1,0]) cube([7,10,6]); translate([24,1,3]) cube([5,6,2]); }
  translate([14,4,3]) label("PRESS",2.5,.6);
}
module red_plate(){
  cube([100,52,2]);
  translate([50,33,2]) label("CAUSE: SUSTAINED",4,.8);
  translate([50,25,2]) label("POSITIVE CONTACT",4,.8);
  translate([50,17,2]) label("WITH JOHN.",5,.8);
}
module tolerance_test(){
  cube([70,24,3]);
  for(i=[0:3]) translate([4+i*16,5,3]) cube([12-(i*.1),14,3]);
}
module rounded_box(s,r){ hull(){ for(x=[r,s[0]-r],y=[r,s[1]-r]) translate([x,y,0]) cylinder(r=r,h=s[2]); } }

if(PART=="shell") shell();
else if(PART=="drawer") drawer();
else if(PART=="armor") armor();
else if(PART=="bar") security_bar();
else if(PART=="red_plate") red_plate();
else if(PART=="tolerance_test") tolerance_test();
else { color("#17191c") shell(); color("#73777b") translate([17,17,H+1]) armor(); color("#8b0f1a") translate([22,20,6]) red_plate(); color("#e5bf19") translate([L-37,W-6,14]) security_bar(); }
