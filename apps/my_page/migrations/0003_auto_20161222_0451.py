# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-22 04:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_page', '0002_portfolioapp_rank'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolioapp',
            options={'ordering': ('rank',)},
        ),
    ]
