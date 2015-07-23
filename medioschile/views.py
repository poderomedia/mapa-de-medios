from django.db import models
from django.shortcuts import render,render_to_response
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic import DetailView
from medioschile.models import *
from rest_framework import viewsets
from medioschile.serializers import *
from .forms import ContactoForm
from django.core.mail import send_mail

def index(request):
	articulos = Articulo.objects.filter(destacado = 1)
	return render(request, 'medioschile/index.html', {"articulos":articulos})

def consultadirecta(request):
	return render(request, 'medioschile/consultadirecta.html')

def metodologia(request):
	return render(request, 'medioschile/metodologia.html')

def datos(request):
	return render(request, 'medioschile/datos.html')

def codigo(request):
	return render(request, 'medioschile/codigo.html')

def analisis(request):
	return render(request, 'medioschile/analisis.html')

def acercade(request):
	return render(request, 'medioschile/acercade.html')

def contacto(request):
	return render(request, 'medioschile/contacto.html')

def aporta(request):
	return render(request, 'medioschile/aporta.html')

def privacidad(request):
	return render(request, 'medioschile/privacidad.html')

class EscritoList(ListView):
	model = Escrito
	context_object_name = 'escrito_list'
	template_name = 'medioschile/escrito_list.html'

class EscritoDetail(DetailView):
	model = Escrito
	context_object_name = 'escrito_detail'
	template_name = 'medioschile/escrito_detail.html'

class CanalTVList(ListView):
	model = CanalTV
	context_object_name = 'canaltv_list'
	template_name = 'medioschile/canaltv_list.html'

class CanalTVDetail(DetailView):
	model = CanalTV
	context_object_name = 'canaltv_detail'
	template_name = 'medioschile/canaltv_detail.html'

class RadioList(ListView):
	model = Radio
	context_object_name = 'radio_list'
	template_name = 'medioschile/radio_list.html'

class RadioDetail(DetailView):
	model = Radio
	context_object_name = 'radio_detail'
	template_name = 'medioschile/radio_detail.html'

class MedioDigitalList(ListView):
	model = MedioDigital
	context_object_name = 'mediodigital_list'
	template_name = 'medioschile/mediodigital_list.html'

class MedioDigitalDetail(DetailView):
	model = MedioDigital
	context_object_name = 'mediodigital_detail'
	template_name = 'medioschile/mediodigital_detail.html'

class PropietarioDetail(DetailView):
	model = Propietario
	context_object_name = 'propietario_detail'
	template_name = 'medioschile/propietario_detail.html'

class PropietarioList(ListView):
	model = Propietario
	context_object_name = 'propietario_list'
	template_name = 'medioschile/propietario_list.html'

class GrupoDetail(DetailView):
	model = Grupo
	context_object_name = 'grupo_detail'
	template_name = 'medioschile/grupo_detail.html'

class GrupoList(ListView):
	model = Grupo
	context_object_name = 'grupo_list'
	template_name = 'medioschile/grupo_list.html'

class RegulacionDetail(DetailView):
	model = Regulacion
	context_object_name = 'regulacion_detail'
	template_name = 'medioschile/regulacion_detail.html'

class RegulacionList(ListView):
	model = Regulacion
	context_object_name = 'regulacion_list'
	template_name = 'medioschile/regulacion_list.html'

class AnalisisDetail(DetailView):
	model = Articulo
	context_object_name = 'analisis_detail'
	template_name = 'medioschile/analisis_detail.html'

class AnalisisList(ListView):
	model = Articulo
	context_object_name = 'analisis_list'
	template_name = 'medioschile/analisis_list.html'

class FuenteList(ListView):
	model = Fuente
	context_object_name = 'fuente_list'
	template_name = 'medioschile/fuente_list.html'

def analisiscl(request):
	analisiscl = Articulo.objects.filter(pais = 1)
	return render(request, 'medioschile/analisis_listcl.html', {"analisiscl":analisiscl})

def analisiscol(request):
	analisiscol = Articulo.objects.filter(pais = 6)
	return render(request, 'medioschile/analisis_listcol.html', {"analisiscol":analisiscol})

def etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'medioschile/analisis_list.html', {"etiquetas":etiquetas})

class PropietarioViewSet(viewsets.ReadOnlyModelViewSet):
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

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

class EmpresarioViewSet(viewsets.ModelViewSet):
    queryset = Empresario.objects.all()
    serializer_class = EmpresarioSerializer

class EjecutivoViewSet(viewsets.ModelViewSet):
    queryset = Ejecutivo.objects.all()
    serializer_class = EjecutivoSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

def get_nombre(request):
    if request.method == 'POST':
    	form = ContactoForm(request.POST)
    	if form.is_valid():
    		su_nombre = form.cleaned_data['su_nombre']
    		asunto = form.cleaned_data['asunto']
    		mensaje = form.cleaned_data['mensaje']
    		email = form.cleaned_data['email']
    		cc_myself = form.cleaned_data['cc_myself']
    		recipients = ['felipe.perry@gmail.com','miguel@poderopedia.com']
    		if cc_myself:
    			recipients.append(email)
    			send_mail(asunto, mensaje, email, recipients)
    			return HttpResponseRedirect('medioschile/gracias/')
    		else:
    			form = ContactoForm()
    			return render(request, 'medioschile/contacto.html', {'form': form})