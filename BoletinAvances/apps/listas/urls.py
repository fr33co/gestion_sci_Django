from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings
from BoletinAvances.apps.listas.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('BoletinAvances.apps.listas.views',
    url(r'^AddlistManual/?$', login_required(ListasManualAddView.as_view()), name='addlistas'),
    url(r'^AddlistasMasivo/?$', 'upload_data_list', name='AddlistasMasivo'),
    url(r'^listas/?$', login_required(ListasListView.as_view()), name='listas'),
    url(r'^listaview-(?P<slug>[-\w]+)/$', login_required(ListasDetailView.as_view()), name='singlelistas_view'),
    url(r'^listadel-(?P<slug>[-\w]+)/$', login_required(ListaDeleteView.as_view()), name='listas_delete'),
    url(r'^listaup-(?P<slug>[-\w]+)/$', login_required(ListasUpdate.as_view()), name='listas_update'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)