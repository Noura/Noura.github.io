$(window).load(function() {
    $('.tile').click(function(e) {
        var $this = $(this);
        var project_id = $this.data('project');
        $('.container').addClass('hide');
        $('.container.project-page[data-project="'+project_id+'"]').removeClass('hide');
        window.location.hash = project_id;
    });
    $('.close-project-page').click(function(e) {
        $('.container').addClass('hide');
        $('.container.tiles').removeClass('hide');
        window.location.hash = '';
    });
    function sync_page() {
        if (window.location.hash.length > 1) {
            var project_id = window.location.hash.slice(1);
            ($('.tile[data-project="'+project_id+'"]')[0]).click();
        } else {
            $('.container').addClass('hide');
            $('.container.tiles').removeClass('hide');
        }
    }
    window.onhashchange = sync_page;
    sync_page();
});
