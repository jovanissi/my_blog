$(document).ready(function(){
	alert("Thank you for your comment!");
	window.history.back();
	
});

// $("#comments_button").click(function(event){
// 	event.preventDefault();
// 	var $form = $( this ),
// 		url = $form.attr('post');

// 	var posting = $.post(url, {article_id: ("#article_id_form_catcher").val(), user_name: ("#name").val(), comment: ("#comment_text").val()});
// 	posting.done(function(data){
// 		alert('Thank you for your comment!!!')
// 	});
// });