from django import template
from medioschile.models import Propietario,Grupo,Escrito,Radio,CanalTV,MedioDigital,Fuente,Regulacion

register = template.Library()

@register.filter
def classname(obj):
    classname = obj.__class__.__name__
    return classname

@register.filter
def appname(obj):
    appname = obj._meta.app_label
    return appname

@register.simple_tag
def contarescritos():
    contarescritos = Escrito.objects.count()
    return contarescritos

@register.simple_tag
def contarcanalestv():
    contarcanalestv = CanalTV.objects.count()
    return contarcanalestv

@register.simple_tag
def contarradios():
    contarradios = Radio.objects.count()
    return contarradios

@register.simple_tag
def contardigitales():
    contardigitales = MedioDigital.objects.count()
    return contardigitales

@register.simple_tag
def contargrupos():
    contargrupos = Grupo.objects.count()
    return contargrupos

@register.simple_tag
def contarleyes():
    contarleyes = Regulacion.objects.count()
    return contarleyes

@register.simple_tag
def contarpropietarios():
    contarpropietarios = Propietario.objects.count()
    return contarpropietarios

@register.simple_tag
def contarfuentes():
    contarfuentes = Fuente.objects.count()
    return contarfuentes

