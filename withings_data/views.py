from django.http import HttpResponse
from django.shortcuts import render, redirect
from models import User
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.contrib.auth.decorators import login_required


def login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	print 'user , authenticate ', user
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponse("Sucessful", status=200)
		else:
			return render(request, 'withings_data/get_data.html')

	else:
		# Return an 'invalid login' error message.
		return HttpResponse("Sucessful", status=200)






def logout_view(request):
	logout(request)
	# Redirect to a success page.

@login_required
def withings_page(request):
	return render(request, 'withings_data/get_data.html')

@login_required
def get_data(request):
	email = request.POST.get("email", "")
	password = request.POST.get("password", "")

	if str(email) is '' or str(password) is '':
		return HttpResponse('No Email and/or Password', status=403)
	else:
		# print 'Email: %s, Password: %s' % (email, password)
		User.objects.get_or_create(first_name='fname', last_name='lname', email=email, password=password)
		return HttpResponse("Sucessful", status=200)
