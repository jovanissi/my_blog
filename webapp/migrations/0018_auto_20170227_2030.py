# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 20:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_user_comment_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headlines',
            name='classifications',
            field=models.CharField(choices=[('Science', 'Science'), ('Social', 'Social'), ('Tech', 'Tech')], default='Tech', max_length=200),
        ),
        migrations.AlterField(
            model_name='user_comment',
            name='reference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.headlines'),
        ),
    ]