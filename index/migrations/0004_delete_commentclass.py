# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-27 05:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_commentclass_commentdate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CommentClass',
        ),
    ]
