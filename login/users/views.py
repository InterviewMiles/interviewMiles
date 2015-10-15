from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from users.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from users.models import *
from users.serializers import *
from django.contrib.auth.models import User

import cgi

class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON.
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

# Create your views here.
def register(request):
	# Like before, get the request's context.
	context = RequestContext(request)
	# A boolean value for telling the template whether the registration was successful.
	# Set to False initially. Code changes value to True when registration succeeds.
	registered = False

	# If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':
		# Attempt to grab information from the raw form information.
		# Note that we make use of both UserForm and UserProfileForm.
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		full_name = cgi.escape(request.POST['full_name'].strip()) 
		username = cgi.escape(request.POST['username'].strip())
		email = cgi.escape(request.POST['email'].strip())
		contact_no = cgi.escape(request.POST['contact_no'].strip())
		password = cgi.escape(request.POST['password'].strip())
		password2 = cgi.escape(request.POST['password2'].strip())

		if not full_name or not username or not email or not password or not password2 :
			result = UserResponce("Required feild missing")
			serializer = UserResponceSerializer(result, many=False)
			return JSONResponse(serializer.data)
		elif password != password2 :
			result = UserResponce("Password mismatch")
			serializer = UserResponceSerializer(result, many=False)
			return JSONResponse(serializer.data)
		result = UserResponce("invalid")
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			user = User.objects.create_user(username=username,email=email,first_name=full_name)
			user.set_password(password)
			user.save()
			userProfile = UserProfile()
			userProfile.user = user
			userProfile.contact_no = contact_no
			userProfile.save();
			registered = True
			result = UserResponce("success")
			serializer = UserResponceSerializer(result, many=False)
			return JSONResponse(serializer.data)

		result = UserResponce("Duplicate username")
		serializer = UserResponceSerializer(result, many=False)
		return JSONResponse(serializer.data)

	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
		# Render the template depending on the context.
		return render_to_response(
				'register.html',
				{'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
				context)

def user_login(request):
	# Like before, obtain the context for the user's request.
	context = RequestContext(request)
	# If the request is a HTTP POST, try to pull out the relevant information.
	if request.method == 'POST':
		# Gather the username and password provided by the user.
		# This information is obtained from the login form.
		username = cgi.escape(request.POST['username'].strip())
		password = cgi.escape(request.POST['password'].strip())

		# Use Django's machinery to attempt to see if the username/password
		# combination is valid - a User object is returned if it is.
		user = authenticate(username=username, password=password)

		# If we have a User object, the details are correct.
		# If None (Python's way of representing the absence of a value), no user
		# with matching credentials was found.
		if user:
			# Is the account active? It could have been disabled.
			if user.is_active:
				# If the account is valid and active, we can log the user in.
				# We'll send the user back to the homepage.
				login(request, user)
				result = UserResponce("success")
				serializer = UserResponceSerializer(result, many=False)
				return JSONResponse(serializer.data)
			else:
				# An inactive account was used - no logging in!
				result = UserResponce("Account disabled")
				serializer = UserResponceSerializer(result, many=False)
				return JSONResponse(serializer.data)
		else:
			# Bad login details were provided. So we can't log the user in.
			result = UserResponce("Invalid login details")
			serializer = UserResponceSerializer(result, many=False)
			return JSONResponse(serializer.data)
	# The request is not a HTTP POST, so display the login form.
	# This scenario would most likely be a HTTP GET.
	else:
		# No context variables to pass to the template system, hence the
		# blank dictionary object...
		return render_to_response('login.html', {}, context)

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
	# Since we know the user is logged in, we can now just log them out.
	logout(request)

	# Take the user back to the homepage.
	return HttpResponseRedirect('/users/')

def check_username(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = cgi.escape(request.POST['username'].strip())
		result = UserResponce("invalid")
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			result=UserResponce("valid")
		serializer = UserResponceSerializer(result, many=False)
		return JSONResponse(serializer.data)
	else:
		return render_to_response('check_user.html', {}, context)