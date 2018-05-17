#coding:utf-8

from django.db import models
from author_manage.models import *

class Project(models.Model):
    name = models.CharField(max_length=30, null=False)
    status = models.SmallIntegerField(choices=((0, u'禁用'), (1, u'启用')), null=False)
    team = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=30, null=False)
    parent = models.IntegerField(null=True)
    project = models.ForeignKey(Project)
    is_del = models.SmallIntegerField(choices=((0, u'已删除'), (1, u'未删除')), null=True)

    def __unicode__(self):
        return self.name


class Environment(models.Model):
    name = models.CharField(max_length=30, null=False)
    host = models.CharField(max_length=20, null=False)
    status = models.SmallIntegerField(choices=((0, u'禁用'), (1, u'启用')), null=False)
    project = models.ForeignKey(Project)
    is_del = models.SmallIntegerField(choices=((0, u'已删除'), (1, u'未删除')), null=True)
    type = models.SmallIntegerField(choices=((0, u'开发环境'), (1, u'测试环境'), (2, u'准生产环境'),(3, u'生产环境')), null=False)

    def __unicode__(self):
        return self.name


class Api(models.Model):
    name = models.CharField(max_length=30, null=False)
    host = models.CharField(max_length=20, null=False)
    method = models.SmallIntegerField(choices=((0, 'GET'), (1, 'POST')), null=False)
    project = models.ForeignKey(Project)
    module = models.ForeignKey(Module)
    is_del = models.SmallIntegerField(choices=((0, u'已删除'), (1, u'未删除')), null=True)

    def __unicode__(self):
        return self.name


class Parameter(models.Model):
    key = models.CharField(max_length=20, null=False)
    desc = models.CharField(max_length=30, null=False)
    is_null = models.SmallIntegerField(choices=((0, u'不可为空'), (1, u'可为空')), null=True)
    is_del = models.SmallIntegerField(choices=((0, u'已删除'), (1, u'未删除')), null=True)
    data_type = models.SmallIntegerField(choices=((0, 'string'), (1, 'number'), (2, 'object'), (3, 'boolean'), (4, 'array'),), null=False)

    def __unicode__(self):
        return self.key


class HeaderPara(models.Model):
    api = models.ForeignKey(Api)
    para = models.ForeignKey(Parameter)
    is_del = models.SmallIntegerField(choices=((0, u'已删除'), (1, u'未删除')), null=True)


class BodyPara(models.Model):
    api = models.ForeignKey(Api)
    para = models.ForeignKey(Parameter)
    content_type = models.SmallIntegerField(choices=((0, 'x-www-form-urlencoded'), (1, 'json'),), null=False)
    is_del = models.SmallIntegerField(choices=((0, u'已删除'), (1, u'未删除')), null=True)


class ResponsePara(models.Model):
    api = models.ForeignKey(Api)
    para = models.ForeignKey(Parameter)
    is_del = models.SmallIntegerField(choices=((0, u'已删除'), (1, u'未删除')), null=True)


class ComplexPara(models.Model):
    parent_para = models.ForeignKey(Parameter)
    chirld_para = models.ForeignKey(Parameter)
    is_del = models.SmallIntegerField(choices=((0, u'已删除'), (1, u'未删除')), null=True)
