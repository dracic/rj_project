# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-19 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gj',
            name='povrsina',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10),
        ),
    ]