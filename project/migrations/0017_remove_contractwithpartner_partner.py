# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-27 06:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_auto_20181127_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contractwithpartner',
            name='partner',
        ),
    ]