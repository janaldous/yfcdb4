# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20160326_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='illness',
            field=models.CharField(blank=True, help_text='Illnesses that require special attention', max_length=100),
        ),
        migrations.AddField(
            model_name='member',
            name='special_skills',
            field=models.CharField(blank=True, help_text='(eg playing musical instruments, dancing, singing, etc)', max_length=100),
        ),
    ]