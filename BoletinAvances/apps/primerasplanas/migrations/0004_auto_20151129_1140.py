# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primerasplanas', '0003_auto_20151128_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivos',
            name='categoria',
            field=models.CharField(default=b'', max_length=30, verbose_name=b'Categoria', choices=[(b'Medios Impresos Carabobo', b'Medios Impresos Carabobo'), (b'Medios Impresos Aragua', b'Medios Impresos Aragua'), (b'Medios Impresos Nacionales', b'Medios Impresos Nacionales')]),
        ),
    ]
