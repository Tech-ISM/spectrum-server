# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-25 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('image', models.ImageField(default='/media/shop/default.png', upload_to='event/')),
                ('time', models.CharField(blank=True, max_length=120, null=True)),
                ('date', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=120, null=True)),
                ('day', models.IntegerField(blank=True, default=0, null=True)),
                ('attendees', models.IntegerField(blank=True, default=0, null=True)),
                ('description', models.CharField(blank=True, max_length=120, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=255, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
