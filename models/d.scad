// ARCHIVE MODULE 3030 — production candidate, 2026-09-23
// Original retro-future archive design. Units: millimeters.
PART = "assembly"; // chassis, lid, drawer, armor, top_text, timeline, reveal, assembly
DRAWER_OPEN = 1; // assembly preview only: 0 closed, 85 open
$fn = 64;

// EDITABLE EXTERIOR LETTERING
TITLE_TEXT = "ARCHIVE MODULE 3030";
STATUS_TEXT = "MEMORY PRESERVED // TIMELINE ACTIVE";
TITLE_SIZE = 9;
STATUS_SIZE = 3.2;
TITLE_WIDTH = 116; // fixed cinematic width; editable with the wording
TITLE_FONT = "Agency FB:style=Bold";
STATUS_FONT = "Bahnschrift:style=SemiBold";
EVENT_YEARS = ["23", "23", "23", "26"];
EVENT_DAYS = ["134", "148", "285", "241"];
OPEN_EVENT_YEAR = "26";
OPEN_EVENT_DAY = "269";
CODE_FONT = "Liberation Sans:style=Bold";

L=150; W=92; chassis_h=31; wall=3;
slide_clearance=0.15;
drawer_l=126; drawer_w=W-2*wall-2*slide_clearance; drawer_h=19.5;
lid_h=2; armor_h=2.4; timeline_h=1.2;
magnet_d=6.10; magnet_depth=3.20;
m2_clearance=2.30; m2_pilot=1.70;
nodes=[[22,7.5],[52,7.5],[82,7.5],[112,7.5]];
open_node=[141,46];

 

  
 
 
module armor(){
  difference(){
    translate([5,4,0]) rounded_box([140,82,armor_h],3);
    for(p=nodes) translate([p[0],p[1],-1]) cylinder(d=m2_clearance,h=armor_h+2);
    // Registration recess for the separately colored black lettering.
    translate([0,0,armor_h-.25]) linear_extrude(.35) top_text_2d();
  }
}

module top_text(){
  // 0.25 mm registers into the armor; 0.60 mm remains visibly raised.
  translate([0,0,armor_h-.25]) linear_extrude(.85) top_text_2d();
}

module line_between(a,b,w=6,h=timeline_h){
  hull(){
    translate([a[0],a[1],0]) cylinder(d=w,h=h);
    translate([b[0],b[1],0]) cylinder(d=w,h=h);
  }
}

module code_tab(center,size=[21,7]){
  translate([center[0]-size[0]/2,center[1]-size[1]/2,0]) rounded_box([size[0],size[1],timeline_h],2);
}

module arc_code(year,day,center,r=4.7,size=1.45){
  // Two-digit year follows the upper arc.
  for(i=[0:1]) let(a=120-i*50)
    translate([center[0]+r*cos(a),center[1]+r*sin(a),timeline_h-.60])
      rotate([0,0,a-90]) linear_extrude(.70)
        offset(delta = 0.15) {
            text(year[i],size=size,font=CODE_FONT,halign="center",valign="center");
        }
  // Three-digit ordinal day follows the lower arc, left to right.
  for(i=[0:2]) let(a=225+i*45)
    translate([center[0]+r*cos(a),center[1]+r*sin(a),timeline_h-.60])
      rotate([0,0,a+90]) linear_extrude(.70)
        offset(delta = 0.15) {
            text(day[i],size=size,font=CODE_FONT,halign="center",valign="center");
}}

module timeline(){
  difference(){
    union(){
      for(i=[0:2]) line_between(nodes[i],nodes[i+1],6);
      line_between(nodes[3],open_node,6);
      for(p=nodes) translate([p[0],p[1],0]) cylinder(d=14,h=timeline_h);
      translate(open_node) cylinder(d=18,h=timeline_h);
    }
    for(p=nodes) translate([p[0],p[1],-1]) cylinder(d=m2_clearance,h=timeline_h+2);
    translate([open_node[0],open_node[1],-1]) cylinder(d=8,h=timeline_h+2);
    // Each event circle is a tiny dial: year above, ordinal day below.
    for(i=[0:3]) arc_code(EVENT_YEARS[i],EVENT_DAYS[i],nodes[i],r=4.4,size=2.55);
    arc_code(OPEN_EVENT_YEAR,OPEN_EVENT_DAY,open_node,r=6.4,size=2.55);
  }
}
 

if(PART=="chassis") chassis();
else if(PART=="lid") lid();
else if(PART=="drawer") drawer();
else if(PART=="armor") armor();
else if(PART=="top_text") top_text();
else if(PART=="timeline") timeline();
else if(PART=="reveal") reveal();
else {
  color("#17191c") chassis();
  color("#17191c") translate([0,0,chassis_h]) lid();
  color("#73777b") translate([0,0,chassis_h+lid_h]) armor();
  color("#111214") translate([0,0,chassis_h+lid_h]) top_text();
  color("#f2c300") translate([0,0,chassis_h+lid_h+armor_h]) timeline();
  color("#73777b") translate([24+DRAWER_OPEN,3.15,3.15]) drawer();
  color("#a71930") translate([32+DRAWER_OPEN,10,6.2]) reveal();
}
