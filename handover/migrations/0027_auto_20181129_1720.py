# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-29 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handover', '0026_auto_20181129_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistdocument',
            name='random_field',
            field=models.CharField(blank=True, default='2019863', max_length=7, unique=True),
        ),
    ]
