from medioschile.models import Ejecutivo,Empresario,GeneroEscrito,Region,Comuna,Ciudad,Sector,Periodicidad,Propietario,TipoSociedad,PaisSociedad,Sociedad,Grupo,Escrito,GeneroRadio,Radio,GeneroCanalTV,CanalTV,GeneroMedioDigital,MedioDigital,Autor,Fuente,TipoDocumento,Regulacion,CargoEjecutivo,Cargo,Etiqueta,Articulo
from rest_framework import serializers


class PropietarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Propietario
        fields = ('propietario', 'rutpropietario', 'tiposociedad', 'sociedadcontroladora', 'propietariopropietario')

class TipoSociedadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoSociedad
        fields = ('tiposociedad',)

class SociedadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sociedad
        fields = ('sociedad', 'rutsociedad', 'controlador', 'sociedadcontroladora', 'linksociedad')

class GrupoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grupo
        fields = ('grupo', 'controladorgrupo', 'paisorigen', 'linkgrupo')

class PaisSociedadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaisSociedad
        fields = ('paissociedad',)

class RadioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Radio
        fields = ('medio', 'frecuencia', 'genero', 'propietario', 'grupo',  'sitioweb')

class EscritoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Escrito
        fields = ('medio', 'tipo', 'genero', 'propietario', 'grupo',  'sitioweb')

class CanalTVSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CanalTV
        fields = ('medio', 'tipo', 'genero', 'propietario', 'grupo',  'sitioweb')

class MedioDigitalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MedioDigital
        fields = ('medio', 'genero', 'propietario', 'grupo',  'sitioweb')

class GeneroRadioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeneroRadio
        fields = ('genero',)

class GeneroCanalTVSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeneroCanalTV
        fields = ('genero',)

class GeneroEscritoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeneroEscrito
        fields = ('genero',)

class GeneroMedioDigitalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeneroMedioDigital
        fields = ('genero',)

class FuenteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fuente
        fields = ('fuente', 'descripcionfuente', 'autor', 'linkfuente')

class ArticuloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Articulo
        fields = ('titulo', 'subtitulo', 'cuerpo', 'fecha', 'autor', 'extracto', 'pais')

class EmpresarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empresario
        fields = ('empresario', 'linkempresario')

class EjecutivoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ejecutivo
        fields = ('ejecutivo',)

class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = ('autor',)