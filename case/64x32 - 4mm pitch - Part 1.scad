use <64x32 - 4mm pitch.scad>

module cut() {
    translate([200, -1, -1])
    cube([60, 130, 60]);
}

difference() {
    case();
    cut();
}