# Generated by Django 2.0.7 on 2018-08-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manage', '0006_auto_20180804_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environment',
            name='host',
            field=models.CharField(default='NULL', max_length=50),
        ),
    ]
