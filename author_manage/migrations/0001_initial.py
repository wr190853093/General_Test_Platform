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
                ('parent', models.IntegerField(null=True)),
                ('is_del', models.SmallIntegerField(null=True, choices=[(0, '\u5df2\u5220\u9664'), (1, '\u672a\u5220\u9664')])),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('username', models.CharField(unique=True, max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.SmallIntegerField(choices=[(0, '\u4ea7\u54c1\u7ecf\u7406'), (1, '\u5f00\u53d1'), (2, '\u6d4b\u8bd5'), (3, '\u8fd0\u7ef4')])),
                ('status', models.SmallIntegerField(choices=[(0, '\u79bb\u804c'), (1, '\u5728\u804c')])),
                ('is_del', models.SmallIntegerField(null=True, choices=[(0, '\u5df2\u5220\u9664'), (1, '\u672a\u5220\u9664')])),
                ('password', models.CharField(max_length=128)),
                ('org', models.ForeignKey(to='author_manage.Organization')),
            ],
        ),
    ]
