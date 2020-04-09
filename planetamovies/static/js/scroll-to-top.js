$('document').ready(function() {
    $('#uptotop').click(function(){
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    });
})

$(window).scroll(function(){
    if(window.pageYOffset > 300) {
        $('#uptotop').show();
    } else {
        $('#uptotop').hide();
    }
})