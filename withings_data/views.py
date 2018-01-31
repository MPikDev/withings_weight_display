from django.http import HttpResponse
from django.shortcuts import render
from models import User


def withings_page(request):
	return render(request, 'withings_data/get_data.html')

def get_data(request):
	email = request.POST.get("email", "")
	password = request.POST.get("password", "")

	if str(email) is '' or str(password) is '':
		return HttpResponse('No Email and/or Password', status=403)
	else:
		# print 'Email: %s, Password: %s' % (email, password)
		User.objects.get_or_create(first_name='fname', last_name='lname', email=email, password=password)
		return HttpResponse("Sucessful", status=200)
