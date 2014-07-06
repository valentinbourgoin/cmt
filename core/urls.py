from django.conf.urls import patterns, include, url

import views


urlpatterns = patterns('',
	# Homepage
	url('^$', views.homepage, name="homepage"),
)
