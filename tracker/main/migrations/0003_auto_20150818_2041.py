# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150813_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='order',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
