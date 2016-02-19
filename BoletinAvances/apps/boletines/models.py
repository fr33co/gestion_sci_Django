import os
from django.db import models
from datetime import datetime
from BoletinAvances.apps.listas.models import Listas
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


TIPO_ENVIO = (
    ('Automatico', 'Automatico'),
    ('Programado', 'Programado'),
)

class Boletines(models.Model):
   '''Clase para los boletines'''
   fecha = models.DateField(default=datetime.now, blank=True)
   hora = models.TimeField(auto_now_add=True, blank=True)
   tipo_envio = models.CharField(max_length=20, choices=TIPO_ENVIO, default='A', verbose_name='Tipo de envio')
   status = models.CharField(max_length=110, verbose_name='Status', blank=True, null=True)
   listas = models.ManyToManyField(Listas)
   titulo_mensaje = models.CharField(max_length=110, verbose_name='Titulo')
   cuerpo_mensaje = models.TextField(verbose_name='Cuerpo del mensaje')
   enviadopor = models.CharField(max_length=50, verbose_name='Enviado por:')
    
   class Meta:
      verbose_name_plural = "Agregar boletin"
      ordering = ('fecha', 'tipo_envio', 'titulo_mensaje', 'status', 'enviadopor')

   def __unicode__(self):
      ''':return: Representacion en cadena de la clase boletines'''
      boletin = "Estatus: %s - Titulo: %s - Tipo de envio: %s" % (self.status, self.titulo_mensaje, self.tipo_envio)
      return boletin   


class Archivos(models.Model):
    '''Clase para archivos'''
    #Campos necesarios
    boletines = models.ForeignKey(Boletines, verbose_name='Boletines', blank=True, null=True)
    documento = models.FileField(upload_to='archivos_boletin/', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Archivos de los boletines"
        ordering = ('documento', )

    def __unicode__(self):
        ''':return: Representacion en cadena de la clase Archivos'''
        return unicode(self.documento) or u''
      
      
@receiver(pre_delete, sender=Archivos)
def Boletines_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.documento.delete(False)