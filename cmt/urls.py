from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Core
	url('', include('core.urls')),

	# Pronostic
	url('^pronostic/', include('pronostic.urls')),

    # Allauth
    url(r'^accounts/', include('allauth.urls')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)
