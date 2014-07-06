from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

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
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('',
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
	'document_root': settings.MEDIA_ROOT}))