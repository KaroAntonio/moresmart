$('#number_button').click(function(){
	submit_number()
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
