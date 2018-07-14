# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('author_manage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='author_manage.Organization', null=True),
        ),
    ]
