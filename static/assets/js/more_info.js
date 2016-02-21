$('#submit-info').click(function(){
	submit_info()
});

subjects = [];

$('#add_subject_button').click(function(){
    subj = [$( "#options-1" ).val(),$( "#options-2" ).val(),$( "#options-3" ).val()];
    subjects.push(subj);
    addRow(subj);
})

var options = [$("#options-1"),$("#options-2"),$("#options-3")];

result = ['opt1','opt2']

for (var i=0; i < options.length; i++) {
    $.each(result, function() {
        options[i].append($("<option />").val(this).text(this));
    });
}

function addRow(cols) {
    // Find a <table> element with id="myTable":
    var table = document.getElementById("selected-subjects");

    // Create an empty <tr> element and add it to the 1st position of the table:
    var row = table.insertRow(0);

    // Insert new cells (<td> elements) at the 1,2,3 position of the "new" <tr> element:
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);

    // Add some text to the new cells:
    cell1.innerHTML = cols[0];
    cell2.innerHTML = cols[1];
    cell3.innerHTML = cols[2];
}

function submit_info() {
    var info = { 
        'number': $('#input-number').val(),
        'price': $('#input-price').val(),
        'subjects': subjects,
    }
    var request = $.ajax({
      url: "/post_number/",
      type: "POST",
      data: info,
      dataType: "html"
    });
    request.done(function(data) {
      console.log(data)
        //give notification that the number is sent
      $('#input-fields').css('display','none')
      $('#key-field').html('<b>KEY: 123asdf567</b>')
    });
}
