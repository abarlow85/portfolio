# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-22 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioapp',
            name='rank',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
