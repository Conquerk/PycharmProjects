# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-12-20 02:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20181219_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='isActive',
            field=models.CharField(default=True, max_length=10),
        ),
    ]
