// ARCHIVE MODULE 3030 — production candidate, 2026-09-23
// Original retro-future archive design. Units: millimeters.
PART = "assembly"; // chassis, lid, drawer, armor, timeline, reveal, assembly
$fn = 64;

L=150; W=92; chassis_h=31; wall=3;
slide_clearance=0.15;
drawer_l=126; drawer_w=W-2*wall-2*slide_clearance; drawer_h=19.5;
lid_h=2; armor_h=2.4; timeline_h=1.2;
magnet_d=6.10; magnet_depth=3.20;
m2_clearance=2.30; m2_pilot=1.70;
nodes=[[22,14],[52,14],[82,14],[112,14]];
open_node=[141,46];

module rounded_box(size,r=3){
  hull() for(x=[r,size[0]-r],y=[r,size[1]-r]) translate([x,y,0]) cylinder(r=r,h=size[2]);
}

module chassis(){
  difference(){
    union(){
      difference(){
        rounded_box([L,W,chassis_h],3);
        translate([wall,wall,wall]) cube([L-wall+1,W-2*wall,chassis_h]);
      }
      for(p=nodes) translate([p[0],p[1],23.6]) cylinder(d=8,h=7.4);
      translate([134,-0.8,8]) cube([14,3.8,10]);
    }
    for(p=nodes) translate([p[0],p[1],28]) cylinder(d=m2_pilot,h=4);
    translate([141,wall,13]) rotate([90,0,0]) cylinder(d=magnet_d,h=magnet_depth);
    translate([L-15,W/2,-0.1]) scale([1,1,.45]) cylinder(r=12,h=7);
  }
}

module lid(){
  difference(){
    rounded_box([L,W,lid_h],3);
    for(p=nodes) translate([p[0],p[1],-1]) cylinder(d=m2_clearance,h=lid_h+2);
  }
}

module drawer(){
  difference(){
    union(){
      cube([drawer_l,drawer_w,3]);
      cube([drawer_l,3,drawer_h]);
      translate([0,drawer_w-3,0]) cube([drawer_l,3,drawer_h]);
      cube([3,drawer_w,drawer_h]);
      translate([drawer_l-3,0,0]) cube([3,drawer_w,drawer_h]);
      translate([110,3,7]) cube([14,.8,10]);
    }
    translate([117,0,12]) rotate([-90,0,0]) cylinder(d=magnet_d,h=magnet_depth);
    translate([drawer_l-1,drawer_w/2,4]) rotate([0,90,0]) cylinder(r=8,h=4);
  }
}

module armor(){
  difference(){
    translate([5,6,0]) rounded_box([140,80,armor_h],3);
    for(p=nodes) translate([p[0],p[1],-1]) cylinder(d=m2_clearance,h=armor_h+2);
  }
  translate([75,57,armor_h]) linear_extrude(.7)
    text("ARCHIVE MODULE 3030",size=7,font="Liberation Sans:style=Bold",halign="center",valign="center");
  translate([75,46,armor_h]) linear_extrude(.6)
    text("MEMORY PRESERVED // TIMELINE ACTIVE",size=3.2,font="Liberation Sans:style=Bold",halign="center",valign="center");
}

module line_between(a,b,w=6,h=timeline_h){
  hull(){
    translate([a[0],a[1],0]) cylinder(d=w,h=h);
    translate([b[0],b[1],0]) cylinder(d=w,h=h);
  }
}

module timeline(){
  difference(){
    union(){
      for(i=[0:2]) line_between(nodes[i],nodes[i+1],6);
      line_between(nodes[3],open_node,6);
      for(p=nodes) translate([p[0],p[1],0]) cylinder(d=12,h=timeline_h);
      translate(open_node) cylinder(d=15,h=timeline_h);
    }
    for(p=nodes) translate([p[0],p[1],-1]) cylinder(d=m2_clearance,h=timeline_h+2);
    translate([open_node[0],open_node[1],-1]) cylinder(d=8,h=timeline_h+2);
  }
}

module reveal(){
  rounded_box([110,72,2],2);
  translate([55,48,2]) linear_extrude(.8)
    text("CAUSE: SUSTAINED",size=5,font="Liberation Sans:style=Bold",halign="center",valign="center");
  translate([55,36,2]) linear_extrude(.8)
    text("POSITIVE CONTACT",size=5,font="Liberation Sans:style=Bold",halign="center",valign="center");
  translate([55,24,2]) linear_extrude(.8)
    text("WITH JOHN.",size=6,font="Liberation Sans:style=Bold",halign="center",valign="center");
}

if(PART=="chassis") chassis();
else if(PART=="lid") lid();
else if(PART=="drawer") drawer();
else if(PART=="armor") armor();
else if(PART=="timeline") timeline();
else if(PART=="reveal") reveal();
else {
  color("#17191c") chassis();
  color("#17191c") translate([0,0,chassis_h]) lid();
  color("#73777b") translate([0,0,chassis_h+lid_h]) armor();
  color("#f2c300") translate([0,0,chassis_h+lid_h+armor_h]) timeline();
  color("#73777b") translate([24,3.15,3.15]) drawer();
  color("#a71930") translate([32,10,6.2]) reveal();
}
