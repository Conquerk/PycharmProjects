# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-12-21 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_book_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_set',
            field=models.ManyToManyField(to='index.Author'),
        ),
    ]