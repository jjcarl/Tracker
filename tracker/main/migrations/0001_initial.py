# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='areas', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date_created',),
            },
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('order', models.IntegerField()),
                ('area', models.ForeignKey(related_name='points', to='main.Area')),
            ],
        ),
    ]
