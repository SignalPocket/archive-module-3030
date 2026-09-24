// JOHN 3030 keychain — original retro-futurist companion piece
// Units: millimeters. Designed for 0.4 mm nozzle.
PART = "assembly"; // base, face, text, signal, red_indicator, assembly
$fn = 64;

NAME_TEXT = "3030 // J&K";
STATUS_TEXT = "POSITIVE CONTACT";
TITLE_FONT = "Agency FB:style=Bold";
STATUS_FONT = "Bahnschrift:style=SemiBold";

L=72; W=30; base_h=4;
ring_center=[8.5,15]; ring_hole=5.4;
face_pos=[17,4]; face_size=[51,22]; face_h=1.0;
fit_clearance=.15;

module rounded_box(size,r=3){
  hull() for(x=[r,size[0]-r],y=[r,size[1]-r])
    translate([x,y,0]) cylinder(r=r,h=size[2]);
}

module face_outline_2d(clearance=0){
  translate([face_pos[0]-clearance,face_pos[1]-clearance])
    offset(r=clearance) square(face_size);
}

module lettering_2d(){
  translate([42.5,20]) resize([43,0],auto=[false,true])
    text(NAME_TEXT,size=7.2,font=TITLE_FONT,spacing=1.04,halign="center",valign="center");
  translate([42.5,14.5])
    text(STATUS_TEXT,size=2.45,font=STATUS_FONT,spacing=1.02,halign="center",valign="center");
}

module signal_2d(extra=0){
  hull(){ translate([24,8.5]) circle(d=5.6+2*extra); translate([43,8.5]) circle(d=5.6+2*extra); }
  hull(){ translate([43,8.5]) circle(d=5.6+2*extra); translate([62,8.5]) circle(d=5.6+2*extra); }
}

module heart_2d(size=3.3){
  scale([size/4.3,size/4.3]) union(){
    translate([-1,0.55]) circle(r=1.15);
    translate([1,0.55]) circle(r=1.15);
    polygon([[-2.1,.55],[2.1,.55],[0,-2.25]]);
  }
}

module base(){
  difference(){
    union(){
      rounded_box([L,W,base_h],5);
      translate(ring_center) cylinder(d=15,h=base_h);
    }
    translate([ring_center[0],ring_center[1],-1]) cylinder(d=ring_hole,h=base_h+2);
    translate([face_pos[0]-fit_clearance,face_pos[1]-fit_clearance,base_h-face_h])
      rounded_box([face_size[0]+2*fit_clearance,face_size[1]+2*fit_clearance,face_h+.2],2.2);
  }
}

module face(){
  difference(){
    translate([face_pos[0],face_pos[1],base_h-face_h]) rounded_box([face_size[0],face_size[1],face_h],2);
    translate([0,0,base_h-.42]) linear_extrude(.5) lettering_2d();
    translate([0,0,base_h-face_h-.1]) linear_extrude(face_h+.2) signal_2d(fit_clearance);
    translate([65.4,23.1,base_h-face_h-.1]) linear_extrude(face_h+.2)
      offset(r=fit_clearance) heart_2d();
  }
}

module text_part(){
  translate([0,0,base_h-.42]) linear_extrude(.42) lettering_2d();
}

module signal(){
  difference(){
    translate([0,0,base_h-face_h]) linear_extrude(face_h) signal_2d();
    for(x=[24,43,62]) translate([x,8.5,base_h-face_h-.1]) cylinder(d=1.8,h=face_h+.2);
  }
}

module red_indicator(){
  translate([65.4,23.1,base_h-face_h]) linear_extrude(face_h) heart_2d();
}

if(PART=="base") base();
else if(PART=="face") face();
else if(PART=="text") text_part();
else if(PART=="signal") signal();
else if(PART=="red_indicator") red_indicator();
else {
  color("#17191c") base();
  color("#73777b") face();
  color("#111214") text_part();
  color("#f2c300") signal();
  color("#a71930") red_indicator();
}
