from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    template = 'todo/index.html'
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':

        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'tasks': tasks,
        'task_form': TaskForm,
    }
    return render(request, template_name=template, context=context)


def update(request, pk):
    template = 'todo/update.html'
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'task': task,
        'task_form': form,
    }
    return render(request, template_name=template, context=context)


def delete(request, pk):
    template = 'todo/delete.html'

    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        if 'delete_task' in request.POST:
            task.delete()
            return redirect('/')

        if 'cancel_task' in request.POST:
            return redirect('/')
    context = {
        'task': task,
    }

    return render(request, template_name=template, context=context)
