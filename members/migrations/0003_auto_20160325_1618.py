# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 16:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20160325_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='address_city',
            field=models.CharField(default='Sta. Rosa', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='address_st',
            field=models.CharField(default='109 Mahogany St', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='address_village',
            field=models.CharField(default='SRVI', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='birthday',
            field=models.DateField(blank=True, default=datetime.date(2016, 3, 25)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='kfc_to_yfc',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='nickname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
