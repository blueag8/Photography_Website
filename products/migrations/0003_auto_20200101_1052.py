# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-01 10:52
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191231_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('1', 'A4 (1 x 29.7cm)'), ('2', 'A3 (29 x 42cm)'), ('3', 'A3 + (32.9 x 48.3cm)')], default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]