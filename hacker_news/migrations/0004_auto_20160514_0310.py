# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-13 21:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hacker_news', '0003_auto_20160514_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.Member'),
        ),
    ]
