var content_width = 4120;
var tab_content_width = 698;
var min_margin = 2;
var dt = 10;

$(window).load(function() {
    var $window = $(window);
    var min_x = 0;
    var max_x = content_width - $window.width();
    var $tabs = [];
    $('.tab').each(function() {
        $tabs.push($(this));
    });
    var tab_content_x = [];
    $('.tab-content').each(function() {
        tab_content_x.push($(this).position().left);
    });

    var prev_prev_x = 0;
    var prev_x = 0;
    setInterval(function() {
        var x = Math.max(0, $window.scrollLeft());
        var i = Math.floor(x / tab_content_width);
        var margin = tab_content_width - (x % tab_content_width);
        //margin = Math.max(min_margin, margin + 3*(prev_x - x));
        margin = Math.max(min_margin, margin);

        //console.log('x', x, 'i', i, 'margin', margin, 'prev_x - x', prev_x - x);
        for (var j = 0; j < i; j++) {
            $tabs[j].css('margin-right', min_margin + 'px');
        }
        $tabs[i].css('margin-right', margin+'px');
        for (var j = tabs.length - 1; j > i; j--) {
            $tabs[j].css('margin-right', tab_content_width + 'px');
        }
        prev_prev_x = prev_x;
        prev_x = x;
    }, dt);

});

