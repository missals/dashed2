$('.wind-speed-value').each(function () {
    var deg = $(this).data('rotate') || 0;
    var rotate = 'rotate(' + $(this).data('rotate') + 'deg)';
    $(this).css({
        '-webkit-transform': rotate,
        '-moz-transform': rotate,
        '-o-transform': rotate,
        '-ms-transform': rotate,
        'transform': rotate
    });
});
