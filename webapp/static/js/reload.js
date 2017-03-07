$(document).ready(function(){
	var name = $("#name").val(),
		comment = $("#comment_text").val();

	if (name != "" && comment != "")
		location.reload(); 
})