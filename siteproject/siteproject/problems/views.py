from http.client import HTTPResponse

from django.shortcuts import render, redirect

from .forms import AddProjectForm
from .models import *
projects = Projects.objects.all()
i = 0
p = Projects.objects.get(id = 1)
menu = ["Главная", "Проекты", "Информация", "Проблемы", "ДОБАВИТЬ ПРОБЛЕМУ", "ДОБАВИТЬ ПРОЕКТ", "Авторизация"]
def index(request):
    return render(request,'problems/index.html', {'projects': projects,'menu': menu, 'title': 'Проекты'})

def main(request):
    return  render(request,'problems/base.html', {'menu': menu, 'title': 'Проектная площадка ММФ НГУ'})

def project(request):
    return render(request, 'problems/project.html', {'menu': menu, 'title': p.title, 'field': p, "i": i})

def addpage(request):
    if request.method == 'POST':
        form = AddProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('add_page')
        else:
            print('')
    elif request.method == 'GET':
        form = AddProjectForm()
    else:
        print('')
    return render(request, 'problems/addForm.html', {'form': form})
"""
title = ""
problem = ""
analysis = ""
shortdescription = ""
description = ""
user = Users.objects.get(id = 4)
def add_to_base():
    test_project = Projects.objects.create(title = title, problem = problem, analysis = analysis,
                                           shortdescription = shortdescription, description = description)
    test_project.project.add(user)
    return
    """