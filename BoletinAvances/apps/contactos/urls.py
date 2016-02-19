from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings
from BoletinAvances.apps.contactos.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('BoletinAvances.apps.contactos.views',
    url(r'^AddcontManual/?$', login_required(ContactosManualAddView.as_view()), name='AddcontManual'),
    url(r'^AddcontMasivo/?$', 'upload_data_contactos', name='AddcontMasivo'),
    url(r'^contactos/?$', login_required(ContactosListView.as_view()), name='contactos'),
    url(r'^contactosin-(?P<slug>[-\w]+)/$', login_required(ContactosDetailView.as_view()), name='singlecontactos_view'),
    url(r'^contactosdel-(?P<slug>[-\w]+)/$', login_required(ContactosDeleteView.as_view()), name='contactos_delete'),
    url(r'^contactosup-(?P<slug>[-\w]+)/$', login_required(ContactosUpdate.as_view()), name='contactos_update'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)