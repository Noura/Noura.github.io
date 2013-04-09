$(window).load(function() {

    // make content the right width to finish scrolling nicely in this window
    var extra_width = $(window).width() - 700 - 151 - 21;
    if (extra_width > 0) {
        var $main = $('#main');
        var main_width = $main.width();
        $main.width(main_width + extra_width);
    }
   
    // constants used throughout
    var $body = $('body');
    $body.scrollLeft(0);
    var tab_content_width = 800;
    var tab_width = 102;
    var cutoff_width = tab_content_width - tab_width;
    var tabs = [];
    $('.tab').each(function() {
        tabs.push({$el: $(this)});
    });

    // clicking on a tab scrolls you there
    $('.tab').on('click', function() {
        var i = $(this).data('i');
        $body.animate({scrollLeft: i*tab_content_width}, 500);
    });

setTimeout(function() {
    // scrolling through tabs
    setInterval(function() {
        var x = Math.max(0, $body.scrollLeft());
        var i = Math.floor(x / cutoff_width);
        if (i >= tabs.length) {
            return;
        }
        var margin_left = i*tab_width;
        var offset = (i+1)*tab_content_width;
        tabs[i].$el.css({'position': 'fixed', 'margin-left': margin_left+'px'});
        for (var j = i + 1; j < tabs.length; j++) {
            tabs[j].$el.css({'position': 'static', 'margin-left': '0'});
        }
        if (i + 1 < tabs.length) {
            tabs[i+1].$el.css('margin-left', offset+'px');
        }
        for (var j = 0; j < tabs.length; j++) {
            if (j == i) {
                tabs[j].$el.addClass('active');
            } else {
                tabs[j].$el.removeClass('active');
            }
        }
    }, 50);
}, 20);
});

