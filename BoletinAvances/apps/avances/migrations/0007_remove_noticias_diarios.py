# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-10 14:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avances', '0006_auto_20160315_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticias',
            name='diarios',
        ),
    ]
