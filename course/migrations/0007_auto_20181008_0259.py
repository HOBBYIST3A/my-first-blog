# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-10-07 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lecturer', '0003_auto_20180908_2310'),
        ('course', '0006_auto_20180926_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='day',
        ),
        migrations.AddField(
            model_name='schedule',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lecturer.Lecturer'),
        ),
    ]
