# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('project_manage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='project_manage.Module', null=True),
        ),
    ]
