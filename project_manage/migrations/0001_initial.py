# Generated by Django 2.0.7 on 2018-08-04 13:52

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author_manage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=20, null=True)),
                ('path', models.CharField(default='NULL', max_length=20)),
                ('method', models.SmallIntegerField(choices=[(0, 'GET'), (1, 'POST')])),
                ('is_del', models.SmallIntegerField(choices=[(0, '已删除'), (1, '未删除')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='BodyPara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.SmallIntegerField(choices=[(0, 'x-www-form-urlencoded'), (1, 'json')])),
                ('is_del', models.SmallIntegerField(choices=[(0, '已删除'), (1, '未删除')], default=1)),
                ('api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_manage.Api')),
            ],
        ),
        migrations.CreateModel(
            name='ComplexPara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.SmallIntegerField(choices=[(0, '已删除'), (1, '未删除')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='NULL', max_length=30)),
                ('host', models.CharField(default='NULL', max_length=20)),
                ('status', models.SmallIntegerField(choices=[(0, '禁用'), (1, '启用')], default=1)),
                ('is_del', models.SmallIntegerField(choices=[(0, '已删除'), (1, '未删除')], default=1)),
                ('type', models.SmallIntegerField(choices=[(0, '开发环境'), (1, '测试环境'), (2, '准生产环境'), (3, '生产环境')])),
            ],
        ),
        migrations.CreateModel(
            name='HeaderPara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.SmallIntegerField(choices=[(0, '已删除'), (1, '未删除')], default=1)),
                ('api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_manage.Api')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('is_del', models.SmallIntegerField(choices=[(0, '已删除'), (1, '未删除')], default=1)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='project_manage.Module')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=30)),
                ('is_null', models.SmallIntegerField(choices=[(0, '不可为空'), (1, '可为空')], null=True)),
                ('is_del', models.SmallIntegerField(choices=[(0, '已删除'), (1, '未删除')], default=1)),
                ('data_type', models.SmallIntegerField(choices=[(0, 'string'), (1, 'number'), (2, 'object'), (3, 'boolean'), (4, 'array')])),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('status', models.SmallIntegerField(choices=[(0, '归档'), (1, '正常')], default=1)),
                ('team', models.ManyToManyField(to='author_manage.Users')),
            ],
        ),
        migrations.CreateModel(
            name='ResponsePara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.SmallIntegerField(choices=[(0, '已删除'), (1, '未删除')], default=1)),
                ('api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_manage.Api')),
                ('para', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_manage.Parameter')),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_manage.Project'),
        ),
        migrations.AddField(
            model_name='headerpara',
            name='para',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_manage.Parameter'),
        ),
        migrations.AddField(
            model_name='environment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_manage.Project'),
        ),
        migrations.AddField(
            model_name='complexpara',
            name='chirld_para',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chirld_para', to='project_manage.Parameter'),
        ),
        migrations.AddField(
            model_name='complexpara',
            name='parent_para',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_para', to='project_manage.Parameter'),
        ),
        migrations.AddField(
            model_name='bodypara',
            name='para',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_manage.Parameter'),
        ),
        migrations.AddField(
            model_name='api',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_manage.Module'),
        ),
        migrations.AddField(
            model_name='api',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_manage.Project'),
        ),
    ]
