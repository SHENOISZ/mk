/**
 * Created by marcelo on 20-09-2015.
 **/

/* function Menu scrolltop */

$('#home').click(function () {
     $('html body').animate({ 'scrollTop': '0px' }, 'speed');
});

$('#contact').click(function () {
     $('html body').animate({ 'scrollTop': ($('#formulario').offset().top - 60) }, 'speed');
});

/* final function Menu scrolltop */


/* funcao menu desktop/mobile */

function navbar() {
     if ($('html body').width() < 767) {
         $('.navbar-color').css('background', '#666');
     } else {
         if (200 < $('html body').scrollTop()) {
            $('.navbar-color').css('background', '#333');
        } else {
            $('.navbar-color').css('background', 'transparent');
        }
     }
}

setInterval('navbar()', 10);

/* final funcao menu desktop/mobile */

/* emotions */

function emotions() {
    html = $('.comments').html();
    html = html.replace(':)', '<img src="/media/images/emotions/smile.png" width="14">');
    html = html.replace(';)', '<img src="/media/images/emotions/blink.png" width="14">');
    html = html.replace(':d', '<img src="/media/images/emotions/full-smile.png" width="14">');
    html = html.replace(':D', '<img src="/media/images/emotions/full-smile.png" width="14">');
    html = html.replace(':(', '<img src="/media/images/emotions/sad.png" width="14">');
    html = html.replace(':/', '<img src="/media/images/emotions/perturged.png" width="14">');
    $('.comments').html(html);
}

emotions();

/* final emotions */

function sender() {
    $('.required1').css('display', 'none');
    $('.required2').css('display', 'none');
    $('.required3').css('display', 'none');
    $('#nome').css('border', '1px solid @form_color');
    $('#email').css('border', '1px solid @form_color');
    $('#comentario').css('border', '1px solid @form_color');
    var nome = $('#nome').val(), email = $('#email').val(), comment = $('#comentario').val(), publicado = Date();
    var publish = publicado.substr(0, 15)+ 'spacespace-spacespace'+ publicado.substr(15, 10);

    if (nome != '' && email != '' && comment != '') {
        $.ajax({ type: 'GET', url: '/ajax/', data: 'nome='+ nome+ '&email='+ email+ '&comment='+ comment+ '&publish='+ publish, success: function (data) {
            $('form')[0].reset();
            var nome_ = data.split('=')[1]; nome_ = nome_.split(';')[0];
            var comment_ = data.split('=')[3]; comment_ = comment_.split(';')[0];
            var publish_ = data.split('=')[4]; publish_ = publish_.split(';')[0];
            var texto = '<div class="col-md-4 lateral"></div><div class="col-md-8 text-center"><div class="comentario-container"> <h4 class="comentario-color text-left"><span class="contorno-icon"><i class="glyphicon glyphicon-user"></i></span>&nbsp;&nbsp;&nbsp;'+nome_ +':</h4> <h5 class="comentario-color text-center">'+comment_ +'</h5> <br> <h6 class="comentario-color text-right">publicado em:&nbsp;'+publish_ +'</h6></div></div>';
            var html = texto+ $('.comments').html();
            $('.comments').html(html);
            emotions();
        }});
    } else {
           $('form')[0].reset();
        if (nome == '') {
            $('.required1').css('display', 'block');
            $('#nome').css('border', '1px solid #ff0000');
        }
        if (email == '') {
            $('.required2').css('display', 'block');
            $('#email').css('border', '1px solid #ff0000');
        }
        if (comment == '') {
            $('.required3').css('display', 'block');
            $('#comentario').css('border', '1px solid #ff0000');
        }
    }
}
