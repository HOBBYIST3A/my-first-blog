# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-11 09:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_auto_20180604_1818'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notice',
            options={'ordering': ['-pk']},
        ),
    ]
