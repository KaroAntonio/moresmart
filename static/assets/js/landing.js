$( document ).ready(function() {
    $.get( "/get_google/", function( data ) {
        $('#google-link').click(function() {
        window.location.href = data;})
    });
});

