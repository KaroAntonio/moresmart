$('#number_button').click(function(){
	submit_number()
});

var options = $("#options");
result = ['opt1','opt2']

$.each(result, function() {
    options.append($("<option />").val(this).text(this));
});

function submit_number() {
    console.log('submit_number',$('#input-box').val())
    var request = $.ajax({
      url: "/post_number/",
      type: "POST",
      data: $('#input-box').val(),
      dataType: "html"
    });
    request.done(function(data) {
      console.log(data)
        //give notification that the number is sent
    });
}
