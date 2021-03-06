# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0026_auto_20170302_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_comment',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='headlines',
            name='classifications',
            field=models.CharField(choices=[('Social', 'Social'), ('Science', 'Science'), ('Tech', 'Tech')], default='Tech', max_length=200),
        ),
    ]
