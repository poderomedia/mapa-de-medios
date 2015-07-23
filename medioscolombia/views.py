from django.db import models
from django.shortcuts import render,render_to_response
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic import DetailView
from medioscolombia.models import Ejecutivo,Empresario,GeneroEscrito,Region,Ciudad,Sector,Periodicidad,Propietario,TipoSociedad,PaisSociedad,Sociedad,Grupo,Escrito,GeneroRadio,Radio,GeneroCanalTV,CanalTV,GeneroMedioDigital,MedioDigital,Autor,Fuente,TipoDocumento,Regulacion,CargoEjecutivo,Cargo
from medioschile.models import Articulo
from rest_framework import viewsets
from medioscolombia.serializers import *

def index(request):
	articulos = Articulo.objects.filter(destacado = 1)
	return render(request, 'medioscolombia/index.html', {"articulos":articulos})

def consultadirecta(request):
	return render(request, 'medioscolombia/consultadirecta.html')

def metodologia(request):
	return render(request, 'medioscolombia/metodologia.html')

def datos(request):
	return render(request, 'medioscolombia/datos.html')

def codigo(request):
	return render(request, 'medioscolombia/codigo.html')

def analisis(request):
	return render(request, 'medioscolombia/analisis.html')

def acercade(request):
	return render(request, 'medioscolombia/acercade.html')

def contacto(request):
	return render(request, 'medioscolombia/contacto.html')

def aporta(request):
	return render(request, 'medioscolombia/aporta.html')

def privacidad(request):
	return render(request, 'medioscolombia/privacidad.html')

class EscritoList(ListView):
	model = Escrito
	context_object_name = 'escrito_list'
	template_name = 'medioscolombia/escrito_list.html'

class EscritoDetail(DetailView):
	model = Escrito
	context_object_name = 'escrito_detail'
	template_name = 'medioscolombia/escrito_detail.html'

class CanalTVList(ListView):
	model = CanalTV
	context_object_name = 'canaltv_list'
	template_name = 'medioscolombia/canaltv_list.html'

class CanalTVDetail(DetailView):
	model = CanalTV
	context_object_name = 'canaltv_detail'
	template_name = 'medioscolombia/canaltv_detail.html'

class RadioList(ListView):
	model = Radio
	context_object_name = 'radio_list'
	template_name = 'medioscolombia/radio_list.html'

class RadioDetail(DetailView):
	model = Radio
	context_object_name = 'radio_detail'
	template_name = 'medioscolombia/radio_detail.html'

class MedioDigitalList(ListView):
	model = MedioDigital
	context_object_name = 'mediodigital_list'
	template_name = 'medioscolombia/mediodigital_list.html'

class MedioDigitalDetail(DetailView):
	model = MedioDigital
	context_object_name = 'mediodigital_detail'
	template_name = 'medioscolombia/mediodigital_detail.html'

class PropietarioDetail(DetailView):
	model = Propietario
	context_object_name = 'propietario_detail'
	template_name = 'medioscolombia/propietario_detail.html'

class PropietarioList(ListView):
	model = Propietario
	context_object_name = 'propietario_list'
	template_name = 'medioscolombia/propietario_list.html'

class GrupoDetail(DetailView):
	model = Grupo
	context_object_name = 'grupo_detail'
	template_name = 'medioscolombia/grupo_detail.html'

class GrupoList(ListView):
	model = Grupo
	context_object_name = 'grupo_list'
	template_name = 'medioscolombia/grupo_list.html'

class RegulacionDetail(DetailView):
	model = Regulacion
	context_object_name = 'regulacion_detail'
	template_name = 'medioscolombia/regulacion_detail.html'

class RegulacionList(ListView):
	model = Regulacion
	context_object_name = 'regulacion_list'
	template_name = 'medioscolombia/regulacion_list.html'

class FuenteList(ListView):
	model = Fuente
	context_object_name = 'fuente_list'
	template_name = 'medioscolombia/fuente_list.html'

class PropietarioViewSet(viewsets.ModelViewSet):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer

class TipoSociedadViewSet(viewsets.ModelViewSet):
	queryset = TipoSociedad.objects.all()
	serializer_class = TipoSociedadSerializer

class SociedadViewSet(viewsets.ModelViewSet):
    queryset = Sociedad.objects.all()
    serializer_class = SociedadSerializer

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

class PaisSociedadViewSet(viewsets.ModelViewSet):
    queryset = PaisSociedad.objects.all()
    serializer_class = PaisSociedadSerializer

class RadioViewSet(viewsets.ModelViewSet):
    queryset = Radio.objects.all()
    serializer_class = RadioSerializer

class EscritoViewSet(viewsets.ModelViewSet):
    queryset = Escrito.objects.all()
    serializer_class = EscritoSerializer

class CanalTVViewSet(viewsets.ModelViewSet):
    queryset = CanalTV.objects.all()
    serializer_class = CanalTVSerializer

class MedioDigitalViewSet(viewsets.ModelViewSet):
    queryset = MedioDigital.objects.all()
    serializer_class = MedioDigitalSerializer

class GeneroRadioViewSet(viewsets.ModelViewSet):
    queryset = GeneroRadio.objects.all()
    serializer_class = GeneroRadioSerializer

class GeneroCanalTVViewSet(viewsets.ModelViewSet):
    queryset = GeneroCanalTV.objects.all()
    serializer_class = GeneroCanalTVSerializer

class GeneroEscritoViewSet(viewsets.ModelViewSet):
    queryset = GeneroEscrito.objects.all()
    serializer_class = GeneroEscritoSerializer

class GeneroMedioDigitalViewSet(viewsets.ModelViewSet):
    queryset = GeneroMedioDigital.objects.all()
    serializer_class = GeneroMedioDigitalSerializer

class GeneroRadioViewSet(viewsets.ModelViewSet):
    queryset = GeneroRadio.objects.all()
    serializer_class = GeneroRadioSerializer

class FuenteViewSet(viewsets.ModelViewSet):
    queryset = Fuente.objects.all()
    serializer_class = FuenteSerializer

class EmpresarioViewSet(viewsets.ModelViewSet):
    queryset = Empresario.objects.all()
    serializer_class = EmpresarioSerializer

class EjecutivoViewSet(viewsets.ModelViewSet):
    queryset = Ejecutivo.objects.all()
    serializer_class = EjecutivoSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer