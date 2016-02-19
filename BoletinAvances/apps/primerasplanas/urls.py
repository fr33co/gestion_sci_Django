from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings
from BoletinAvances.apps.primerasplanas.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('BoletinAvances.apps.primerasplanas.views',
    url(r'^ver/?$', login_required(PrimerasPlanasListView.as_view()), name='ver_primerasplanas'),
    url(r'^enviar/?$', login_required(PrimerPlanaAddView.as_view()), name='enviar_primerasplanas'),
    url(r'^detalle-(?P<slug>[-\w]+)/$', login_required(PrimeraPlanaDetailView.as_view()), name='singleprimeraplana_view'),
    url(r'^del-(?P<slug>[-\w]+)/$', login_required(PrimeraPlanaDeleteView.as_view()), name='primeraplana_delete'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)