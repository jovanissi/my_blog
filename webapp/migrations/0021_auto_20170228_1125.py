# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0020_auto_20170228_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headlines',
            name='classifications',
            field=models.CharField(choices=[('Social', 'Social'), ('Science', 'Science'), ('Tech', 'Tech')], default='Tech', max_length=200),
        ),
        migrations.AlterField(
            model_name='user_comment',
            name='reference',
            field=models.IntegerField(default=0, verbose_name='0%s'),
        ),
    ]
