(function(){
        var $html=document.querySelector('html');
        var $body=document.querySelector("body");
        var psdsize=parseInt($body.getAttribute('data-psd-width'));
        var htmlfont=$body.offsetWidth/psdsize*100+'px';
        $html.style.fontSize=htmlfont
		$body.style.opacity=1
        window.onresize=function(){
            htmlfont=$body.offsetWidth/psdsize*100+'px';
            $html.style.fontSize=htmlfont
        };
})();