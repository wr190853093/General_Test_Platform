# Generated by Django 2.0.7 on 2018-08-23 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceshi_manage', '0003_auto_20180821_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='step',
            name='check',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='step',
            name='headers',
            field=models.TextField(null=True),
        ),
    ]
