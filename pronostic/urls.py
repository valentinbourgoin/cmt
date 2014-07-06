from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
	# Pronostic page
	url('^$', views.matchday, name="matchday"),
)