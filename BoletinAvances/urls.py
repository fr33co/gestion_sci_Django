from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^', include('BoletinAvances.apps.login.urls')),
    url(r'^administracion/', include('BoletinAvances.apps.listas.urls')),
    url(r'^administracion/', include('BoletinAvances.apps.contactos.urls')),
    url(r'^boletines/', include('BoletinAvances.apps.boletines.urls')),
    url(r'^avances/', include('BoletinAvances.apps.avances.urls')),
	url(r'^primerasplanas/', include('BoletinAvances.apps.primerasplanas.urls')),
)