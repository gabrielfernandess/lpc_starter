# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 00:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0004_auto_20170327_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataEHoraDaInscricao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='data e hora da inscrição')),
                ('tipoDaInscricao', models.CharField(max_length=200, verbose_name='Tipo da Inscricao')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.Evento')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.PessoaFisica')),
            ],
        ),
    ]
