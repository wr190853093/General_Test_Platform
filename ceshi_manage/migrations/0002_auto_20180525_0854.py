# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceshi_manage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.SmallIntegerField(default=1, choices=[(0, '\u8df3\u8fc7'), (1, '\u542f\u7528')]),
        ),
    ]
