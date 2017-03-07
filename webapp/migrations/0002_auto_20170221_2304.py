# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headlines',
            name='classifications',
            field=models.CharField(choices=[('Social', 'Social'), ('Science', 'Science'), ('Tech', 'Tech')], default='Tech', max_length=200),
        ),
        migrations.AlterField(
            model_name='headlines',
            name='sub_classifications',
            field=models.CharField(choices=[('Geography', 'Geography'), ('Phones', 'Phones'), ('History', 'History'), ('Sports', 'Sports'), ('Biology', 'Biology'), ('Physics', 'Physics'), ('Computers', 'Computers'), ('Gadgets', 'Gadgets'), ('Leisure', 'Sports')], default='Computers', max_length=200),
        ),
    ]