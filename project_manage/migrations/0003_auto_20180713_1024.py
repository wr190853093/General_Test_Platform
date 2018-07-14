# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_manage', '0002_auto_20180712_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.SmallIntegerField(default=1, choices=[(0, '\u5f52\u6863'), (1, '\u6b63\u5e38')]),
        ),
    ]
