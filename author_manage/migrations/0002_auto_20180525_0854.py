# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author_manage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='is_del',
            field=models.SmallIntegerField(default=1, choices=[(0, '\u5df2\u5220\u9664'), (1, '\u672a\u5220\u9664')]),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_del',
            field=models.SmallIntegerField(default=1, choices=[(0, '\u5df2\u5220\u9664'), (1, '\u672a\u5220\u9664')]),
        ),
        migrations.AlterField(
            model_name='users',
            name='status',
            field=models.SmallIntegerField(default=1, choices=[(0, '\u79bb\u804c'), (1, '\u5728\u804c')]),
        ),
    ]
