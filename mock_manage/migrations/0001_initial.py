# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_manage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header_key', models.CharField(max_length=20)),
                ('header_value', models.CharField(max_length=400)),
                ('body_content_type', models.SmallIntegerField(choices=[(0, b'x-www-form-urlencoded'), (1, b'json')])),
                ('body_key', models.CharField(max_length=20)),
                ('body_value', models.CharField(max_length=400)),
                ('respone_value', models.CharField(max_length=400)),
                ('api', models.ForeignKey(to='project_manage.Api')),
                ('module', models.ForeignKey(to='project_manage.Module')),
                ('project', models.ForeignKey(to='project_manage.Project')),
            ],
        ),
    ]
