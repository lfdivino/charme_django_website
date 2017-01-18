$(function () {
    //incluso essa variavel para setar atributos do css depois
    var elemento = $('.element-fixed');

    $(window).scroll(function () {
    //distancia que o scroll devera rolar para aparecer o box da div
        if (($(this).scrollTop() > 850) && ($(this).scrollTop() < ($("body")["0"].clientHeight - 1000))) {
            //bloco incluso para setar o css
            elemento.css({
                'position': 'fixed',
                'bottom': '15%',
                'top': '10%'
            });

            $('.element-fixed').fadeIn();
        } else {
            $('.element-fixed').fadeOut();
        }
    });
});
