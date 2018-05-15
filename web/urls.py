#coding:utf-8

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^org/', 'web.views.org'),
    url(r'^users/', 'web.views.users'),
    url(r'^project/', 'web.views.project'),
    url(r'^module/', 'web.views.module'),
    url(r'^environment/', 'web.views.environment'),
    url(r'^api/', 'web.views.api'),
    url(r'^case/', 'web.views.case'),
    url(r'^task/', 'web.views.task'),
    url(r'^report/', 'web.views.report'),
    url(r'^mock/', 'web.views.mock'),

]
