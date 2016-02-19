# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primerasplanas', '0002_auto_20151128_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='primerasplanas',
            name='cuerpo_mensaje',
            field=models.TextField(null=True, verbose_name=b'Cuerpo del mensaje', blank=True),
        ),
        migrations.AddField(
            model_name='primerasplanas',
            name='titulo_mensaje',
            field=models.CharField(max_length=110, null=True, verbose_name=b'Titulo', blank=True),
        ),
    ]
