function translate() { //中文 - 英文
    window.mycallback = function(response) { $("p").html(response); }
    var s = document.createElement("script");
    s.src = "http://api.microsofttranslator.com/V2/Ajax.svc/Translate?oncomplete=mycallback&appId=A4D660A48A6A97CCA791C34935E4C02BBB1BEC1C&from=zh-cn&to=en&text=" + $("p").html();
    document.getElementsByTagName("head")[0].appendChild(s);
}
function translate2() { //英文 - 中文
    window.mycallback = function(response) { $("p").html(response); }
    var s = document.createElement("script");
    s.src = "http://api.microsofttranslator.com/V2/Ajax.svc/Translate?oncomplete=mycallback&appId=A4D660A48A6A97CCA791C34935E4C02BBB1BEC1C&from=en&to=zh-cn&text=" + $("p").html();
    document.getElementsByTagName("head")[0].appendChild(s);
}
