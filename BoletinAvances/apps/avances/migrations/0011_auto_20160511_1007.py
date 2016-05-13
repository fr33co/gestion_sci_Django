# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-11 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avances', '0010_auto_20160511_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avances',
            name='tipo_envio',
            field=models.CharField(choices=[(b'Automatico', b'Automatico'), (b'Programado', b'Programado')], default=b'0', max_length=20, verbose_name=b'Tipo de envio'),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='tag',
            field=models.CharField(choices=[(b'0', b'----'), (b'REG', b'Regionales'), (b'NAC', b'Nacionales'), (b'INT', b'Internacionales'), (b'ECO', b'Economia'), (b'DEP', b'Deporte'), (b'SUC', b'Sucesos')], default=b'', max_length=30, verbose_name=b'Etiqueta'),
        ),
    ]