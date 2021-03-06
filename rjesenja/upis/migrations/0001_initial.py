# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 08:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GJ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gj_id', models.CharField(max_length=3, unique=True)),
                ('gj_naziv', models.CharField(max_length=100)),
                ('godina', models.PositiveSmallIntegerField()),
                ('vrsta_elaborata', models.CharField(choices=[('Program', 'Program'), ('Osnova', 'Osnova')], default='Osnova', max_length=10)),
                ('obraslo', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('neobraslo_proizvodno', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('neobraslo_neproizvodno', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('neplodno', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('drvna_zaliha_debljinski_razredi', models.PositiveIntegerField(default=0)),
                ('drvna_zaliha_dobni_razredi', models.PositiveIntegerField(default=0)),
                ('prirast_debljinski_razredi', models.PositiveIntegerField(default=0)),
                ('prirast_dobni_razredi', models.PositiveIntegerField(default=0)),
                ('oos_povrsina', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('oos_zaliha', models.PositiveIntegerField(default=0)),
                ('gp_povrsina', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('gp_zaliha', models.PositiveIntegerField(default=0)),
                ('pp_povrsina', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('pp_zaliha', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Gospodarska jedinica',
                'verbose_name_plural': 'Gospodarske jedinice',
                'ordering': ['ušp', 'gj_id'],
            },
        ),
        migrations.CreateModel(
            name='UŠP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ušp_id', models.CharField(max_length=2, unique=True)),
                ('ušp_naziv', models.CharField(max_length=15, unique=True)),
            ],
            options={
                'verbose_name': 'Uprava šuma podružnica',
                'verbose_name_plural': 'UŠP',
                'ordering': ['ušp_id'],
            },
        ),
        migrations.AddField(
            model_name='gj',
            name='ušp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gjs', to='upis.UŠP'),
        ),
    ]
