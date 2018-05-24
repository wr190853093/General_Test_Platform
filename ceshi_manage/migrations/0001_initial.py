# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_manage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('status', models.SmallIntegerField(choices=[(0, '\u8df3\u8fc7'), (1, '\u542f\u7528')])),
                ('desc', models.CharField(max_length=30)),
                ('project', models.ForeignKey(to='project_manage.Project')),
            ],
        ),
        migrations.CreateModel(
            name='CheckPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.SmallIntegerField(choices=[(0, b'herader value'), (2, b'body value')])),
                ('key', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=30)),
                ('order', models.IntegerField(default=1)),
                ('para_type', models.SmallIntegerField(choices=[(10, b'herader para'), (21, b'body para urlencoded'), (22, b'body para json')])),
                ('key', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=400)),
                ('api', models.ForeignKey(to='project_manage.Api')),
                ('case', models.ForeignKey(to='ceshi_manage.Case')),
                ('para', models.ForeignKey(to='project_manage.Parameter')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=30)),
                ('case', models.ManyToManyField(to='ceshi_manage.Case')),
                ('environment', models.ForeignKey(to='project_manage.Environment')),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='task',
            field=models.ManyToManyField(to='ceshi_manage.Task'),
        ),
        migrations.AddField(
            model_name='checkpoint',
            name='step',
            field=models.ForeignKey(to='ceshi_manage.Step'),
        ),
    ]
