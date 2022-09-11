use <64x32 - 4mm pitch.scad>

module cut() {
    translate([200, -1, -1])
    cube([60, 130, 60]);
}

translate([-200, 0, 0])
intersection() {
    case();
    cut();
}
