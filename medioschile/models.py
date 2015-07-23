# -*- encoding: utf-8 -*-
from django.db import models
import select2.fields
import select2.models
import datetime
YEAR_CHOICES = []
for r in range(1800, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

class Ejecutivo(models.Model):
	class Meta:
			verbose_name = 'Ejecutivo de Medio'
			verbose_name_plural = 'Ejecutivos de Medios'
			managed = True
	ejecutivo = models.CharField("Ejecutivo", max_length=255, unique=True)
	def __unicode__(self):
		return self.ejecutivo

class Cargo(models.Model):
	class Meta:
			verbose_name = 'Cargo'
			verbose_name_plural = 'Cargos'
			managed = True
	cargo = models.CharField("Cargo", max_length=255, unique=True)
	def __unicode__(self):
		return self.cargo

class Empresario(models.Model):
	class Meta:
			verbose_name = 'Miembro Directorio'
			verbose_name_plural = 'Miembros de Directorios'
			managed = True
	empresario = models.CharField("Miembro de Directorio", max_length=255, unique=True)
	linkempresario = models.URLField("Link Poderopedia", null=True, blank=True, help_text="http://...")
	def __unicode__(self):
		return self.empresario

class GeneroEscrito(models.Model):
	class Meta:
			verbose_name = 'Género Medio Escrito'
			verbose_name_plural = 'Géneros Medios Escritos'
			managed = True
	genero = models.CharField("Género", max_length=255, unique=True)
	def __unicode__(self):
		return self.genero

class Region(models.Model):
	class Meta:
			verbose_name = 'Región'
			verbose_name_plural = 'Regiones'
			managed = True
	region = models.CharField("Región", max_length=255, unique=True)
	def __unicode__(self):
		return self.region

class Comuna(models.Model):
	class Meta:
			verbose_name = 'Comuna'
			verbose_name_plural = 'Comunas'
			managed = True
	comuna = models.CharField("Comuna", max_length=255, unique=True)
	def __unicode__(self):
		return self.comuna

class Ciudad(models.Model):
	class Meta:
			verbose_name = 'Ciudad'
			verbose_name_plural = 'Ciudades'
			managed = True
	ciudad = models.CharField("Ciudad", max_length=255, unique=True)
	def __unicode__(self):
		return self.ciudad

class Sector(models.Model):
	class Meta:
			verbose_name = 'Sector de Actividad Socio'
			verbose_name_plural = 'Sectores de Actividad Socios'
			managed = True
	sector = models.CharField("Sector de Actividad Socios", max_length=255, unique=True)
	def __unicode__(self):
		return self.sector

class Periodicidad(models.Model):
	class Meta:
			verbose_name = 'Periodicidad'
			verbose_name_plural = 'Periodicidades'
			managed = True
	periodicidad = models.CharField("Periodicidad", max_length=255, unique=True)
	def __unicode__(self):
		return self.periodicidad

class TipoSociedad(models.Model):
	class Meta:
			verbose_name = 'Tipo Entidad'
			verbose_name_plural = 'Tipos de Entidad'
			managed = True
	tiposociedad = models.CharField("Tipo Sociedad", max_length=255, unique=True)
	def __unicode__(self):
		return self.tiposociedad

class PaisSociedad(models.Model):
	class Meta:
			verbose_name = 'País'
			verbose_name_plural = 'Paises'
			managed = True
	paissociedad = models.CharField("Pais", max_length=255, unique=True)
	def __unicode__(self):
		return self.paissociedad

class Autor(models.Model):
	class Meta:
			verbose_name = 'Autor'
			verbose_name_plural = 'Autores'
			managed = True
	autor = models.CharField("Autor", max_length=255, unique=True)
	def __unicode__(self):
		return self.autor
	datosautor = models.CharField("Datos Autor", max_length=255, null=True, blank=True)

class Fuente(models.Model):
	class Meta:
			verbose_name = 'Fuente'
			verbose_name_plural = 'Fuentes'
			managed = True
	fuente = models.CharField("Fuente", max_length=255, unique=True)
	def __unicode__(self):
		return self.fuente
	descripcionfuente = models.TextField("Descripción", null=True, blank=True)
	autor = select2.fields.ManyToManyField(Autor, verbose_name="Autor/es", blank=True, help_text="Actualice con F5")
	linkfuente = models.URLField("Link", null=True, blank=True, help_text="http://...")

class Sociedad(models.Model):
	class Meta:
			verbose_name = 'Socio'
			verbose_name_plural = 'Socios'
			managed = True
	sociedad = models.CharField("Nombre Socio", max_length=255, unique=True)
	def __unicode__(self):
		return self.sociedad
	rutsociedad = models.CharField("R.U.T.", max_length=255, null=True, blank=True)
	tiposociedad = models.ForeignKey(TipoSociedad, verbose_name="Tipo de Sociedad", related_name="sociedad_tiposociedad", null=True, blank=True)
	paissocio = models.ForeignKey(PaisSociedad, related_name="pais_socio", verbose_name="País de origen", null=True, blank=True)
	controlador = models.ForeignKey('self', related_name="controlador_socio", verbose_name="Controlador", null=True, blank=True)
	presidentedirectorio = models.ForeignKey(Empresario, related_name="sociedad_presidentedirectorio", verbose_name="Presidente Directorio", null=True, blank=True)
	miembrosdirectorio = select2.fields.ManyToManyField(Empresario, related_name="sociedad_miembrosdirectorio", verbose_name="Miembros Directorio", blank=True, help_text="Actualice con F5")
	fuentes = models.ForeignKey(Fuente, related_name="fuente_info_sociedad", verbose_name="Fuente", null=True, blank=True, max_length=255)
	utilidades = models.CharField("Utilidades -último año-", max_length=255, null=True, blank=True)
	infoutilidades = models.CharField("Información Utilidades", max_length=255, null=True, blank=True)
	fuenteutilidades = models.ForeignKey(Fuente, related_name="fuente_utilidades_sociedad", verbose_name="Fuente", null=True, blank=True, max_length=255)
	sectores = select2.fields.ManyToManyField(Sector, verbose_name="Sectores de Actividad Socio", blank=True, help_text="Actualice con F5")
	sociedadcontroladora = models.ForeignKey('self', related_name="sociedad_controladora_sociedad", verbose_name="Socio Controlador", max_length=255, null=True, blank=True)
	pcentsociedadcontroladora = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedada = models.ForeignKey('self', related_name="sociedad_a_sociedad", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedada = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadb = models.ForeignKey('self', related_name="sociedad_b_sociedad", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadb = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadc = models.ForeignKey('self', related_name="sociedad_c_sociedad", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadc = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadd = models.ForeignKey('self', related_name="sociedad_d_sociedad", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadd = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedade = models.ForeignKey('self', related_name="sociedad_e_sociedad", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedade = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadf = models.ForeignKey('self', related_name="sociedad_f_sociedad", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadf = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadg = models.ForeignKey('self', related_name="sociedad_g_sociedad", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadg = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadh = models.ForeignKey('self', related_name="sociedad_h_sociedad", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadh = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadi = models.ForeignKey('self', related_name="sociedad_i_sociedad", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadi = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadj = models.ForeignKey('self', related_name="sociedad_j_sociedad", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadj = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadk = models.ForeignKey('self', related_name="sociedad_k_sociedad", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadk = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadl = models.ForeignKey('self', related_name="sociedad_l_sociedad", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadl = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadm = models.ForeignKey('self', related_name="sociedad_m_sociedad", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadm = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadn = models.ForeignKey('self', related_name="sociedad_n_sociedad", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadn = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	fechainfo = models.DateField("Fecha Información", null=True, blank=True)
	fuentesociedad = models.ForeignKey(Fuente, verbose_name="Fuente", null=True, blank=True, max_length=255)
	linksociedad = models.URLField("Link Poderopedia", null=True, blank=True, help_text="http://...")

class Propietario(models.Model):
	class Meta:
			verbose_name = 'Empresas Controladora'
			verbose_name_plural = 'Empresas Controladoras'
			managed = True
	propietario = models.CharField("Nombre Empresa/Sociedad", max_length=255, unique=True)
	def __unicode__(self):
		return self.propietario
	rutpropietario = models.CharField("R.U.T.", max_length=255, null=True, blank=True)
	tiposociedad = models.ForeignKey(TipoSociedad, verbose_name="Tipo de Sociedad", related_name="propietario_tiposociedad", null=True, blank=True)
	presidentedirectorio = models.ForeignKey(Empresario, related_name="propietario_presidentedirectorio", verbose_name="Presidente Directorio/Ejecutivo", null=True, blank=True)
	miembrosdirectorio = select2.fields.ManyToManyField(Empresario, related_name="propietario_miembrosdirectorio", verbose_name="Miembros Directorio/Consejo", blank=True, help_text="Actualice con F5")
	utilidades = models.CharField("Utilidades -último año-", max_length=255, null=True, blank=True)
	infoutilidades = models.CharField("Información Utilidades", max_length=255, null=True, blank=True)
	fuenteutilidades = models.ForeignKey(Fuente, related_name="fuente_utilidades_propietario", verbose_name="Fuente", null=True, blank=True, max_length=255)
	sectores = select2.fields.ManyToManyField(Sector, verbose_name="Sectores de Actividad Socio", blank=True, help_text="Actualice con F5")
	sociedadcontroladora = models.ForeignKey(Sociedad, related_name="sociedad_controladora_propietario", verbose_name="Socio Controlador", max_length=255, null=True, blank=True)
	pcentsociedadcontroladora = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedada = models.ForeignKey(Sociedad, related_name="sociedad_a_propietario", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedada = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadb = models.ForeignKey(Sociedad, related_name="sociedad_b_propietario", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadb = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadc = models.ForeignKey(Sociedad, related_name="sociedad_c_propietario", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadc = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadd = models.ForeignKey(Sociedad, related_name="sociedad_d_propietario", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadd = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedade = models.ForeignKey(Sociedad, related_name="sociedad_e_propietario", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedade = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadf = models.ForeignKey(Sociedad, related_name="sociedad_f_propietario", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadf = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadg = models.ForeignKey(Sociedad, related_name="sociedad_g_propietario", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadg = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadh = models.ForeignKey(Sociedad, related_name="sociedad_h_propietario", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadh = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadi = models.ForeignKey(Sociedad, related_name="sociedad_i_propietario", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadi = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadj = models.ForeignKey(Sociedad, related_name="sociedad_j_propietario", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadj = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadk = models.ForeignKey(Sociedad, related_name="sociedad_k_propietario", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadk = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadl = models.ForeignKey(Sociedad, related_name="sociedad_l_propietario", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadl = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadm = models.ForeignKey(Sociedad, related_name="sociedad_m_propietario", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadm = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	otrasociedadn = models.ForeignKey(Sociedad, related_name="sociedad_n_propietario", verbose_name="Socio Minoritario", max_length=255, null=True, blank=True)
	pcentsociedadn = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	fechainfo = models.DateField("Fecha Información", null=True, blank=True)
	fuentepropietario = models.ForeignKey(Fuente, verbose_name="Fuente", related_name="fuente2prop", null=True, blank=True, max_length=255)
	fuentesociedad = models.ForeignKey(Fuente, verbose_name="Fuente", null=True, blank=True, max_length=255)
	propietariopropietario = models.ForeignKey('self', related_name="propietario_propietario", verbose_name="Empresa/Sociedad Controladora", null=True, blank=True)
	pcentpropietario = models.CharField("Porcentaje", max_length=255, null=True, blank=True)
	observacionespropiedad = models.CharField("Observaciones Propiedad", null=True, blank=True, max_length=255)
	linkpropietario = models.URLField("Link Poderopedia", null=True, blank=True, help_text="http://...")
	grupo = models.ForeignKey('Grupo', null=True, blank=True)
	escritospropietario = select2.fields.ManyToManyField('Escrito', verbose_name="Medios Papel del propietario", blank=True, related_name="propietario_escritos")
	radiospropietario = select2.fields.ManyToManyField('Radio', verbose_name="Radios del propietario", blank=True, related_name="propietario_radios")
	canaltvspropietario = select2.fields.ManyToManyField('CanalTV', verbose_name="Canales TV del propietario", blank=True, related_name="propietario_canaltvs")
	digitalespropietario = select2.fields.ManyToManyField('MedioDigital', verbose_name="Medios Digitales del propietario", blank=True, related_name="propietario_digitales")
	ejecutivouno = models.ForeignKey(Ejecutivo, related_name="ejecutivouno_propietario", null=True, verbose_name="Ejecutivo", blank=True)
	ejecutivounocargo = models.ForeignKey(Cargo, related_name="ejecutivounocargo_propietario", null=True, verbose_name="Cargo", blank=True)
	ejecutivounocargofecha = models.DateField("Fecha del dato", null=True, blank=True)
	ejecutivodos = models.ForeignKey(Ejecutivo, related_name="ejecutivodos_propietario", null=True, verbose_name="Ejecutivo", blank=True)
	ejecutivodoscargo = models.ForeignKey(Cargo, related_name="ejecutivodoscargo_propietario", null=True, verbose_name="Cargo", blank=True)
	ejecutivodoscargofecha = models.DateField("Fecha del dato", null=True, blank=True)
	ejecutivotres = models.ForeignKey(Ejecutivo, related_name="ejecutivotres_propietario", null=True, verbose_name="Ejecutivo", blank=True)
	ejecutivotrescargo = models.ForeignKey(Cargo, related_name="ejecutivotrescargo_propietario", null=True, verbose_name="Cargo", blank=True)
	ejecutivotrescargofecha = models.DateField("Fecha del dato", null=True, blank=True)

class Grupo(models.Model):
	class Meta:
			verbose_name = 'Grupo de Medios'
			verbose_name_plural = 'Grupos de Medios'
			managed = True
	grupo = models.CharField("Grupo de Medios", max_length=255, unique=True)
	def __unicode__(self):
		return self.grupo
	controladorgrupo = models.ForeignKey(Sociedad, verbose_name="Controlador Grupo", max_length=255, null=True, blank=True)
	otrosnegociosgrupo = select2.fields.ManyToManyField(Sector, verbose_name="Otros Negocios Controlador", blank=True, help_text="Negocios fuera de la industria de medios")
	paisorigen = models.ForeignKey(PaisSociedad, related_name="pais_grupo", verbose_name="País de Origen", null=True, blank=True)
	linkgrupo = models.URLField("Link Controlador en Poderopedia", null=True, blank=True, help_text="http://...")
	escritosgrupo = select2.fields.ManyToManyField('Escrito', verbose_name="Medios Papel del grupo", blank=True, related_name="grupo_escritos")
	radiosgrupo = select2.fields.ManyToManyField('Radio', verbose_name="Radios del grupo", blank=True, related_name="grupo_radios")
	canaltvsgrupo = select2.fields.ManyToManyField('CanalTV', verbose_name="Canales TV del grupo", blank=True, related_name="grupo_canaltvs")
	digitalesgrupo = select2.fields.ManyToManyField('MedioDigital', verbose_name="Medios Digitales del grupo", blank=True, related_name="grupo_digitales")

class Escrito(models.Model):
	class Meta:
			verbose_name = 'Medio Escrito'
			verbose_name_plural = 'Medios Escritos'
			managed = True
	TIPO_MEDIO = (
		('Diario', 'Diario'),
		('Revista', 'Revista'),
		)
	tipo = models.CharField("Tipo", max_length=100, null=True, blank=True, choices=TIPO_MEDIO)
	medio = models.CharField("Nombre", max_length=255, unique=True)
	def __unicode__(self):
		return self.medio
	asociadoaescrito = models.ForeignKey('self', related_name="escrito_asociadoaescrito", verbose_name="Asociado a Medio Escrito", null=True, blank=True)
	asociadoaradio = models.ForeignKey('Radio', related_name="escrito_asociadoaradio", verbose_name="Asociado a Radio", null=True, blank=True)
	asociadoacanaltv = models.ForeignKey('CanalTV', related_name="escrito_asociadoacanaltv", verbose_name="Asociado a Canal de TV", null=True, blank=True)
	asociadoamediodigital = models.ForeignKey('MedioDigital', related_name="escrito_asociadoamediodigital", verbose_name="Asociado a Medio Digital", null=True, blank=True)
	genero = models.ForeignKey(GeneroEscrito, null=True, blank=True, verbose_name="Género")
	PAGADO_GRATUITO = (
		('Pagado/a', 'Pagado/a'),
		('Gratuito/a', 'Gratuito/a'),
		)
	pagado_gratuito = models.CharField("Pagado o Gratuito", max_length=100, null=True, blank=True, choices=PAGADO_GRATUITO)
	inicio = models.DateField("Fecha Fundación", null=True, blank=True)
	inicioyear = models.IntegerField(('Año Fundación'), choices=YEAR_CHOICES, default=datetime.datetime.now().year, null=True, blank=True)
	CIRCULACION = (
		('Nacional', 'Nacional'),
		('Regional', 'Regional'),
		('Comunal', 'Comunal'),
		)
	circulacion = models.CharField("Circulación", max_length=100, null=True, blank=True, choices=CIRCULACION)
	region = select2.fields.ManyToManyField(Region, verbose_name="Región", blank=True)
	comuna = select2.fields.ManyToManyField(Comuna, verbose_name="Comuna", blank=True, help_text="Actualice con F5 - Si el medio tiene cobertura regional, no es necesario ingresar las comunas.")
	ciudad = select2.fields.ManyToManyField(Ciudad, verbose_name="Ciudad", blank=True, help_text="Actualice con F5 - Si ingresa la(s) comuna(s) correspondientes, no es necesario señalar la(s) ciudad(es).")
	periodicidad = models.ForeignKey(Periodicidad, verbose_name="Periodicidad", null=True, blank=True)
	lectoria = models.CharField("Índice de Lectoría", max_length=100, null=True, blank=True)
	infolectoria = models.CharField("Información Lectoría", max_length=255, blank=True)
	fuentelectoria = models.ForeignKey(Fuente, related_name="fuente_lectoria_escrito", verbose_name="Fuente Lectoría", null=True, blank=True, max_length=255)
	tiraje = models.CharField("Tiraje", max_length=100, null=True, blank=True)
	infotiraje = models.CharField("Información Tiraje", max_length=255, null=True, blank=True)
	fuentetiraje = models.ForeignKey(Fuente, related_name="fuente_tiraje_escrito", verbose_name="Fuente Tiraje", null=True, blank=True, max_length=255)
	direccion = models.CharField("Dirección", max_length=255, blank=True, help_text="Calle-Nº-Comuna-Ciudad")
	sitioweb = models.URLField("Sitio WEB", max_length=255, null=True, blank=True, help_text="http://...")
	propietario = select2.fields.ManyToManyField(Propietario, related_name="propietario_escrito", verbose_name="Empresa Controladora", max_length=255, blank=True, help_text="Actualice con F5")
	fuentepropiedad = models.ForeignKey(Fuente, related_name="fuente_propiedad_escrito", verbose_name="Fuente Propiedad", null=True, blank=True, max_length=255)
	grupo = models.ForeignKey(Grupo, related_name="grupo_escrito", null=True, verbose_name="Grupo de Medios", blank=True, max_length=255)
	telefono = models.CharField("Teléfono", max_length=100, null=True, blank=True)
	observaciones = models.TextField("Observaciones", null=True, blank=True)
	anexos = models.TextField("Anexos", null=True, blank=True)
	check = models.BooleanField("Terminado", default=None)
	ejecutivouno = models.ForeignKey(Ejecutivo, related_name="ejecutivouno_escrito", null=True, verbose_name="Ejecutivo", blank=True)
	ejecutivounocargo = models.ForeignKey(Cargo, related_name="ejecutivounocargo_escrito", null=True, verbose_name="Cargo", blank=True)
	ejecutivounocargofecha = models.DateField("Fecha del dato", null=True, blank=True)
	ejecutivodos = models.ForeignKey(Ejecutivo, related_name="ejecutivodos_escrito", null=True, verbose_name="Ejecutivo", blank=True)
	ejecutivodoscargo = models.ForeignKey(Cargo, related_name="ejecutivodoscargo_escrito", null=True, verbose_name="Cargo", blank=True)
	ejecutivodoscargofecha = models.DateField("Fecha del dato", null=True, blank=True)
	ejecutivotres = models.ForeignKey(Ejecutivo, related_name="ejecutivotres_escrito", null=True, verbose_name="Ejecutivo", blank=True)
	ejecutivotrescargo = models.ForeignKey(Cargo, related_name="ejecutivotrescargo_escrito", null=True, verbose_name="Cargo", blank=True)
	ejecutivotrescargofecha = models.DateField("Fecha del dato", null=True, blank=True)
	logo = models.ImageField(upload_to='medios', null=True, blank=True)
	app = models.CharField("País", default="Chile", max_length=10, editable=False)

class GeneroRadio(models.Model):
	class Meta:
			verbose_name = 'Género Radio'
			verbose_name_plural = 'Géneros Radios'
			managed = True
	genero = models.CharField("Género", max_length=255, unique=True)
	def __unicode__(self):
		return self.genero

class Radio(models.Model):
	class Meta:
			verbose_name = 'Radio'
			verbose_name_plural = 'Radios'
			managed = True
	medio = models.CharField("Nombre", max_length=255, unique=True)
	def __unicode__(self):
		return self.medio
	asociadoaescrito = models.ForeignKey('Escrito', related_name="radio_asociadoaescrito", verbose_name="Asociado a Medio Escrito", null=True, blank=True)
	asociadoaradio = models.ForeignKey('self', related_name="radio_asociadoaradio", verbose_name="Asociado a Radio", null=True, blank=True)
	asociadoacanaltv = models.ForeignKey('CanalTV', related_name="radio_asociadoacanaltv", verbose_name="Asociado a Canal de TV", null=True, blank=True)
	asociadoamediodigital = models.ForeignKey('MedioDigital', related_name="radio_asociadoamediodigital", verbose_name="Asociado a Medio Digital", null=True, blank=True)
	genero = models.ForeignKey(GeneroRadio, related_name="radio_genero", null=True, blank=True, verbose_name="Género")
	FRECUENCIA = (
		('AM', 'AM'),
		('FM', 'FM'),
		('AM y FM', 'AM y FM'),
		)
	frecuencia = models.CharField("Frecuencia", max_length=100, null=True, blank=True, choices=FRECUENCIA)
	inicio = models.DateField("Fecha Fundación", null=True, blank=True)
	inicioyear = models.IntegerField(('Año'), choices=YEAR_CHOICES, default=datetime.datetime.now().year, null=True, blank=True)
	indiceaudiencia = models.CharField("Índice de Audiencia", max_length=100, null=True, blank=True)
	infoaudiencia = models.CharField("Información de Índice Audiencia", max_length=255, blank=True)
	fuenteaudiencia = models.ForeignKey(Fuente, related_name="fuente_audiencia_radio", verbose_name="Fuente Audiencia", null=True, blank=True, max_length=255)
	COBERTURA = (
		('Nacional', 'Nacional'),
		('Regional', 'Regional'),
		('Comunal', 'Comunal'),
		)
	cobertura = models.CharField("Cobertura", max_length=100, null=True, blank=True, choices=COBERTURA)
	region = select2.fields.ManyToManyField(Region, verbose_name="Región", related_name="radio_region", blank=True)
	comuna = select2.fields.ManyToManyField(Comuna, verbose_name="Comuna", blank=True, help_text="Actualice con F5 - Si el medio tiene cobertura regional, no es necesario ingresar las comunas.")
	ciudad = select2.fields.ManyToManyField(Ciudad, verbose_name="Ciudad", related_name="radio_ciudad", blank=True, help_text="Actualice con F5 - Si ingresa la(s) comuna(s) correspondientes, no es necesario señalar la(s) ciudad(es).")
	direccion = models.CharField("Dirección", max_length=255, blank=True, help_text="Calle-Nº-Comuna-Ciudad")
	sitioweb = models.URLField("Sitio WEB", max_length=255, null=True, blank=True, help_text="http://...")
	propietario = select2.fields.ManyToManyField(Propietario, related_name="propietario_radio", verbose_name="Empresa Controladora", max_length=255, blank=True, help_text="Actualice con F5")
	fuentepropiedad = models.ForeignKey(Fuente, related_name="fuente_propiedad_radio", verbose_name="Fuente Propiedad", null=True, blank=True, max_length=255)
	grupo = models.ForeignKey(Grupo, related_name="grupo_radio", null=True, verbose_name="Grupo de Medios", blank=True, max_length=255)
	telefono = models.CharField("Teléfono", max_length=100, null=True, blank=True)
	observaciones = models.TextField("Observaciones", null=True, blank=True)
	anexos = models.TextField("Anexos", null=True, blank=True)
	check = models.BooleanField("Terminado", default=None)
	ejecutivouno = models.ForeignKey(Ejecutivo, related_name="ejecutivouno_radio", null=True, verbose_name="Ejecutivo", blank=True)
	ejecutivounocargo = models.ForeignKey(Cargo, related_name="ejecutivounocargo_radio", null=True, verbose_name="Cargo", blank=True)
	ejecutivounocargofecha = models.DateField("Fecha del dato", null=True, blank=True)
	ejecutivodos = models.ForeignKey(Ejecutivo, related_name="ejecutivodos_radio", null=True, verbose_name="Ejecutivo", blank=True)
	ejecutivodoscargo = models.ForeignKey(Cargo, related_name="ejecutivodoscargo_radio", null=True, verbose_name="Cargo", blank=True)
	ejecutivodoscargofecha = models.DateField("Fecha del dato", null=True, blank=True)
	ejecutivotres = models.ForeignKey(Ejecutivo, related_name="ejecutivotres_radio", null=True, verbose_name="Ejecutivo", blank=True)
	ejecutivotrescargo = models.ForeignKey(Cargo, related_name="ejecutivotrescargo_radio", null=True, verbose_name="Cargo", blank=True)
	ejecutivotrescargofecha = models.DateField("Fecha del dato", null=True, blank=True)
	logo = models.ImageField(upload_to='medios', null=True, blank=True)
	app = models.CharField("País", default="Chile", max_length=10, editable=False)

class GeneroCanalTV(models.Model):
	class Meta:
			verbose_name = 'Género Canal TV'
			verbose_name_plural = 'Géneros Canales TV'
			managed = True
	genero = models.CharField("Género", max_length=255, unique=True)
	def __unicode__(self):
		return self.genero

class CanalTV(models.Model):
	class Meta:
			verbose_name = 'Canal de TV'
			verbose_name_plural = 'Canales de TV'
			managed = True
	TIPO = (
		('Abierta', 'Abierta'),
		('Cable', 'Cable'),
		('Abierta y Cable', 'Abierta y Cable'),
		)
	tipo = models.CharField("Tipo", max_length=100, null=True, blank=True, choices=TIPO)
	medio = models.CharField("Nombre", max_length=255, unique=True)
	def __unicode__(self):
		return self.medio
	asociadoaescrito = models.ForeignKey('Escrito', related_name="canaltv_asociadoaescrito", verbose_name="Asociado a Medio Escrito", null=True, blank=True)
	asociadoaradio = models.ForeignKey('Radio', related_name="canaltv_asociadoaradio", verbose_name="Asociado a Radio", null=True, blank=True)
	asociadoacanaltv = models.ForeignKey('self', related_name="canaltv_asociadoacanaltv", verbose_name="Asociado a Canal de TV", null=True, blank=True)
	asociadoamediodigital = models.ForeignKey('MedioDigital', related_name="canaltv_asociadoamediodigital", verbose_name="Asociado a Medio Digital", null=True, blank=True)
	genero = models.ForeignKey(GeneroCanalTV, related_name="canaltv_genero", null=True, blank=True, verbose_name="Género")
	inicio = models.DateField("Fecha Fundación", null=True, blank=True)
	inicioyear = models.IntegerField(('Año'), choices=YEAR_CHOICES, default=datetime.datetime.now().year, null=True, blank=True)
	COBERTURA = (
		('Nacional', 'Nacional'),
		('Regional', 'Regional'),
		('Comunal', 'Comunal'),
		)
	cobertura = models.CharField("Cobertura", max_length=100, null=True, blank=True, choices=COBERTURA)
	rating = models.CharField("Rating", max_length=100, null=True, blank=True)
	inforating = models.CharField("Información de Rating", max_length=255, blank=True)
	fuenterating = models.ForeignKey(Fuente, related_name="fuente_rating_canaltv", verbose_name="Fuente Rating", null=True, blank=True, max_length=255)
	region = select2.fields.ManyToManyField(Region, verbose_name="Región", related_name="canaltv_region", blank=True)
	comuna = select2.fields.ManyToManyField(Comuna, verbose_name="Comuna", blank=True, help_text="Actualice con F5 - Si el medio tiene cobertura regional, no es necesario ingresar las comunas.")
	ciudad = select2.fields.ManyToManyField(Ciudad, verbose_name="Ciudad", related_name="canaltv_ciudad", blank=True, help_text="Actualice con F5 - Si ingresa la(s) comuna(s) correspondientes, no es necesario señalar la(s) ciudad(es).")
	direccion = models.CharField("Dirección", max_length=255, blank=True, help_text="Calle-Nº-Comuna-Ciudad")
	sitioweb = models.URLField("Sitio WEB", max_length=255, null=True, blank=True, help_text="http://...")
	propietario = select2.fields.ManyToManyField(Propietario, related_name="propietario_canaltv", verbose_name="Empresa Controladora", max_length=255, blank=True, help_text="Actualice con F5")
	fuentepropiedad = models.ForeignKey(Fuente, related_name="fuente_propiedad_canaltv", verbose_name="Fuente Propiedad", null=True, blank=True, max_length=255)
	grupo = models.ForeignKey(Grupo, related_name="grupo_canaltv", null=True, verbose_name="Grupo de Medios", blank=True, max_length=255)
	telefono = models.CharField("Teléfono", max_length=100, null=True, blank=True)
	observaciones = models.TextField("Observaciones", null=True, blank=True)
	anexos = models.TextField("Anexos", null=True, blank=True)
	check = models.BooleanField("Terminado", default=None)
	ejecutivouno = models.ForeignKey(Ejecutivo, related_name="ejecutivouno_canaltv", null=True, verbose_name="Ejecutivo", blank=True)
	ejecutivounocargo = models.ForeignKey(Cargo, related_name="ejecutivounocargo_canaltv", null=True, verbose_name="Cargo", blank=True)
	ejecutivounocargofecha = models.DateField("Fecha del dato", null=True, blank=True)
	ejecutivodos = models.ForeignKey(Ejecutivo, related_name="ejecutivodos_canaltv", null=True, verbose_name="Ejecutivo", blank=True)
	ejecutivodoscargo = models.ForeignKey(Cargo, related_name="ejecutivodoscargo_canaltv", null=True, verbose_name="Cargo", blank=True)
	ejecutivodoscargofecha = models.DateField("Fecha del dato", null=True, blank=True)
	ejecutivotres = models.ForeignKey(Ejecutivo, related_name="ejecutivotres_canaltv", null=True, verbose_name="Ejecutivo", blank=True)
	ejecutivotrescargo = models.ForeignKey(Cargo, related_name="ejecutivotrescargo_canaltv", null=True, verbose_name="Cargo", blank=True)
	ejecutivotrescargofecha = models.DateField("Fecha del dato", null=True, blank=True)
	logo = models.ImageField(upload_to='medios', null=True, blank=True)
	app = models.CharField("País", default="Chile", max_length=10, editable=False)

class GeneroMedioDigital(models.Model):
	class Meta:
			verbose_name = 'Género Medio Digital'
			verbose_name_plural = 'Géneros Medios Digitales'
			managed = True
	genero = models.CharField("Género", max_length=255, unique=True)
	def __unicode__(self):
		return self.genero

class MedioDigital(models.Model):
	class Meta:
			verbose_name = 'Medio Digital'
			verbose_name_plural = 'Medios Digitales'
			managed = True
	medio = models.CharField("Nombre", max_length=255, unique=True)
	def __unicode__(self):
		return self.medio
	sitioweb = models.URLField("Sitio WEB", max_length=255, null=True, blank=True, help_text="http://...")
	genero = models.ForeignKey(GeneroMedioDigital, related_name="mediodigital_genero", null=True, blank=True, verbose_name="Género")
	COBERTURA = (
		('Nacional', 'Nacional'),
		('Regional', 'Regional'),
		('Comunal', 'Comunal'),
		)
	cobertura = models.CharField("Cobertura", max_length=100, null=True, blank=True, choices=COBERTURA)
	CARACTERISTICA = (
		('Nativo', 'Nativo'),
		('Asociado a medio', 'Asociado a medio'),
		)
	nativoasociado = models.CharField("Nativo o Asociado", max_length=100, null=True, blank=True, choices=CARACTERISTICA)
	PAGADO_GRATUITO = (
		('Pagado', 'Pagado'),
		('Gratuito', 'Gratuito'),
		('Gratuito con Contenido Pagado', 'Gratuito con Contenido Pagado')
		)
	pagado_gratuito = models.CharField("Pagado o Gratuito", max_length=100, null=True, blank=True, choices=PAGADO_GRATUITO)
	asociadoaescrito = models.ForeignKey('Escrito', related_name="mediodigital_asociadoaescrito", verbose_name="Asociado a Medio Escrito", null=True, blank=True)
	asociadoaradio = models.ForeignKey('Radio', related_name="mediodigital_asociadoaradio", verbose_name="Asociado a Radio", null=True, blank=True)
	asociadoacanaltv = models.ForeignKey('CanalTV', related_name="mediodigital_asociadoacanaltv", verbose_name="Asociado a Canal de TV", null=True, blank=True)
	asociadoamediodigital = models.ForeignKey('self', related_name="mediodigital_asociadoamediodigital", verbose_name="Asociado a Medio Digital", null=True, blank=True)
	inicio = models.DateField("Fecha Fundación", null=True, blank=True)
	inicioyear = models.IntegerField(('Año'), choices=YEAR_CHOICES, default=datetime.datetime.now().year, null=True, blank=True)
	visitaspaginasvistas = models.IntegerField("Visitas Mes-Páginas Vistas", null=True, blank=True)
	visitasunicas = models.IntegerField("Visitas Mes-Visitas Únicas", null=True, blank=True)
	infovisitas = models.CharField("Información de Visitas", max_length=255, blank=True)
	fuentevisitas = models.ForeignKey(Fuente, related_name="fuente_visitas_mediodigital", verbose_name="Fuente", null=True, blank=True, max_length=255)
	region = select2.fields.ManyToManyField(Region, verbose_name="Región", related_name="mediodigital_region", blank=True)
	comuna = select2.fields.ManyToManyField(Comuna, verbose_name="Comuna", blank=True, help_text="Actualice con F5 - Si el medio tiene cobertura regional, no es necesario ingresar las comunas.")
	ciudad = select2.fields.ManyToManyField(Ciudad, verbose_name="Ciudad", related_name="mediodigital_ciudad", blank=True, help_text="Actualice con F5 - Si ingresa la(s) comuna(s) correspondientes, no es necesario señalar la(s) ciudad(es).")
	direccion = models.CharField("Dirección", max_length=255, blank=True, help_text="Calle-Nº-Comuna-Ciudad")
	propietario = select2.fields.ManyToManyField(Propietario, related_name="propietario_mediodigital", verbose_name="Empresa Controladora", max_length=255, blank=True, help_text="Actualice con F5")
	fuentepropiedad = models.ForeignKey(Fuente, related_name="fuente_propiedad_mediodigital", verbose_name="Fuente Propiedad", null=True, blank=True, max_length=255)
	grupo = models.ForeignKey(Grupo, related_name="grupo_mediodigital", null=True, verbose_name="Grupo de Medios", blank=True, max_length=255)
	telefono = models.CharField("Teléfono", max_length=100, null=True, blank=True)
	observaciones = models.TextField("Observaciones", null=True, blank=True)
	anexos = models.TextField("Anexos", null=True, blank=True)
	check = models.BooleanField("Terminado", default=None)
	ejecutivouno = models.ForeignKey(Ejecutivo, related_name="ejecutivouno_mediodigital", null=True, verbose_name="Ejecutivo", blank=True)
	ejecutivounocargo = models.ForeignKey(Cargo, related_name="ejecutivounocargo_mediodigital", null=True, verbose_name="Cargo", blank=True)
	ejecutivounocargofecha = models.DateField("Fecha del dato", null=True, blank=True)
	ejecutivodos = models.ForeignKey(Ejecutivo, related_name="ejecutivodos_mediodigital", null=True, verbose_name="Ejecutivo", blank=True)
	ejecutivodoscargo = models.ForeignKey(Cargo, related_name="ejecutivodoscargo_mediodigital", null=True, verbose_name="Cargo", blank=True)
	ejecutivodoscargofecha = models.DateField("Fecha del dato", null=True, blank=True)
	ejecutivotres = models.ForeignKey(Ejecutivo, related_name="ejecutivotres_mediodigital", null=True, verbose_name="Ejecutivo", blank=True)
	ejecutivotrescargo = models.ForeignKey(Cargo, related_name="ejecutivotrescargo_mediodigital", null=True, verbose_name="Cargo", blank=True)
	ejecutivotrescargofecha = models.DateField("Fecha del dato", null=True, blank=True)
	logo = models.ImageField(upload_to='medios', null=True, blank=True)
	app = models.CharField("País", default="Chile", max_length=10, editable=False)

class CargoEjecutivo(models.Model):
	class Meta:
			verbose_name = 'Cargo Ejectutivo'
			verbose_name_plural = 'Cargos Ejecutivos'
			managed = True
	ejecutivocargo = models.ForeignKey(Ejecutivo, verbose_name="Ejecutivo", related_name="ejecutivo_cargo", null=True, blank=True)
	fechacargo = models.DateField("Fecha", null=True, blank=True)
	cargo = models.ForeignKey(Cargo, verbose_name="Cargo", related_name="cargo_ejecutivo", null=True, blank=True)
	escrito = models.ForeignKey(Escrito, null=True, blank=True)
	canaltv = models.ForeignKey(CanalTV, null=True, blank=True)
	radio = models.ForeignKey(Radio, null=True, blank=True)
	mediodigital = models.ForeignKey(MedioDigital, null=True, blank=True)

class TipoDocumento(models.Model):
	class Meta:
			verbose_name = 'Tipo de Regulación'
			verbose_name_plural = 'Tipos de Regulación'
			managed = True
	tipodocumento = models.CharField("Tipo", max_length=255, unique=True)
	def __unicode__(self):
		return self.tipodocumento

class Regulacion(models.Model):
	class Meta:
			verbose_name = 'Regulación'
			verbose_name_plural = 'Regulaciones'
			managed = True
	documento = models.CharField("Documento", max_length=255, unique=True)
	tipodocumento = models.ForeignKey(TipoDocumento, verbose_name="Tipo de Regulación", null=True, blank=True)
	historia = models.TextField("Historia", max_length=10000, null=True, blank=True, help_text="Fechas importantes en relación al documento")
	descripciondocumento = models.TextField("Descripción", null=True, blank=True, help_text="Detalle del texto en relación a la industria de medios")
	actores = models.TextField("Autores/Entidades Involucradas", max_length=10000, null=True, blank=True, help_text="Nombre de la entidad involucrada(autoridad,gremio,ong,etc.)-Explicación de la situación(lobby,rrpp,vocería,etc.")
	linkdocumento = models.URLField("Link", null=True, blank=True, help_text="http://...")

class Etiqueta(models.Model):
	class Meta:
			verbose_name = 'Etiqueta'
			verbose_name_plural = 'Etiquetas'
			managed = True
	etiqueta = models.CharField("Etiqueta", max_length=255, unique=True)
	def __unicode__(self):
		return self.etiqueta

class Articulo(models.Model):
	class Meta:
			verbose_name = 'Artículo'
			verbose_name_plural = 'Artículos'
			managed = True
			ordering = ['-fecha']
	titulo = models.CharField("Título", max_length=255, unique=True)
	def __unicode__(self):
		return self.titulo
	subtitulo = models.TextField("Subtítulo", null=True, blank=True)
	cuerpo = models.TextField("Cuerpo", null=True, blank=True)
	imagen = models.ImageField(upload_to='medios', null=True, blank=True)
	imagen2 = models.ImageField(upload_to='medios', null=True, blank=True)
	imagen3 = models.ImageField(upload_to='medios', null=True, blank=True)
	imagen_destacada = models.ImageField(upload_to='medios', null=True, blank=True)
	fecha = models.DateField("Fecha", null=True, blank=True)
	autor = models.ForeignKey(Autor, null=True, blank=True)
	extracto = models.TextField("Extracto", null=True, blank=True)
	pais = models.ForeignKey(PaisSociedad, null=True, blank=True)
	destacado = models.BooleanField("Destacado Portada", default=None, help_text="Si marca el artículo como destacado, aparecerá en portada, por lo que debe eligir también la posición (1,2,3,4)")
	POSICION = (
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
		)
	posicion = models.CharField("Posición", max_length=2, default=None, null=True, choices=POSICION, help_text="Elija el lugar que ocupará el artículo en el carrusel de portada")
	etiqueta = models.ForeignKey(Etiqueta, default=None, null=True)