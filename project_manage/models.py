#coding:utf-8

from django.db import models
from author_manage.models import *

class Project(models.Model):
    name = models.CharField(max_length=30, null=False)
    status = models.SmallIntegerField(choices=((0, u'禁用'), (1, u'启用')), null=False)
    team = models.ManyToManyField(User)


class Module(models.Model):
    name = models.CharField(max_length=30, null=False)
    parent = models.IntegerField(null=True)
    project = models.ForeignKey(Project)
    is_del = models.SmallIntegerField(choices=((0, u'已删除'), (1, u'未删除')), null=True)


class Environment(models.Model):
    name = models.CharField(max_length=30, null=False)
    host = models.CharField(max_length=20, null=False)
    status = models.SmallIntegerField(choices=((0, u'禁用'), (1, u'启用')), null=False)
    project = models.ForeignKey(Project)
    is_del = models.SmallIntegerField(choices=((0, u'已删除'), (1, u'未删除')), null=True)
    type = models.SmallIntegerField(choices=((0, u'开发环境'), (1, u'测试环境'), (2, u'准生产环境'),(3, u'生产环境')), null=False)


class Api(models.Model):
    pass

