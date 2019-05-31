# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-16 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0019_auto_20171023_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardpage',
            name='introduction',
            field=models.CharField(blank=True, help_text='Enter the title to display on the page, you can use only 255 characters.', max_length=255),
        ),
    ]