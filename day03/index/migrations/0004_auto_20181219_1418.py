# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-12-19 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20181219_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(),
        ),
    ]