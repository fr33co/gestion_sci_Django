from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings
from BoletinAvances.apps.resumen.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('BoletinAvances.apps.avances.views',

    #NoticiaResumen
    url(r'^NoticiaResumenver/?$', login_required(NoticiaResumenListView.as_view()), name='ver_noticia_resumen'),
    url(r'^NoticiaResumendetalle-(?P<slug>[-\w]+)/$', login_required(NoticiaResumenDetailView.as_view()), name = 'noticia_resumen_detalle'),
    url(r'^NoticiaResumenenviar/?$', login_required(NoticiaResumenAddView.as_view()), name = 'enviar_noticia_resumen'),
    url(r'^NoticiaResumendel-(?P<slug>[-\w]+)/$', login_required(NoticiaResumenDeleteView.as_view()), name = 'noticia_resumen_delete'),

    #Resumen
    url(r'^Resumenver/?$', login_required(ResumenListView.as_view()), name='ver_resumen'),
    url(r'^Resumendetalle-(?P<slug>[-\w]+)/$', login_required(ResumenDetailView.as_view()), name = 'resumen_detalle'),
    url(r'^Resumenenviar/?$', login_required(ResumenAddView.as_view()), name = 'enviar_resumen'),
    url(r'^Resumendel-(?P<slug>[-\w]+)/$', login_required(ResumenDeleteView.as_view()), name = 'resumen_delete'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
