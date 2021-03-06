# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='headlines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_img', models.FileField(default='null', upload_to='uploads/images')),
                ('title', models.TextField(default='null')),
                ('classifications', models.CharField(choices=[('Science', 'Science'), ('Tech', 'Tech'), ('Social', 'Social')], default='Tech', max_length=200)),
                ('sub_classifications', models.CharField(choices=[('Sports', 'Sports'), ('Leisure', 'Sports'), ('Physics', 'Physics'), ('Biology', 'Biology'), ('Computers', 'Computers'), ('Gadgets', 'Gadgets'), ('Phones', 'Phones'), ('History', 'History'), ('Geography', 'Geography')], default='Computers', max_length=200)),
            ],
        ),
    ]
