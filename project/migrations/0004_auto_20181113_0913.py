# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-13 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20181113_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='kelengkapan_dokumen',
            field=models.CharField(choices=[('Lengkap', 'Lengkap'), ('Tidak Lengkap', 'Tidak Lengkap')], default='Tidak Lengkap', max_length=15),
        ),
    ]
