$(document).ready(function(){

    // TODO save this as a cookie instead so it works when going between
    // the different pages of vMLK website
    var playback_position = 0;

    // Works in Firefox and Safari. Does not work in Chrome
    var sync_playback = _.throttle(function() {
        playback_position = this.currentTime;
        console.log('syncing playback positions to', playback_position);
        $('.my_audio_class').each(function() {
            this.currentTime = playback_position;
        });
    }, 500);

    $('.my_audio_class').on('pause', sync_playback);

});
