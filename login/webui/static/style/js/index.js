function login(){
	$.ajax({
	    url : '/users/login/',
	    type: "POST",
	    data : $("#login_form" ).serialize(),
	    dataType : "json",
	    success: function( data ){
	    	if( data.result == "success"){
	        	alert("login sucessfull");
	        	location.reload();
	        }
	        else
	        	alert(data.result);
	    }
	});
	return false;
}
function register(){
	$.ajax({
	    url : '/users/register/',
	    type: "POST",
	    data : $("#user_form" ).serialize(),
	    dataType : "json",
	    success: function( data ){
	    	if( data.result == "success"){
	        	alert("registeration sucessfull");
	        	location.reload();
	        }
	        else
	        	alert(data.result);
	    },
	    error: function (xhr, ajaxOptions, thrownError) {
	        alert(xhr.status);
	        alert(thrownError);
	    }
	});
	return false;
}