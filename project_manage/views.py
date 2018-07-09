from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from project_manage.models import *
from rest_framework.decorators import api_view
import json


# Create your views here.

@api_view(['POST'])
def reat_project(request):
    pass


@api_view(['POST'])
def edit_project(request):
    pass


@api_view(['POST'])
def file_project(request):
    pass


@api_view(['GET'])
def project_list(request):
    pass


@api_view(['POST'])
def add_member(request):
    pass


@api_view(['POST'])
def delete_member(request):
    pass


@api_view(['POST'])
def creat_module(request):
    pass


@api_view(['POST'])
def edit_module(request):
    pass


@api_view(['POST'])
def delete_module(request):
    pass


@api_view(['GET'])
def module_tree(request):
    pass


@api_view(['POST'])
def creat_environment(request):
    pass


@api_view(['POST'])
def delete_environment(request):
    pass


@api_view(['POST'])
def edit_environment(request):
    pass


@api_view(['POST'])
def enable_evironment(request):
    pass


@api_view(['POST'])
def unenable_evironment(request):
    pass


@api_view(['GET'])
def evironment_list(request):
    pass
