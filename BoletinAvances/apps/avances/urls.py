from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings
from BoletinAvances.apps.avances.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('BoletinAvances.apps.avances.views',
    #Diarios
    url(r'^Diariosver/?$', login_required(DiariosListView.as_view()), name='ver_diarios'),
    url(r'^Diariosenviar/?$', login_required(DiarioAddView.as_view()), name='enviar_diarios'),
    url(r'^Diariodetalle-(?P<slug>[-\w]+)/$', login_required(DiariosDetailView.as_view()), name='singlediarios_view'),
    url(r'^Diariosdel-(?P<slug>[-\w]+)/$', login_required(DiariosDeleteView.as_view()), name='diario_delete'),
    #Noticias
    url(r'^Noticiasver/?$', login_required(NoticiasListView.as_view()), name='ver_noticias'),
    url(r'^Noticiasenviar/?$', login_required(NoticiasAddView.as_view()), name='enviar_noticia'),
    url(r'^Noticiasdetalle-(?P<slug>[-\w]+)/$', login_required(NoticiasDetailView.as_view()), name='singlenoticias_view'),
    #Avances
    url(r'^Avancesver/?$', login_required(AvancesListView.as_view()), name='ver_avances'),
    url(r'^Avancesenviar/?$', login_required(AvancesAddView.as_view()), name='enviar_avance'),
    url(r'^Avancesdetalle-(?P<slug>[-\w]+)/$', login_required(AvancesDetailView.as_view()), name='singleavance_view'),
    url(r'^Avancesdel-(?P<slug>[-\w]+)/$', login_required(AvancesDeleteView.as_view()), name='avance_delete'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
