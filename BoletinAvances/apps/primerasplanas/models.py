import os
from django.db import models
from datetime import datetime
from BoletinAvances.apps.listas.models import Listas
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


CATEGORIA = (
    ('Medios Impresos Carabobo', 'Medios Impresos Carabobo'),
    ('Medios Impresos Aragua', 'Medios Impresos Aragua'),
    ('Medios Impresos Nacionales', 'Medios Impresos Nacionales'),
)

class PrimerasPlanas(models.Model):
   '''Clase para los primeras planas'''
   fecha = models.DateField(default=datetime.now, blank=True)
   status = models.CharField(max_length=110, verbose_name='Status', blank=True, null=True)
   titulo_mensaje = models.CharField(max_length=110, verbose_name='Titulo', blank=True, null=True)
   cuerpo_mensaje = models.TextField(verbose_name='Cuerpo del mensaje', blank=True, null=True)
   listas = models.ManyToManyField(Listas)
   enviadopor = models.CharField(max_length=50, verbose_name='Enviado por:')
    
   class Meta:
      verbose_name_plural = "Agregar primera plana"
      ordering = ('fecha', 'status', 'enviadopor')

   def __unicode__(self):
      ''':return: Representacion en cadena de la clase boletines'''
      primeraplana = "Fecha: %s - Titulo: %s - Enviado por: %s" % (self.fecha, self.titulo_mensaje, self.enviadopor)
      return primeraplana   


class Archivos(models.Model):
    '''Clase para archivos'''
    #Campos necesarios
    primeraplana = models.ForeignKey(PrimerasPlanas, verbose_name='Primeras Planas', blank=True, null=True)
    documento = models.FileField(upload_to='archivos_primeras_planas/', blank=True, null=True)
    categoria = models.CharField(max_length=30, choices=CATEGORIA, default='', verbose_name='Categoria')
    
    class Meta:
        verbose_name_plural = "Archivos de las primeras planas"
        ordering = ('documento', )

    def __unicode__(self):
        ''':return: Representacion en cadena de la clase Archivos'''
        return unicode(self.documento) or u''
      
      
@receiver(pre_delete, sender=Archivos)
def PrimerasPlanas_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.documento.delete(False)