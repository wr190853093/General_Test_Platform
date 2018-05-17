#coding:utf-8

from django.db import models
from project_manage.models import *


class Case(models.Model):
    name = models.CharField(max_length=30, null=False)
    status = models.SmallIntegerField(choices=((0, u'跳过'), (1, u'启用')), null=False)
    desc = models.CharField(max_length=30, null=False)
    project = models.Model(Project)

    def __unicode__(self):
        return self.name


class Step(models.Model):
    name = models.CharField(max_length=30, null=False)
    desc = models.CharField(max_length=30, null=False)
    case = models.Model(Case)
    api = models.Model(Api)
    order = models.IntegerField(null=False, default=1)
    para = models.ForeignKey(Parameter)
    para_type = models.SmallIntegerField(choices=((10, 'herader para'), (21, 'body para urlencoded'), (22, 'body para json')), null=False)
    key = models.CharField(max_length=20, null=False)
    value = models.CharField(max_length=400, null=False)

    def __unicode__(self):
        return self.name


class CheckPoint(models.Model):
    step = models.ForeignKey(Step)
    type = models.SmallIntegerField(choices=((0, 'herader value'), (2, 'body value'),), null=False)
    key = models.CharField(max_length=20, null=False)
    value = models.CharField(max_length=400, null=False)


class Task(models.Model):
    name = models.CharField(max_length=30, null=False)
    desc = models.CharField(max_length=30, null=False)
    environment = models.ForeignKey(Environment)
    case = models.ManyToManyField(Case)

    def __unicode__(self):
        return self.name


class Report(models.Model):
    task = models.ManyToManyField(Task)
    file_name = models.CharField(max_length=30, null=False)

    def __unicode__(self):
        return self.file_name

