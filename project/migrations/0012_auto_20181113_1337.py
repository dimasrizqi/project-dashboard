# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-13 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_partner_partner_alias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='partner_alias',
            field=models.CharField(max_length=5),
        ),
    ]
