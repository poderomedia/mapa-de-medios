import datetime
from haystack import indexes
from medioscolombia.models import *

class EscritoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    medio = indexes.CharField(model_attr='medio')
    def get_model(self):
        return Escrito
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class CanalTVIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    medio = indexes.CharField(model_attr='medio')
    def get_model(self):
        return CanalTV
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class RadioIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    medio = indexes.CharField(model_attr='medio')
    def get_model(self):
        return Radio
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class MedioDigitalIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    medio = indexes.CharField(model_attr='medio')
    def get_model(self):
        return MedioDigital
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class PropietarioIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    propietario = indexes.CharField(model_attr='propietario')
    def get_model(self):
        return Propietario
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class GrupoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    grupo = indexes.CharField(model_attr='grupo')
    def get_model(self):
        return Grupo
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()