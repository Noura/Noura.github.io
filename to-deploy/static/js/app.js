$(window).load(function() {
    var $body = $('body');
    var tab_content_width = 800;
    var tab_width = 102;
    var cutoff_width = tab_content_width - tab_width;
    var tabs = [];
    $('.tab').each(function() {
        tabs.push({$el: $(this), fixed: false});
    });

    $('.tab').on('click', function() {
        var i = $(this).data('i');
        $body.animate({scrollLeft: i*tab_content_width}, 500);
    });

    setInterval(function() {
        var x = Math.max(0, $body.scrollLeft());
        var i = Math.floor(x / cutoff_width);
        if (i >= tabs.length) {
            return;
        }
        var margin_left = i*tab_width;
        var offset = (i+1)*tab_content_width;
        if (!tabs[i].fixed) {
            tabs[i].$el.css({'position': 'fixed', 'margin-left': margin_left+'px'});
            tabs[i].fixed = true;
        }
        for (var j = i + 1; j < tabs.length; j++) {
            if (tabs[j].fixed) {
                tabs[j].$el.css({'position': 'static', 'margin-left': '0'});
                tabs[j].fixed = false;
            }
        }
        if (i + 1 < tabs.length) {
            tabs[i+1].$el.css('margin-left', offset+'px');
        }
    }, 50);
});

