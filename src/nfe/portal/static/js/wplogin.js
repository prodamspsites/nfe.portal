// JScript File
var url = {
    login       : "https://nfe.prefeitura.sp.gov.br/login.aspx",
    senha       : "https://nfe.prefeitura.sp.gov.br/login.aspx",
    novo        : "https://nfe.prefeitura.sp.gov.br/login.aspx?new=true",
    certificado : "https://nfe.prefeitura.sp.gov.br/loginicp.aspx"
}

$(document).ready(function() {
    cmdLoginSistema  = $("#enviar").click(loginSistema);
    cmdEsqueciSenha  = $("#linkEsqueciSenha").click(esqueciSenha);
    cmdNaoCadastrado = $("#linkNaoCadastrado").click(naoCadastrado);
    cmdCertificado   = $("#linkCertificado").click(loginCertificado);
    loginForm        = $("#wploginform");

    j_username = $("#j_username");
    j_password = $("#j_password");

    j_username.focus(function(){
        $(this).setMask("99999999999999").val("");
    });

    j_username.blur(function(){
        var j_username = $(this).val()
        if(j_username.length <= 11)
            $(this).setMask("999.999.999-99");
        if(j_username.length > 11)
            $(this).setMask("99.999.999/9999-99");
        validateCpfCnpj();
    })

    loginForm.submit(validateCpfCnpj);
});


function loginSistema(e) {
    $("#enviar").attr("disabled", "disabled");
    e.preventDefault();
    $("#j_command").val("executarLogin");

    var isValidPassword = validatePassword();
    var isValidCpfCnpj  = validateCpfCnpj();

    if(isValidPassword && isValidCpfCnpj) {
        loginForm.attr("action", url.login).submit();
    } else {
        $("#enviar").removeAttr("disabled");
    }
}

function loginCertificado(e) {
    e.preventDefault();
    loginForm.unbind("submit");
    loginForm.attr("action", url.certificado).submit();
}

function esqueciSenha(e) {
    e.preventDefault();
    $("#j_command").val("recuperarSenha");
    loginForm.attr("action", url.senha).submit();
}

function naoCadastrado(e) {
    e.preventDefault();
    $("#j_command").val("solicitarSenha");
    loginForm.attr("action", url.novo).submit();
}

function validateCpfCnpj() {
    if(j_username.val() == "") {
        j_username.addClass("erro");
        j_username.focus()
        return false;
    }
    else {
        j_username.removeClass("erro");
    }

    return true;
}

function validatePassword() {
    if(j_password.val() == "") {
        j_password.addClass("erro");
        j_password.focus()
        return false;
    }
    else {
        j_password.removeClass("erro");
    }

    return true;
}
