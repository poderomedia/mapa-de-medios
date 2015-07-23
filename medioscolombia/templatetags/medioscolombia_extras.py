from django import template
from medioscolombia.models import Propietario,Grupo,Escrito,Radio,CanalTV,MedioDigital,Fuente,Regulacion

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
def contarescritoscol():
    contarescritoscol = Escrito.objects.count()
    return contarescritoscol

@register.simple_tag
def contarcanalestvcol():
    contarcanalestvcol = CanalTV.objects.count()
    return contarcanalestvcol

@register.simple_tag
def contarradioscol():
    contarradioscol = Radio.objects.count()
    return contarradioscol

@register.simple_tag
def contardigitalescol():
    contardigitalescol = MedioDigital.objects.count()
    return contardigitalescol

@register.simple_tag
def contargruposcol():
    contargruposcol = Grupo.objects.count()
    return contargruposcol

@register.simple_tag
def contarleyescol():
    contarleyescol = Regulacion.objects.count()
    return contarleyescol

@register.simple_tag
def contarpropietarioscol():
    contarpropietarioscol = Propietario.objects.count()
    return contarpropietarioscol

@register.simple_tag
def contarfuentescol():
    contarfuentescol = Fuente.objects.count()
    return contarfuentescol