# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-06 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacker_news', '0002_news_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='comments',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='upvotes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]