
from django.db import models
from project_manage.models import *


class Mock(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    api = models.ForeignKey(Api, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    header_key = models.CharField(max_length=20, null=False)
    header_value = models.CharField(max_length=400, null=False)
    body_content_type = models.SmallIntegerField(choices=((0, 'x-www-form-urlencoded'), (1, 'json'),), null=False)
    body_key = models.CharField(max_length=20, null=False)
    body_value = models.CharField(max_length=400, null=False)
    response_value = models.CharField(max_length=400, null=False)
