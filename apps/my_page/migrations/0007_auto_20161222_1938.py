# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-22 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_page', '0006_auto_20161222_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True)),
                ('fa_class', models.CharField(max_length=24)),
            ],
        ),
        migrations.RemoveField(
            model_name='aboutme',
            name='location',
        ),
        migrations.AddField(
            model_name='aboutme',
            name='position',
            field=models.CharField(default='Full Stack Web Developer', max_length=128),
        ),
    ]