# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-27 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handover', '0019_auto_20181127_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistdocument',
            name='random_field',
            field=models.CharField(blank=True, default='4380097', max_length=7, unique=True),
        ),
    ]
