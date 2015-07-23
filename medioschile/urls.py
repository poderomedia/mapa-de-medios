from . import views
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from rest_framework import routers
from medioschile import serializers

router = routers.DefaultRouter()
router.register(r'propietarios', views.PropietarioViewSet)
router.register(r'sociedades', views.SociedadViewSet)
router.register(r'tiposociedades', views.TipoSociedadViewSet)
router.register(r'grupos', views.GrupoViewSet)
router.register(r'paises', views.PaisSociedadViewSet)
router.register(r'fuentes', views.FuenteViewSet)
router.register(r'escritos', views.EscritoViewSet)
router.register(r'canaltvs', views.CanalTVViewSet)
router.register(r'generoradios', views.GeneroRadioViewSet)
router.register(r'generoescritos', views.GeneroEscritoViewSet)
router.register(r'generocanaltvs', views.GeneroCanalTVViewSet)
router.register(r'generomediodigitales', views.GeneroMedioDigitalViewSet)
router.register(r'radios', views.RadioViewSet)
router.register(r'mediodigitales', views.MedioDigitalViewSet)
router.register(r'ejecutivos', views.EjecutivoViewSet)
router.register(r'empresarios', views.EmpresarioViewSet)
router.register(r'articulos', views.ArticuloViewSet)
router.register(r'autores', views.AutorViewSet)

urlpatterns = [
	url(r'^index/$', 'medioschile.views.index', name='index'),
    url(r'^acercade/$', 'medioschile.views.acercade', name='acercade'),
	url(r'^consultadirecta/$', 'medioschile.views.consultadirecta', name='consultadirecta'),
    url(r'^metodologia/$', 'medioschile.views.metodologia', name='metodologia'),
    url(r'^privacidad/$', 'medioschile.views.privacidad', name='privacidad'),
    url(r'^datos/$', 'medioschile.views.datos', name='datos'),
    url(r'^codigo/$', 'medioschile.views.codigo', name='codigo'),
    url(r'^contacto/$', 'medioschile.views.contacto', name='contacto'),
    url(r'^aporta/$', 'medioschile.views.aporta', name='aporta'),
    url(r'^analisiscl/$', 'medioschile.views.analisiscl', name='analisiscl'),
    url(r'^analisiscol/$', 'medioschile.views.analisiscol', name='analisiscol'),
    url(r'^fuente/$', views.FuenteList.as_view(), name='fuenteslist'),
    url(r'^analisis/$', views.AnalisisList.as_view(), name='analisislist'),
    url(r'^analisis/(?P<pk>\d+)/$', views.AnalisisDetail.as_view(), name='analisisdetail'),
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
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]