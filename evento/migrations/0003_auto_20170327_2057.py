# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 23:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0002_auto_20170327_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='cep',
            field=models.CharField(max_length=200, verbose_name='cep'),
        ),
        migrations.AlterField(
            model_name='pessoajuridica',
            name='razaoSocial',
            field=models.CharField(max_length=200, verbose_name='razao social'),
        ),
    ]
