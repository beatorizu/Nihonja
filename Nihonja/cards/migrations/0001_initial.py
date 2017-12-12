# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-12 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phrase', models.CharField(max_length=100, verbose_name='Frase')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('kanji', models.TextField(verbose_name='Kanji')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Cartão',
                'verbose_name_plural': 'Cartões',
                'ordering': ['phrase'],
            },
        ),
    ]
