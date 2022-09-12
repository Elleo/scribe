// Base plate
module case() {
    difference() {
        difference() {
            cube([255.70, 127.70, 5]);
            translate([17.5, 17.5, -1])
            cube([220, 95, 7]);
        }
        // Screw holes
        translate([7.85, 7.85, -1])
        cylinder(7, 3, 3);
        translate([7.85, 7.85, 3])
        cylinder(3, 5, 5);
        translate([7.85, 119.85, -1])
        cylinder(7, 3, 3);
        translate([7.85, 119.85, 3])
        cylinder(3, 5, 5);
        translate([127.85, 7.85, -1])
        cylinder(7, 3, 3);
        translate([127.85, 7.85, 3])
        cylinder(3, 5, 5);
        translate([247.85, 119.85, -1])
        cylinder(7, 3, 3);
        translate([247.85, 119.85, 3])
        cylinder(3, 5, 5);
        translate([247.85, 7.85, -1])
        cylinder(7, 3, 3);
        translate([247.85, 7.85, 3])
        cylinder(3, 5, 5);
    }

    // Box
    translate([12.5, 12.5, 5])
    difference() {
        difference() {
            cube([230, 115.35, 45]);
            translate([5, 5, -1])
            cube([220, 95, 35]);
        }

        // Mic stand screw hole
        translate([115, 116, 17])
        rotate([90, 0, 0])
        // Hole should be slightly too small, so thread can be melted in
        cylinder(16.1, 15, 15);
    }
}

case();