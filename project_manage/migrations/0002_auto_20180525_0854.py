# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_manage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='is_del',
            field=models.SmallIntegerField(default=1, choices=[(0, '\u5df2\u5220\u9664'), (1, '\u672a\u5220\u9664')]),
        ),
        migrations.AlterField(
            model_name='bodypara',
            name='is_del',
            field=models.SmallIntegerField(default=1, choices=[(0, '\u5df2\u5220\u9664'), (1, '\u672a\u5220\u9664')]),
        ),
        migrations.AlterField(
            model_name='complexpara',
            name='is_del',
            field=models.SmallIntegerField(default=1, choices=[(0, '\u5df2\u5220\u9664'), (1, '\u672a\u5220\u9664')]),
        ),
        migrations.AlterField(
            model_name='environment',
            name='is_del',
            field=models.SmallIntegerField(default=1, choices=[(0, '\u5df2\u5220\u9664'), (1, '\u672a\u5220\u9664')]),
        ),
        migrations.AlterField(
            model_name='environment',
            name='status',
            field=models.SmallIntegerField(default=1, choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528')]),
        ),
        migrations.AlterField(
            model_name='headerpara',
            name='is_del',
            field=models.SmallIntegerField(default=1, choices=[(0, '\u5df2\u5220\u9664'), (1, '\u672a\u5220\u9664')]),
        ),
        migrations.AlterField(
            model_name='module',
            name='is_del',
            field=models.SmallIntegerField(default=1, choices=[(0, '\u5df2\u5220\u9664'), (1, '\u672a\u5220\u9664')]),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='is_del',
            field=models.SmallIntegerField(default=1, choices=[(0, '\u5df2\u5220\u9664'), (1, '\u672a\u5220\u9664')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.SmallIntegerField(default=1, choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528')]),
        ),
        migrations.AlterField(
            model_name='responsepara',
            name='is_del',
            field=models.SmallIntegerField(default=1, choices=[(0, '\u5df2\u5220\u9664'), (1, '\u672a\u5220\u9664')]),
        ),
    ]
