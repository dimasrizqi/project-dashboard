# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-27 06:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_contractwithpartner_partner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contractwithpartner',
            name='partner',
        ),
        migrations.AddField(
            model_name='contractwithpartner',
            name='partner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='project.Partner'),
            preserve_default=False,
        ),
    ]
