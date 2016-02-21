$('#submit-info').click(function(){
	submit_info()
});

$('#key-field').css('display','none')

subjects = [];

$('#add_subject_button').click(function(){
    subj = [$( "#options-1" ).val(),$( "#options-2" ).val(),$( "#options-3" ).val()];
    subjects.push(subj);
    addRow(subj);
})

var options = [$("#options-1"),$("#options-2"),$("#options-3")];

var course, school, department;

$.get( "/all_courses/", function( data ) {
    parsed = JSON.parse(data)
    course = parsed['course']
    school = parsed['school']
    department = parsed['department']
    console.log(course)
    
    $.each(school, function() {
        options[0].append($("<option />").val(this).text(this));
    });
    $.each(department, function() {
        options[1].append($("<option />").val(this).text(this));
    });
    $.each(course, function() {
        options[2].append($("<option />").val(this).text(this));
    });     
});


function submit_info() {
    var info = { 
        'price': $('#input-price').val(),
        'school': $( "#options-1" ).val(),
        'department': $( "#options-2" ).val(),
        'course': $( "#options-3" ).val(),
    }
    console.log(JSON.stringify(info))
    var request = $.ajax({
      url: "/request_tutor/",
      type: "POST",
      data: JSON.stringify(info),
      dataType: "html"
    });
    request.done(function(data) {
      console.log(data)
        //give notification that the number is sent
      $('#key-field').css('display','inline-block')
      //$('#key-field').html('<b>TEXT KEY: 123asdf567 to +14387937578</b>')
    });
}






