$(document).ready(function() {
    function sync_pages() {
        if (window.location.hash.length > 1) {
            // show a project page
            var project_id = window.location.hash.slice(1);
            var $tile = ($('.tile[data-project="'+project_id+'"]')[0]);
            $('.container').addClass('hide');
            $('.container.project-page[data-project="'+project_id+'"]').removeClass('hide');
        } else {
            // hide all project pages, show the home page
            $('.container').addClass('hide');
            $('.container.tiles').removeClass('hide');
        }
        $(window).scrollTop(0);
    }
    window.onhashchange = sync_pages;
    sync_pages();
});
