# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-09-02 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Md5Rainbow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plaintext', models.CharField(max_length=5, verbose_name='明文')),
                ('ciphertext', models.CharField(max_length=40, verbose_name='密文')),
            ],
            options={
                'verbose_name_plural': 'md5彩虹表',
                'db_table': 'md5_rainbow',
                'verbose_name': 'md5彩虹表',
            },
        ),
    ]