from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    template = 'main/index.html'
    return render(request, template)

def about(request):
    title = 'Add task'
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
        'title': title,
    }
    template = 'main/tasks.html'
    return render(request, template, context)

def add_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:tasks')
        else:
            error = 'Форма неверна'

    form = TaskForm()
    context = {
        'form': form,
        'error': error,
    }
    template = 'main/add_task.html'
    return render(request, template, context)