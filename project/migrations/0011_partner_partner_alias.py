# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-13 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_auto_20181113_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='partner_alias',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
