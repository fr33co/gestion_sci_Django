# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 17:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avances', '0002_auto_20160314_1258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enlacediarios',
            options={'ordering': ('diario', 'noticia', 'url'), 'verbose_name_plural': 'Enlace de Noticias'},
        ),
    ]
