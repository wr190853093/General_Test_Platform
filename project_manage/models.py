# coding:utf-8

from django.db import models
from author_manage.models import *
from mptt.models import MPTTModel


class Project(models.Model):
    name = models.CharField(max_length=30, null=False)
    status = models.SmallIntegerField(choices=((0, u'归档'), (1, u'正常')), null=False, default=1)
    team = models.ManyToManyField(Users)

    def __str__(self):
        return self.name


class Module(MPTTModel):
    name = models.CharField(max_length=30, null=False)
    parent = TreeForeignKey("self", blank=True, null=True, related_name="children", on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    is_del = models.SmallIntegerField(choices=((0, u'已删除'), (1, u'未删除')), null=False, default=1)

    def __str__(self):
        return self.name


class Environment(models.Model):
    name = models.CharField(max_length=30, null=False)
    host = models.CharField(max_length=20, null=False)
    status = models.SmallIntegerField(choices=((0, u'禁用'), (1, u'启用')), null=False, default=1)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    is_del = models.SmallIntegerField(choices=((0, u'已删除'), (1, u'未删除')), null=False, default=1)
    type = models.SmallIntegerField(choices=((0, u'开发环境'), (1, u'测试环境'), (2, u'准生产环境'), (3, u'生产环境')), null=False)

    def __str__(self):
        return self.name


class Api(models.Model):
    name = models.CharField(max_length=30, null=False)
    host = models.CharField(max_length=20, null=False)
    method = models.SmallIntegerField(choices=((0, 'GET'), (1, 'POST')), null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    is_del = models.SmallIntegerField(choices=((0, u'已删除'), (1, u'未删除')), null=False, default=1)

    def __str__(self):
        return self.name


class Parameter(models.Model):
    key = models.CharField(max_length=20, null=False)
    desc = models.CharField(max_length=30, null=False)
    is_null = models.SmallIntegerField(choices=((0, u'不可为空'), (1, u'可为空')), null=True)
    is_del = models.SmallIntegerField(choices=((0, u'已删除'), (1, u'未删除')), null=False, default=1)
    data_type = models.SmallIntegerField(
        choices=((0, 'string'), (1, 'number'), (2, 'object'), (3, 'boolean'), (4, 'array'),), null=False)

    def __str__(self):
        return self.key


class HeaderPara(models.Model):
    api = models.ForeignKey(Api, on_delete=models.CASCADE)
    para = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    is_del = models.SmallIntegerField(choices=((0, u'已删除'), (1, u'未删除')), null=False, default=1)


class BodyPara(models.Model):
    api = models.ForeignKey(Api, on_delete=models.CASCADE)
    para = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    content_type = models.SmallIntegerField(choices=((0, 'x-www-form-urlencoded'), (1, 'json'),), null=False)
    is_del = models.SmallIntegerField(choices=((0, u'已删除'), (1, u'未删除')), null=False, default=1)


class ResponsePara(models.Model):
    api = models.ForeignKey(Api, on_delete=models.CASCADE)
    para = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    is_del = models.SmallIntegerField(choices=((0, u'已删除'), (1, u'未删除')), null=False, default=1)


class ComplexPara(models.Model):
    parent_para = models.ForeignKey(Parameter, related_name='parent_para', on_delete=models.CASCADE)
    chirld_para = models.ForeignKey(Parameter, related_name='chirld_para', on_delete=models.CASCADE)
    is_del = models.SmallIntegerField(choices=((0, u'已删除'), (1, u'未删除')), null=False, default=1)
