# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-13 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handover', '0011_auto_20181113_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistdocument',
            name='random_field',
            field=models.CharField(blank=True, default='1578099', max_length=7, unique=True),
        ),
    ]
