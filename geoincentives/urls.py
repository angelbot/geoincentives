import os

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('geoincentives.views',
    url(r'^$', 'home', name='home'),
    url(r'^checkin/$', 'checkin', name='checkin'),

    # Examples:
    # url(r'^$', 'geoincentives.views.home', name='home'),
    # url(r'^geoincentives/', include('geoincentives.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = urlpatterns + patterns('',
	(r'^login/$', 'django.contrib.auth.views.login'),
)
