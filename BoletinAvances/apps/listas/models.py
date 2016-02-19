#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Modelos para Listas'''

from django.db import models

TIPO_LISTA = (
    ('Boletin', 'Boletin'),
    ('Avance', 'Avance'),
    ('Resumen', 'Resumen'),
    ('Primeras planas', 'Primeras planas'),
    ('Columna de opinión', 'Columna de opinión'),
    ('Informe de Televisión', 'Informe de Televisión'),
)


class Listas(models.Model):
    '''Informacion de las Listas'''
    tipo_lista = models.CharField(max_length=20, choices=TIPO_LISTA, default='Boletin', verbose_name='Tipo de lista')
    nombre_lista = models.CharField(max_length=100, verbose_name='Nombre de la lista', unique=True)
    descripcion_lista = models.TextField(max_length=1000, verbose_name='Descripcion de la lista')

    class Meta:
        verbose_name_plural = "Agregar Listas"
        ordering = ('nombre_lista', )

    def __unicode__(self):
        ''':return: Representacion en cadena de la clase Listas'''
        listas = "%s" % (self.nombre_lista)
        return listas