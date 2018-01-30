from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^withings_data/', include('withings_data.urls')),
	url(r'^admin/', include(admin.site.urls)),
)