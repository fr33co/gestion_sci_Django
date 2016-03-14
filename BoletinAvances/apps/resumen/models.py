from django.db import models
from datetime import datetime

from BoletinAvances.apps.listas.models import Listas

TAG = (
    ('REG', 'Regionales'),
    ('NAC', 'Nacionales'),
    ('INT', 'Internacionales'),
    ('ECO', 'Economia'),
    ('DEP', 'Deporte'),
    ('SUC', 'Sucesos'),
)

TIPO_ENVIO = (
    ('Automatico', 'Automatico'),
    ('Programado', 'Programado'),
)

class Resumen(models.Model):
    ''' Clase para Resumen '''
    titulo_mensaje = models.CharField(max_length=150, verbose_name='Titulo', default='')
    cuerpo_mensaje = models.TextField(verbose_name='Cuerpo el mensaje', default='')
    tipo_envio = models.CharField(max_length=20, choices=TIPO_ENVIO, default='', verbose_name='Tipo de envio')
    fecha = models.DateField(default=datetime.now, blank=True, null=True)
    hora = models.TimeField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(max_length=110, verbose_name='Status', blank=True, null=True)
    enviadopor = models.CharField(max_length=50, verbose_name='Enviado por:', default='')
    lista = models.ManyToManyField(Listas)

    class Meta:
        verbose_name_plural = "Agregar Resumen"
        ordering = ('fecha', 'status', 'enviadopor',)

    def __unicode__(self):
         ''':return: Representacion en cadena de la clase Resumen'''
         resumen = "Fecha: %s - Titulo: %s - Enviado por: %s" % (self.fecha, self.titulo_mensaje, self.enviadopor)
         return resumen

class NoticiaResumen(models.Model):
    ''' Clase para Resumen de Noticia '''
    resumenes = models.ForeignKey(Resumen, verbose_name='Resumen', blank=True, null=True)
    titulo_noticia_resumen = models.CharField(max_length=350, verbose_name='Titulo de Resumen')
    cuerpo_noticia_resumen = models.TextField(verbose_name='Cuerpo del resumen', default='')
    tag_noticia_resumen = models.CharField(max_length=30, verbose_name='Etiqueta', choices=TAG, default='')
    url_noticia_resumen = models.TextField(verbose_name='URLs')
    status = models.CharField(max_length=110, verbose_name='Status', blank=True, null=True)
    enviadopor_noticia_resumen = models.CharField(max_length=50, verbose_name='Enviado por:', default='')
    fecha_noticia_resumen = models.DateField(default=datetime.now, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Agregar Resumen de Noticia"
        ordering = ('tag_noticia_resumen', 'titulo_noticia_resumen',)
