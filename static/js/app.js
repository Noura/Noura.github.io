$(window).load(function() {
    $('.tile').click(function(e) {
        var $this = $(this);
        var project_id = $this.data('project');
        $('.container').addClass('hide');
        $('.container.project-page[data-project="'+project_id+'"]').removeClass('hide');
    });
    $('.close-project-page').click(function(e) {
        $('.container').addClass('hide');
        $('.container.tiles').removeClass('hide');
    });
});
