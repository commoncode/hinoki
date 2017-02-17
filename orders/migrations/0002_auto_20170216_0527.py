# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 05:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='english_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='ingredients',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='is_glutenfree',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='is_vegan',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='is_vegetarian',
            field=models.BooleanField(default=False),
        ),
    ]