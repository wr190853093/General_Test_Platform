from django.db import models
from project_manage.models import *


class Case(models.Model):
    name = models.CharField(max_length=30, null=False)
    status = models.SmallIntegerField(choices=((0, u'跳过'), (1, u'启用')), null=False, default=1)
    desc = models.CharField(max_length=30, null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name


class Step(models.Model):
    name = models.CharField(max_length=30, null=False)
    desc = models.CharField(max_length=30, null=False)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    api = models.ForeignKey(Api, on_delete=models.CASCADE)
    order = models.IntegerField(null=False, default=1)
    headers = models.TextField(null=True)
    body = models.TextField(null=True)
    check = models.TextField(null=True)
    is_del = models.SmallIntegerField(choices=((0, u'已删除'), (1, u'未删除')), null=False, default=1)

    # para_type = models.SmallIntegerField(
    #     choices=((10, 'herader para'), (21, 'body para urlencoded'), (22, 'body para json')), null=False)
    # key = models.CharField(max_length=20, null=False)
    # value = models.CharField(max_length=400, null=False)

    def __unicode__(self):
        return self.name


# class CheckPoint(models.Model):
#     step = models.ForeignKey(Step, on_delete=models.CASCADE)
#     type = models.SmallIntegerField(choices=((0, 'herader value'), (2, 'body value'),), null=False)
#     key = models.CharField(max_length=20, null=False)
#     value = models.CharField(max_length=400, null=False)


class Task(models.Model):
    name = models.CharField(max_length=30, null=False)
    desc = models.CharField(max_length=30, null=False)
    # environment = models.ForeignKey(Environment, on_delete=models.CASCADE)
    # case = models.ForeignKey(Case, on_delete=models.CASCADE)
    # step = models.ForeignKey(Step, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name


class TaskEnvironment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    step = models.ForeignKey(Step, on_delete=models.CASCADE)


class Report(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=100, null=False)
    status = models.IntegerField(choices=((0, '运行中'), (1, '结束')), null=True)
    # time = models.TimeField()
    time = models.FloatField(null=False, unique=True)

    def __unicode__(self):
        return self.file_name
