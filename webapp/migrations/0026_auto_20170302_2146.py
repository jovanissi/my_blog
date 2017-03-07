# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0025_auto_20170228_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headlines',
            name='classifications',
            field=models.CharField(choices=[('Tech', 'Tech'), ('Science', 'Science'), ('Social', 'Social')], default='Tech', max_length=200),
        ),
    ]
