from django.db import models
from datetime import datetime
from BoletinAvances.apps.listas.models import Listas


TIPO_ENVIO = (
    ('Automatico', 'Automatico'),
    ('Programado', 'Programado'),
)


TAG = (
    ('0', '----'),
    ('REG', 'Regionales'),
    ('NAC', 'Nacionales'),
    ('INT', 'Internacionales'),
    ('ECO', 'Economia'),
    ('DEP', 'Deporte'),
    ('SUC', 'Sucesos'),
)


class Avances(models.Model):
   '''Clase para los avances'''
   fecha = models.DateField(default=datetime.now, blank=True)
   hora = models.TimeField(auto_now_add=True, blank=True)
   tipo_envio = models.CharField(max_length=20, choices=TIPO_ENVIO, default='0', verbose_name='Tipo de envio')
   status = models.CharField(max_length=110, verbose_name='Status', blank=True, null=True)
   listas = models.ManyToManyField(Listas)
   titulo_mensaje = models.CharField(max_length=1000, verbose_name='Titulo')
   cuerpo_mensaje = models.TextField(verbose_name='Cuerpo del mensaje')
   enviadopor = models.CharField(max_length=50, verbose_name='Enviado por:')

   class Meta:
      verbose_name_plural = "Agregar avances"
      ordering = ('fecha', 'tipo_envio', 'titulo_mensaje', 'status', 'enviadopor')

   def __unicode__(self):
      ''':return: Representacion en cadena de la clase avances'''
      boletin = "Estatus: %s - Titulo: %s - Tipo de envio: %s" % (self.status, self.titulo_mensaje, self.tipo_envio)
      return boletin


class Diarios(models.Model):
   '''Clase para los diarios'''
   pais = models.CharField(max_length=110, verbose_name='Pais', blank=True, null=True)
   estado = models.CharField(max_length=110, verbose_name='Estado', blank=True, null=True)
   nombre_diario = models.CharField(max_length=110, verbose_name='Diario', blank=True, null=True)

   class Meta:
      verbose_name_plural = "Agregar diario"
      ordering = ('nombre_diario',)

   def __unicode__(self):
      ''':return: Representacion en cadena de la clase diarios'''
      diario = "Diario: %s" % (self.nombre_diario,)
      return diario


class Noticias(models.Model):
    '''Clase para noticias'''
    #Campos necesarios
    avances = models.ForeignKey(Avances, verbose_name='Avances', blank=True, null=True)
    fecha = models.DateField(default=datetime.now, blank=True)
    hora = models.TimeField(auto_now_add=True, blank=True, null=True)
    tag = models.CharField(max_length=30, verbose_name='Etiqueta', choices=TAG, default='')
    status = models.CharField(max_length=110, verbose_name='Status', blank=True, null=True)
    enviadopor = models.CharField(max_length=50, verbose_name='Enviado por:')
    titulo_noticia = models.CharField(max_length=500, verbose_name='Titulo')
    antetitulo_noticia = models.CharField(max_length=500, verbose_name='Antetitulo', blank=True)
    enviadopor = models.CharField(max_length=50, verbose_name='Enviado por:')
    noticia = models.TextField(verbose_name='Extracto de la noticia')

    class Meta:
        verbose_name_plural = "Agregar noticias para avances"
        ordering = ('status',)

    def __unicode__(self):
        ''':return: Representacion en cadena de la clase noticias'''
        noticia = "ID: %s - Titulo de noticia: %s " % (self.id, self.titulo_noticia)
        return noticia


class EnlaceDiarios(models.Model):
    ''' Clase para vincular enlaces con Diarios '''
    diario = models.ForeignKey(Diarios)
    noticia = models.ForeignKey(Noticias)
    url = models.URLField(verbose_name='Enlace de noticia')

    class Meta:
        verbose_name_plural = "Enlace de Noticias"
        ordering = ('diario', 'noticia', 'url')

    def __unicode__(self):
        url = "Diario: %s - URL: %s" % (self.diario, self.url)
        return url
