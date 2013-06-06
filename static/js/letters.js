function letters_control($scope) {
    var min_font_size = 50; // percent
    var max_font_size = 3000;
    var fonts = ['quicksand-light', 'quicksand-dash', 'quicksand-book', 'quicksand-bold'];
    var space_width = '50px';
    var space_height = '50px';

    $scope.letters = [];

    $scope.update = function() {
        var letters_cleared = false;
        var characters = $scope.input.split('');
        angular.forEach(characters, function(c, i) {
            if ($scope.letters.length > i &&
                c === $scope.letters[i].letter) {
                return;
            }
            if (!letters_cleared) {
                $scope.letters = $scope.letters.slice(0, i+1);
                letters_cleared = true;
            }
            var font_size = random(min_font_size, max_font_size) + '%';
            var rgb = 'rgb(' +
                random(0, 255) + ',' +
                random(0, 255) + ',' +
                random(0, 255) + ')';
            var font = fonts[random(0, fonts.length)];
            var min_width = c == ' ' ? space_width : '0';
            var min_height = c == ' ' ? space_height : '0';
            $scope.letters.push({
                letter: c,
                size:font_size,
                color: rgb,
                font: font,
                min_width: min_width,
                min_height: min_height,
            });
        });
        $scope.letters = $scope.letters.slice(0, characters.length);
    };

    function random(min, max) {
        var x = min + Math.random() * (max - min);
        return Math.floor(x);
    }
}
