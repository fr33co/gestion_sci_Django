# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primerasplanas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='primerasplanas',
            options={'ordering': ('fecha', 'status', 'enviadopor'), 'verbose_name_plural': 'Agregar primera plana'},
        ),
        migrations.RemoveField(
            model_name='primerasplanas',
            name='categoria',
        ),
        migrations.AddField(
            model_name='archivos',
            name='categoria',
            field=models.CharField(default=b'', max_length=20, verbose_name=b'Categoria', choices=[(b'Medios Impresos Carabobo', b'Medios Impresos Carabobo'), (b'Medios Impresos Aragua', b'Medios Impresos Aragua'), (b'Medios Impresos Nacionales', b'Medios Impresos Nacionales')]),
        ),
    ]
