# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('is_del', models.SmallIntegerField(default=1, choices=[(0, '\u5df2\u5220\u9664'), (1, '\u672a\u5220\u9664')])),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', models.ForeignKey(blank=True, to='author_manage.Organization', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('username', models.CharField(unique=True, max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.SmallIntegerField(choices=[(0, '\u4ea7\u54c1\u7ecf\u7406'), (1, '\u5f00\u53d1'), (2, '\u6d4b\u8bd5'), (3, '\u8fd0\u7ef4')])),
                ('status', models.SmallIntegerField(default=1, choices=[(0, '\u79bb\u804c'), (1, '\u5728\u804c')])),
                ('is_del', models.SmallIntegerField(default=1, choices=[(0, '\u5df2\u5220\u9664'), (1, '\u672a\u5220\u9664')])),
                ('password', models.CharField(max_length=128)),
                ('org', models.ForeignKey(to='author_manage.Organization')),
            ],
        ),
    ]
