# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_auto_20170227_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_comment',
            name='reference',
            field=models.IntegerField(default=0),
        ),
    ]
