# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='lat',
            field=models.FloatField(default=40.233671),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='area',
            name='lng',
            field=models.FloatField(default=-111.658673),
            preserve_default=False,
        ),
    ]
