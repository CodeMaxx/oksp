# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-07 12:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hacker_news', '0008_comment_comment_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_link',
        ),
    ]
