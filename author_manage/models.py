#coding:utf-8

from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=20, null=False)
    parent = models.IntegerField(null=True)
    is_del = models.SmallIntegerField(choices=((0, u'已删除'), (1, u'未删除')), null=True)

    def __unicode__(self):
        return self.name


class Users(models.Model):
    name = models.CharField(max_length=15)
    username = models.CharField(max_length=20, unique=True, null=False)
    email = models.EmailField()
    org = models.ForeignKey(Organization)
    role = models.SmallIntegerField(choices=((0, u'产品经理'), (1, u'开发'), (2, u'测试'),(3, u'运维')), null=False)
    status = models.SmallIntegerField(choices=((0, u'离职'), (1, u'在职')), null=False)
    is_del = models.SmallIntegerField(choices=((0, u'已删除'), (1, u'未删除')), null=True)
    password = models.CharField(max_length=128, null=False)

    def __unicode__(self):
        return self.name