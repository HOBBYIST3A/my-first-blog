# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-10-16 05:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_schedule_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='course',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='course.Course'),
            preserve_default=False,
        ),
    ]
