from django.conf.urls import patterns, include, url
from django.contrib import admin
from withings_data import views

urlpatterns = patterns('',
	# url(r'^accounts/login/', views.login, name='login'),
	url(r'^withings_page/', views.withings_page),
	url(r'^get_data/', views.get_data),
	url(r'^admin/', include(admin.site.urls)),
)