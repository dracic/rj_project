# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-19 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upis', '0002_gj_povrsina'),
    ]

    operations = [
        migrations.AddField(
            model_name='gj',
            name='drvna_zaliha',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
