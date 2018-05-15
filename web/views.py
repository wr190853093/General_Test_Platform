from django.shortcuts import render

# Create your views here.


def org(request):
    return render(request, 'users.html')


def users(request):
    return render(request, 'users.html')


def project(request):
    return render(request, 'project.html')


def module(request):
    return render(request, 'module.html')


def environment(request):
    return render(request, 'environment.html')


def api(request):
    return render(request, 'api.html')


def case(request):
    return render(request, 'case.html')


def task(request):
    return render(request, 'task.html')


def report(request):
    return render(request, 'report.html')


def mock(request):
    return render(request, 'mock.html')
