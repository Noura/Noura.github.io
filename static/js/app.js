$(document).ready(function() {

    $('.carousel').carousel();

    // constants used throughout
    $window = $(window);
    $content = $('#content');
    var tab_content_width = 800;
    var tab_width = 102;
    var cutoff_width = tab_content_width - tab_width;
    var min_d = 30;
    var max_d = 100;
    var tabs = [];
    $('.tab').each(function() {
        tabs.push({$el: $(this)});
    });

    function vertical_sizing() {
        $content.height($window.height() - 122);
    }
    vertical_sizing();
    $window.resize(vertical_sizing);

    // make content the right width to finish scrolling nicely in this window
    var extra_width = $window.width() - 700 - 72 - 150;
    if (extra_width > 0) {
        var $main = $('#main');
        var main_width = $main.width();
        $main.width(main_width + extra_width);
    }

    function scroll_to_tab(i) {
        $('body,html').animate({scrollLeft: i*tab_content_width}, 500);
    }

    // clicking on a tab scrolls you there
    $('.tab').on('click', function() {
        var i = $(this).data('i');
        scroll_to_tab(i);
    });

    // clicking on an arrow scrolls to next tab
    $('.tab-arrow-right').on('click', function(ev) {
        ev.stopPropagation();
        var i = $(this).data('i');
        scroll_to_tab(i + 1);
    });

    // scrolling through tabs
    setInterval(function() {
        var x = Math.max(0, $window.scrollLeft());
        var I = Math.floor(x / cutoff_width);
        if (I >= tabs.length) {
            return;
        }
        for (var i = 0; i < I; i++) {
            var margin_left = i*tab_width;
            tabs[i].$el.css({'position': 'fixed', 'margin-left': margin_left+'px'})
                .removeClass('active');
        }
        var margin_left = I*tab_width;
        tabs[I].$el.css({'position': 'fixed', 'margin-left': margin_left+'px'})
            .addClass('active');
        var i = I + 1;
        var offset = i * tab_content_width;
        if (i < tabs.length) {
            tabs[i].$el.css({'position': 'static', 'margin-left': offset+'px'})
                .removeClass('active');
        }
        i++;
        while (i < tabs.length) {
            tabs[i].$el.css({'position': 'static', 'margin-left': 0+'px'})
                .removeClass('active');
            i++;
        }

        var opacity;
        var d = (I+1) * cutoff_width - x;
        if (d <= min_d) {
            opacity = 0;
        } else if (d >= max_d) {
            opacity = 1;
        } else {
            opacity = 1/(max_d - min_d) * (d - min_d);
        }
        tabs[I].$el.find('.tab-arrow-right').first().css('opacity', opacity);
    }, 50);
});

