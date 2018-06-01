# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mock_manage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mock',
            old_name='respone_value',
            new_name='response_value',
        ),
    ]
