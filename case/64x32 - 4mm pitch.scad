difference() {
    difference() {
        cube([255.70, 127.70, 5]);
        translate([17.5, 17.5, -1])
        cube([220, 95, 7]);
    }
    translate([7.85, 7.85, -1])
    cylinder(7, 4, 4);
    translate([7.85, 119.85, -1])
    cylinder(7, 4, 4);
    translate([247.85, 119.85, -1])
    cylinder(7, 4, 4);
    translate([247.85, 7.85, -1])
    cylinder(7, 4, 4);
}
translate([12.5, 12.5, 5])
difference() {
    cube([230, 105, 40]);
    translate([5, 5, -1])
    cube([220, 95, 30]);
}