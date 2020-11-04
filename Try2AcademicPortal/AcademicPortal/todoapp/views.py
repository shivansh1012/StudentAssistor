from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


# Create your views here.
@login_required(login_url='login')
def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('todoapp:list')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todolist/list.html', context)

@login_required(login_url='login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todoapp:list')

    context = {'form': form}

    return render(request, 'todolist/update_task.html', context)

@login_required(login_url='login')
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('todoapp:list')

    context = {'item': item}
    return render(request, 'todolist/delete.html', context)
