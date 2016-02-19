#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Modelos para Contactos'''

from django.db import models
from BoletinAvances.apps.listas.models import Listas


class Contactos(models.Model):
    '''Informacion de las Contactos'''
    nombre_contacto = models.CharField(max_length=50, verbose_name='Nombre y apellido del contacto')
    institucion = models.CharField(max_length=50, verbose_name='Institucion')
    telefono = models.CharField(max_length=50, verbose_name='Telefono', blank=True)
    correo = models.EmailField(verbose_name='Correo', blank=True)
    listas = models.ManyToManyField(Listas)

    class Meta:
        verbose_name_plural = "Agregar Contactos"
        ordering = ('nombre_contacto', )

    def __unicode__(self):
        ''':return: Representacion en cadena de la clase Contactos'''
        contactos = "%s" % (self.nombre_contacto)
        return contactos