# Generated by Django 2.0.7 on 2018-08-28 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manage', '0007_auto_20180828_2237'),
        ('ceshi_manage', '0006_auto_20180828_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskenvironment',
            name='case',
        ),
        migrations.RemoveField(
            model_name='taskenvironment',
            name='environment',
        ),
        migrations.RemoveField(
            model_name='taskenvironment',
            name='step',
        ),
        migrations.RemoveField(
            model_name='taskenvironment',
            name='task',
        ),
        migrations.AddField(
            model_name='task',
            name='case',
            field=models.ManyToManyField(to='ceshi_manage.Case'),
        ),
        migrations.AddField(
            model_name='task',
            name='environment',
            field=models.ManyToManyField(to='project_manage.Environment'),
        ),
        migrations.AddField(
            model_name='task',
            name='step',
            field=models.ManyToManyField(to='ceshi_manage.Step'),
        ),
        migrations.DeleteModel(
            name='TaskEnvironment',
        ),
    ]