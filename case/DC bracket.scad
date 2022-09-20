module bracket() {
    difference() {
        cube([14, 9, 5]);
        translate([7, 5, -1])
        cylinder(7, d=3, $fn=64);
    }
    translate([0, 22, 0])
    difference() {
        cube([14, 10, 5]);
        translate([7, 5, -1])
        cylinder(7, d=3, $fn=64);
    }
    translate([0, 9, 0])
    difference() {
        cube([14, 14, 30]);
        translate([7, 7, -1])
        cylinder(20, d=12, $fn=64);
        translate([7, 7, 18.99])
        cylinder(13, d1=12, d2=5, $fn=64);
    }
}

module cut() {
    translate([-1, -1, -1])
    cube([16, 17, 40]);
}

translate([0, 5, 0])
difference() {    
    bracket();
    cut();
}

intersection() {    
    bracket();
    cut();
}