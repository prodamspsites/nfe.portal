// $.urlParam = function(name){
//     var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
//     if (results==null){
//        return null;
//     }
//     else{
//        return results[1] || 0;
//     }
// }

$(document).ready(function(){


    if ($('body').hasClass('template-legislacao_view')) {
        queryString = window.location.search;
        if(queryString) {
            $('.pagination').remove();
            $('.listingBar').remove();
        }
    }

    if ($('body').hasClass('portaltype-folder') && $('body').hasClass('template-nfe_folder_contents') || $('body').hasClass('template-folder_contents')) {
        links = $('#content td a.contenttype-folder').each(function() {
            href = $(this).attr('href');
            href = href.split('/');
            if (href[href.length-1] == 'folder_contents') {
                href[href.length-1] = 'nfe_folder_contents'
            }
            $(this).attr('href', href.join('/'))
        })
    }
    //BUSCA VAZIA
    $('.searchButton').click(function(){
        if ($('#searchGadget').val() == ''){
            $('#searchGadget').focus();
            return false;
        }
    });
    //SLIDER HOME
    $('.bxslider').bxSlider({
     // auto: true,
      //autoControls: true,
    });

    //CONTATO FOCUS TOPO
    $(".acessibilidade ul li a").focus();

    //MASCARA CONTATO
    $("input#telefone").mask("(99) 9999-99999");

    //ALERTAS MOBILE
    var windowsize = $(window).width();

    if (windowsize < 800) {
        $(".informativosHome p").each(function (i) {
            var listText = []
            var listShortText = []
            var text = $(this).html();
            var len = text.length;
            var thisItens = $(this);
            listText[i] = text;

            if (len > 80) {
                //mostra o ler mais se tiver muito texto
                $(this).parent().find('.lerMaisMobile').show().attr('data-count', i);

                //guarda o texto completo
                var textoAlert = $(this).html();

                //corta o texto
                var query = text.split(" ", 13);
                    query.push('...');
                    res = query.join(' ');
                    listShortText[i] = res;
                $(this).html(res);

                //volta o texto normal
                $('.lerMaisMobile').click(function(){
                    count = $(this).data('count');
                    $(thisItens).html(listText[count]);
                    $(this).remove();
                    /*if ($(this).hasClass('mais')){
                        console.log('mais');
                        $(this).removeClass('mais');
                        $(this).text('LER MENOS');
                        $(this).addClass('menos');

                    }
                    else{
                        console.log('menos');
                        $(this).text('LER MAIS');
                        $(this).removeClass('menos');
                        $(this).addClass('mais');
                        $(thisItens).text(listShortText[count]);
                    }*/

                });
            }
        });
    }

    $('.bxslider2').bxSlider({
      pager: 'short'
    });

    $('.bxsliderAlerta').bxSlider({
       controls: true,
        nextText: 'Next',
        prevText: 'Prev',
        pager:false,
        infiniteLoop: false,
        hideControlOnEnd:true
    });

    //ACCORDEON
    $('.divAccordeon .textoAccordeon').hide();
    $('.divAccordeon h3').click(function(){
        $(this).toggleClass('active');
        $(this).next().slideToggle();
        /*if($(this).is('.active')){
        }else{
            $(this).next().slideToggle();
            $('.divAccordeon .textoAccordeon').slideUp();
        }*/

    });

//MASCARA CPF E CNPJ$(".inputAcesso.cpf").mask("999.999.999-99");
   $(".inputAcesso.cpf, #cpf-ou-cnpj").focus(function(){
    try {
        $(".inputAcesso.cpf, #cpf-ou-cnpj").unmask();
    } catch (e) {}
    });

   $(".inputAcesso.cpf, #cpf-ou-cnpj").focusout(function(){
    var tamanho = $(".inputAcesso.cpf, #cpf-ou-cnpj").val();
    tamanho = tamanho.replace(/\./g,'').replace(/\-/g,'').replace(/\//g,'').length;

    if(tamanho < 11){
        $(".inputAcesso.cpf, #cpf-ou-cnpj").mask("999.999.999-99");
    } else if(tamanho >= 11){
        $(".inputAcesso.cpf, #cpf-ou-cnpj").mask("99.999.999/9999-99");
    }
    });
    //SIDEBAR FIXO
    var scrollBottom = $(document).height() - 690;
    $(window).scroll(function() {
        if (($(this).scrollTop() > 205) && ($(this).scrollTop() < scrollBottom)) {
            $('#portal-column-two').addClass('fixo');
            $('#portal-column-content').addClass('fixo');
        }
        else{
             $('#portal-column-two').removeClass('fixo');
            $('#portal-column-content').removeClass('fixo');
        }
        //console.log($(this).scrollTop() , scrollBottom);
    });

    //CHECA A LARGURA DA TELA PARA MENU
    var windowsize = $(window).width();

    //MENU MOBILE
    $('.menuResp').click(function(){
        $('.divMenu, .menuSite').toggle();
        return false;
    });
    if (windowsize < 800) {
        $('nav.menu ul li.submenu > a').click(function(){
            $(this).parent().toggleClass('active');
            $(this).parent().find('.menuLista').toggle();
            return false;
        });
        $('.menu-mobile-segundo').click(function(){
            $('#content .menu-segundo-nivel ul').slideToggle();
        });
    }
    //MENU
    if (windowsize > 800) {
        $('nav.menu ul li.submenu').hover(function(){
            $(this).find('.menuLista').toggle();
        });
    }

    // Cria os Cookies
        if ($.cookie('contraste1') === "true") {
            $('body').addClass('contraste1');
        }

        if ($.cookie('contraste2') === "true") {
            $('body').addClass('contraste2');
        }
        if ($.cookie('resetCookie') === "true") {
            $('body').removeClass('contraste1');
            $('body').removeClass('contraste2');
        }
        if ($.cookie('librasCookie') === "ativo") {
            $('a.btn-libras').attr('id','ativo');
            $('.contEsq .divLibras').addClass('abrevideo');
            $('a.btn-libras').addClass('ativo');
        }else{
            $('.contEsq .divLibras').removeClass('abrevideo');
            $('a.btn-libras').removeClass('ativo');
            $('a.btn-libras').attr('id','');
        }

        $(".fontResizer_add").click(function () {
            maisFont();
        });
        $(".fontResizer_minus").click(function () {
            menosFont();
        });
        $(".fontResizer_reset").click(function () {
            resetFont();
        });
        (function(){
            var tam = $.cookie('tamanhoLetra');
            $('body').css("font-size",tam+"px");
        })();

        function maisFont(){
            var tamanho = $('body').css("font-size");
            var maisUm = parseInt(tamanho.substr(0, 2));
            maisUm++;
            $.cookie('tamanhoLetra', maisUm,{ path: '/' });
            $('body').css("font-size",maisUm+"px");
        }
        function menosFont(){
            var tamanho = $('body').css("font-size");
            var maisUm = parseInt(tamanho.substr(0, 2));
            maisUm--;
            $.cookie('tamanhoLetra', maisUm,{ path: '/' });
            $('body').css("font-size",maisUm+"px");
        }
        function resetFont(){
            $('body').css("font-size","16px");

            $.removeCookie('contraste2', { path: '/' });
            $.removeCookie('contraste1', { path: '/' });

            if (!($.cookie('resetCookie') === "true")) {
                $('body').removeClass('contraste1');
                $('body').removeClass('contraste2');
                $.cookie('resetCookie','true',{path:'/'});

                $('.fontSize').removeAttr('style');
                $('.fontSize15').removeAttr('style');
                $.removeCookie('tamanhoLetra', { path: '/' });
            }
            else {
                $('.fontSize').removeAttr('style');
                $('.fontSize15').removeAttr('style');
                $.removeCookie('tamanhoLetra', { path: '/' });
                $.cookie('resetCookie','false',{path:'/'});
            }
        }

        // Acoes nos botoes de acessibilidade
        $(".btn-contraste1").click(function () {
            $.removeCookie('contraste2', { path: '/' });
            $.removeCookie('resetCookie', { path: '/' });
            if (!($.cookie('contraste1') === "true")) {
                $('body').removeClass('contraste2');
                $('body').addClass('contraste1');
                $.cookie('contraste1','true',{path:'/'});
            }
            else {
                $.cookie('contraste1','false',{path:'/'});
            }
            return false;
        });
        $(".btn-contraste2").click(function () {
            $.removeCookie('contraste1', { path: '/' });
            $.removeCookie('resetCookie', { path: '/' });
            if (!($.cookie('contraste2') === "true")) {
                $('body').removeClass('contraste1');
                $('body').addClass('contraste2');
                $.cookie('contraste2','true',{path:'/'});
            }
            else {
                $.cookie('contraste2','false',{path:'/'});
            }
            return false;
        });
        $(".btn-libras").click(function () {
            if($(this).attr('id')=='ativo'){
                $('.contEsq .divLibras').removeClass('abrevideo');
                $('a.btn-libras').removeClass('ativo');
                $('a.btn-libras').attr('id','');

            }else{
                $('a.btn-libras').attr('id','ativo');
                $('.contEsq .divLibras').addClass('abrevideo');
                $('a.btn-libras').addClass('ativo');
            }
            $.cookie('librasCookie',$(this).attr('id'),{ path: '/' });

        });

});
