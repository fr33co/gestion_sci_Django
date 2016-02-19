from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required, permission_required
from BoletinAvances.apps.login.views import *
from django.conf import settings


urlpatterns = patterns('BoletinAvances.apps.login.views',
    url(r'^$', 'login_view', name='login_view'),
    url(r'^logout/', 'logout_view', name='logout_view'),
    url(r'^tablero/$','graph_view', name='graph_view'),
    url(r'^administracion/usuarios/$','usuarios_view', name='usuarios'),
    url(r'^administracion/anadirusuario/','register_view',name='anadirusuario'),
    url(r'^administracion/usuariosin-(?P<id>.*)/$','singleusuarios_view',name='singleusuarios_view'),
    url(r'^administracion/usuariodel-(?P<id>.*)/$','singleusuarios_delete',name='singleusuarios_delete'),
    url(r'^administracion/usuarioup-(?P<slug>[-\w]+)/$', login_required(UsuariosUpdate.as_view()), name='updateusuarios_view'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)