function setup() {
    createCanvas(500, 500);
    background(245, 245, 245);


    var nick = ["n","i","c","k"];
    var noura = ["n", "o", "u", "r", "a"];
    var nx = 300;
    var ny = 230;
    var nt = 5000;
    var ni = 1;
    strokeWeight(0);
    fill(0);
    for(var i = 0; i < noura.length - 1; i++) {
        setTimeout(function() {
            text(nick[ni], nx, ny);
            text(noura[ni], nx + 100, ny);
            nx += 10;
            ni += 1;
        }, nt);
        nt += 350;
    }
}

function draw() {
    stroke(0);
    fill(0,0,0,0);
    var t = random(0, 2*PI);
    var x = map(t, 0, 4*PI, 0, width);
    var y = 250 + 100 * (-1) * sin(t);
    if ( y < 0 ) { y *= -1; }
    pencil(x + 50, y);
    pencil(x + 150, y);
}

function pencil(x, y) {
    stroke(50, 50, 50, 100);
    fill(50, 50, 50, 100);
    ellipse(x, y, 20, 20);
}
