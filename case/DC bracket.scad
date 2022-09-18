module bracket() {
    difference() {
        cube([12, 10, 5]);
        translate([6, 5, -1])
        cylinder(7, d=3, $fn=64);
    }
    translate([0, 22, 0])
    difference() {
        cube([12, 10, 5]);
        translate([6, 5, -1])
        cylinder(7, d=3, $fn=64);
    }
    translate([0, 10, 0])
    difference() {
        cube([12, 12, 30]);
        translate([6, 6, -1])
        cylinder(20, d=10, $fn=64);
        translate([6, 6, 18.99])
        cylinder(13, d1=10, d2=5, $fn=64);
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