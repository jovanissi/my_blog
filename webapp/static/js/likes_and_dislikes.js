$(document).on('submit', '#like',function(e){
	e.preventDefault();
	$.ajax({
		type: 'POST',
		url : 'like',
		data:{
			article_pk : $('#article_pk').val(),
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]'),

		},
		success:function(){
			alert('Liked');
		}

	});
});

$(document).on('submit', '#dislike',function(e){
	e.preventDefault();
	$.ajax({
		type: 'POST',
		url : 'dislike',
		data:{
			article_pk : $('#article_pk').val(),
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]'),

		},
		success:function(){
			alert('Liked');
		}

	});
});

// $("#likes").click(function(){
// 	alert('disliked!');
// 	event.preventDefault();
// 	var element = $(this);
// 	$.ajax({
// 		url : '/all_likes/',
// 		type : 'POST',
// 		data: {comments_id: element.attr("data-id")},
// 		success : function(response){
// 			element.html(' ' + response);
// 		}

// 	});
// });

// function getCookie(name){
// 	var cookieValue = null;
// 	if (document.cookie && document.cookie != ''){
// 		var cookies = document.cookie.split(';');
// 		for (var i = 0; i < cookies.length; i++){
// 			var cookie = jQuery.trim(cookies[i]);
// 			if(cookie.substring(0, name.lenght + 1) == (name + '=')){
// 				cookieValue = decodeURIComponent(
// 							  cookie.substring(name.length + 1));
// 				break;
// 			}
// 		}
// 	}
// 	return cookieValue;
// }
// var csrftoken = getCookie('csrftoken');

// function csrfSafeMethod(Method) {
// 	return(/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
// }

// $.ajaxSetup({
// 	beforeSend: function(xhr, settings){
// 		if (!csrfSafeMethod(settings.type) && !this.crossDomain){
// 			xhr.setRequestHeader("X-CSRFToken", csrftoken)
// 		}
// 	}
// })