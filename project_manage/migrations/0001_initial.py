# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author_manage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('host', models.CharField(max_length=20)),
                ('method', models.SmallIntegerField(choices=[(0, b'GET'), (1, b'POST')])),
                ('is_del', models.SmallIntegerField(default=1, choices=[(0, '\u5df2\u5220\u9664'), (1, '\u672a\u5220\u9664')])),
            ],
        ),
        migrations.CreateModel(
            name='BodyPara',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_type', models.SmallIntegerField(choices=[(0, b'x-www-form-urlencoded'), (1, b'json')])),
                ('is_del', models.SmallIntegerField(default=1, choices=[(0, '\u5df2\u5220\u9664'), (1, '\u672a\u5220\u9664')])),
                ('api', models.ForeignKey(to='project_manage.Api')),
            ],
        ),
        migrations.CreateModel(
            name='ComplexPara',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_del', models.SmallIntegerField(default=1, choices=[(0, '\u5df2\u5220\u9664'), (1, '\u672a\u5220\u9664')])),
            ],
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('host', models.CharField(max_length=20)),
                ('status', models.SmallIntegerField(default=1, choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528')])),
                ('is_del', models.SmallIntegerField(default=1, choices=[(0, '\u5df2\u5220\u9664'), (1, '\u672a\u5220\u9664')])),
                ('type', models.SmallIntegerField(choices=[(0, '\u5f00\u53d1\u73af\u5883'), (1, '\u6d4b\u8bd5\u73af\u5883'), (2, '\u51c6\u751f\u4ea7\u73af\u5883'), (3, '\u751f\u4ea7\u73af\u5883')])),
            ],
        ),
        migrations.CreateModel(
            name='HeaderPara',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_del', models.SmallIntegerField(default=1, choices=[(0, '\u5df2\u5220\u9664'), (1, '\u672a\u5220\u9664')])),
                ('api', models.ForeignKey(to='project_manage.Api')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('is_del', models.SmallIntegerField(default=1, choices=[(0, '\u5df2\u5220\u9664'), (1, '\u672a\u5220\u9664')])),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', models.ForeignKey(blank=True, to='project_manage.Module', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=30)),
                ('is_null', models.SmallIntegerField(null=True, choices=[(0, '\u4e0d\u53ef\u4e3a\u7a7a'), (1, '\u53ef\u4e3a\u7a7a')])),
                ('is_del', models.SmallIntegerField(default=1, choices=[(0, '\u5df2\u5220\u9664'), (1, '\u672a\u5220\u9664')])),
                ('data_type', models.SmallIntegerField(choices=[(0, b'string'), (1, b'number'), (2, b'object'), (3, b'boolean'), (4, b'array')])),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('status', models.SmallIntegerField(default=1, choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528')])),
                ('team', models.ManyToManyField(to='author_manage.Users')),
            ],
        ),
        migrations.CreateModel(
            name='ResponsePara',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_del', models.SmallIntegerField(default=1, choices=[(0, '\u5df2\u5220\u9664'), (1, '\u672a\u5220\u9664')])),
                ('api', models.ForeignKey(to='project_manage.Api')),
                ('para', models.ForeignKey(to='project_manage.Parameter')),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='project',
            field=models.ForeignKey(to='project_manage.Project'),
        ),
        migrations.AddField(
            model_name='headerpara',
            name='para',
            field=models.ForeignKey(to='project_manage.Parameter'),
        ),
        migrations.AddField(
            model_name='environment',
            name='project',
            field=models.ForeignKey(to='project_manage.Project'),
        ),
        migrations.AddField(
            model_name='complexpara',
            name='chirld_para',
            field=models.ForeignKey(related_name='chirld_para', to='project_manage.Parameter'),
        ),
        migrations.AddField(
            model_name='complexpara',
            name='parent_para',
            field=models.ForeignKey(related_name='parent_para', to='project_manage.Parameter'),
        ),
        migrations.AddField(
            model_name='bodypara',
            name='para',
            field=models.ForeignKey(to='project_manage.Parameter'),
        ),
        migrations.AddField(
            model_name='api',
            name='module',
            field=models.ForeignKey(to='project_manage.Module'),
        ),
        migrations.AddField(
            model_name='api',
            name='project',
            field=models.ForeignKey(to='project_manage.Project'),
        ),
    ]
