# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-10 04:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import questions.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpectedOutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=questions.models.upload_expected_output_file_location)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['file'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('title', models.CharField(max_length=120, unique=True)),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=questions.models.upload_test_case_file_location)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question')),
            ],
            options={
                'ordering': ['file'],
            },
        ),
        migrations.AddField(
            model_name='expectedoutput',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question'),
        ),
        migrations.AddField(
            model_name='expectedoutput',
            name='test_case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.TestCase'),
        ),
    ]
