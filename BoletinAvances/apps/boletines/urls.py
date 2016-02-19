from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings
from BoletinAvances.apps.boletines.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('BoletinAvances.apps.boletines.views',
    url(r'^ver/?$', login_required(BoletinesListView.as_view()), name='ver_boletines'),
    url(r'^enviar/?$', login_required(BoletinesAddView.as_view()), name='enviar_boletin'),
    url(r'^detalle-(?P<slug>[-\w]+)/$', login_required(BoletinesDetailView.as_view()), name='singleboletin_view'),
    url(r'^Boletindel-(?P<slug>[-\w]+)/$', login_required(BoletinesDeleteView.as_view()), name='boletin_delete'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)