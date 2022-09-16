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
        cylinder(7, d=3, $fn=64);
        translate([7.85, 7.85, 3])
        cylinder(3, d=6, $fn=64);
        translate([7.85, 119.85, -1])
        cylinder(7, d=3, $fn=64);
        translate([7.85, 119.85, 3])
        cylinder(3, d=6, $fn=64);
        translate([127.85, 7.85, -1])
        cylinder(7, d=3, $fn=64);
        translate([127.85, 7.85, 3])
        cylinder(3, d=6, $fn=64);
        translate([247.85, 119.85, -1])
        cylinder(7, d=3, $fn=64);
        translate([247.85, 119.85, 3])
        cylinder(3, d=6, $fn=64);
        translate([247.85, 7.85, -1])
        cylinder(7, d=3, $fn=64);
        translate([247.85, 7.85, 3])
        cylinder(3, d=6, $fn=64);

        // Holes for plastic prongs
        translate([7.85, 40, -1])
        cylinder(7, d=3, $fn=64);
        translate([247.85, 40, -1])
        cylinder(7, d=3, $fn=64);
    }

    // Box
    translate([12.5, 12.5, 5])
    difference() {
        difference() {
            cube([230, 115.35, 30]);
            translate([5, 5, -1])
            cube([220, 95, 25]);
        }

        // Mic stand screw hole
        translate([115, 116, 8])
        rotate([90, 0, 0])
        // Hole should be slightly too small, so thread can be melted in
        cylinder(16.1, d=15, $fn=64);

        // Raspberry Pi mounting holes
        translate([86.9, 57.9, 23])
        cylinder(5, d=4, $fn=64);
        translate([86.9, 8.9, 23])
        cylinder(5, d=4, $fn=64);
        translate([28.9, 57.9, 23])
        cylinder(5, d=4, $fn=64);
        translate([28.9, 8.9, 23])
        cylinder(5, d=4, $fn=64);

        // Raspberry Pi ports
        translate([-1, 7, 7])
        cube([7, 15, 17]);
        translate([-1, 25, 7])
        cube([7, 15, 17]);
        translate([-1, 42.8, 9.5])
        cube([7, 17, 14.5]);
        rotate([90, 0, 0])
        translate([37, 20.5, -6])
        cylinder(7, d=7, $fn=64);
        translate([46.5, -1, 19.3])
        cube([9, 7, 4.7]);
        translate([60, -1, 19.3])
        cube([9, 7, 4.7]);
        translate([73.5, -1, 19.3])
        cube([12, 7, 4.7]);

        // DC socket hole
        rotate([0, 90, 0])
        translate([-10, 80, 224])
        cylinder(7, d=7, $fn=64);
        rotate([0, 90, 0])
        translate([-10, 80, 224])
        cylinder(4, d=10, $fn=64);
    }

}

case();