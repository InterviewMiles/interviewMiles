function login(){
	$.ajax({
	    url : url,
	    type: "POST",
	    data : {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
	    dataType : "json",
	    success: function( data ){
	        // do something
	    }
	});
}