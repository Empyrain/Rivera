# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-14 08:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_auto_20160914_1114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='id',
            new_name='message_id',
        ),
    ]