# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-25 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_auto_20161115_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]