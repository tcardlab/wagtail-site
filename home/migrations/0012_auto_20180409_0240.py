# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-09 02:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_aboutpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
