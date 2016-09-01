$(document).ready(function() {

    // if the browser does not support background-blend-mode,
    // implement the backup plan
    if(typeof window.getComputedStyle(document.body).backgroundBlendMode == 'undefined') {
        console.log('falling back to css without background-blend-mode');
        $('body').addClass('no-background-blend-mode');
    }

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
