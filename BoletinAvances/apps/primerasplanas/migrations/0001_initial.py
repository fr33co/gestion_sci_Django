# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('listas', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('documento', models.FileField(null=True, upload_to=b'archivos_primeras_planas/', blank=True)),
            ],
            options={
                'ordering': ('documento',),
                'verbose_name_plural': 'Archivos de las primeras planas',
            },
        ),
        migrations.CreateModel(
            name='PrimerasPlanas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.datetime.now, blank=True)),
                ('categoria', models.CharField(default=b'A', max_length=20, verbose_name=b'Categoria', choices=[(b'Medios Impresos Carabobo', b'Medios Impresos Carabobo'), (b'Medios Impresos Aragua', b'Medios Impresos Aragua'), (b'Medios Impresos Nacionales', b'Medios Impresos Nacionales')])),
                ('status', models.CharField(max_length=110, null=True, verbose_name=b'Status', blank=True)),
                ('enviadopor', models.CharField(max_length=50, verbose_name=b'Enviado por:')),
                ('listas', models.ManyToManyField(to='listas.Listas')),
            ],
            options={
                'ordering': ('fecha', 'categoria', 'status', 'enviadopor'),
                'verbose_name_plural': 'Agregar primera plana',
            },
        ),
        migrations.AddField(
            model_name='archivos',
            name='primeraplana',
            field=models.ForeignKey(verbose_name=b'Primeras Planas', blank=True, to='primerasplanas.PrimerasPlanas', null=True),
        ),
    ]
