# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-24 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.ImageField(upload_to=''),
        ),
    ]
