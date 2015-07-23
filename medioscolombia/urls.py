from . import views
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from medioscolombia.views import *
from rest_framework import routers
from medioscolombia import serializers

router = routers.DefaultRouter()
router.register(r'propietarios', views.PropietarioViewSet)
router.register(r'sociedades', views.SociedadViewSet)
router.register(r'tiposociedades', views.TipoSociedadViewSet)
router.register(r'grupos', views.GrupoViewSet)
router.register(r'paises', views.PaisSociedadViewSet)
router.register(r'fuentes', views.FuenteViewSet)
router.register(r'escritos', views.EscritoViewSet)
router.register(r'canaltvs', views.CanalTVViewSet)
router.register(r'radios', views.RadioViewSet)
router.register(r'generoradios', views.GeneroRadioViewSet)
router.register(r'generoescritos', views.GeneroEscritoViewSet)
router.register(r'generocanaltvs', views.GeneroCanalTVViewSet)
router.register(r'generomediodigitales', views.GeneroMedioDigitalViewSet)
router.register(r'mediodigitales', views.MedioDigitalViewSet)
router.register(r'ejecutivos', views.EjecutivoViewSet)
router.register(r'empresarios', views.EmpresarioViewSet)
router.register(r'autores', views.AutorViewSet)

urlpatterns = [
	url(r'^index/$', 'medioscolombia.views.index', name='index'),
    url(r'^contacto/$', 'medioscolombia.views.contacto', name='contacto'),
    url(r'^aporta/$', 'medioscolombia.views.aporta', name='aporta'),
    url(r'^fuente/$', views.FuenteList.as_view(), name='fuenteslist'),
    url(r'^regulacion/$', views.RegulacionList.as_view(), name='regulacioneslist'),
    url(r'^regulacion/(?P<pk>\d+)/$', views.RegulacionDetail.as_view(), name='regulaciondetail'),
    url(r'^grupo/(?P<pk>\d+)/$', views.GrupoDetail.as_view(), name='grupodetail'),
    url(r'^grupo/$', views.GrupoList.as_view(), name='gruposlist'),
    url(r'^propietario/$', views.PropietarioList.as_view(), name='propietarioslist'),
    url(r'^propietario/(?P<pk>\d+)/$', views.PropietarioDetail.as_view(), name='propietariodetail'),
    url(r'^escritolist/$', views.EscritoList.as_view(), name='escritoslist'),
    url(r'^escritolist/(?P<pk>\d+)/$', views.EscritoDetail.as_view(), name='escritodetail'),
    url(r'^canaltvlist/$', views.CanalTVList.as_view(), name='canalestvlist'),
    url(r'^canaltvlist/(?P<pk>\d+)/$', views.CanalTVDetail.as_view(), name='canaltvdetail'),
    url(r'^radiolist/$', views.RadioList.as_view(), name='radioslist'),
    url(r'^radiolist/(?P<pk>\d+)/$', views.RadioDetail.as_view(), name='radiodetail'),
    url(r'^mediodigitallist/$', views.MedioDigitalList.as_view(), name='digitaleslist'),
    url(r'^mediodigitallist/(?P<pk>\d+)/$', views.MedioDigitalDetail.as_view(), name='digitaldetail'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]