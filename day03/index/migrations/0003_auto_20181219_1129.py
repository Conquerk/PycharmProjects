# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-12-19 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_author_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publicate_date',
            field=models.DateField(),
        ),
    ]
