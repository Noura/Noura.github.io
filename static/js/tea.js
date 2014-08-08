$(document).ready(function() {
    var w2h = 1920 / 1200; // width to height ratio of my background picture
    function sync_bg_img() {
        var r = window.innerWidth / window.innerHeight;
        var css = {'width': 'auto', 'height': 'auto'};
        if (r < w2h) {
            css.height = window.innerHeight;
        } else {
            css.width = window.innerWidth;
        }
        $('.background-image').css(css);
    }
    sync_bg_img();
    $(window).on('resize', sync_bg_img);
});
