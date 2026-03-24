from django.shortcuts import render
from .models import Task

def task_list(request):
    # Veritabanından görevleri çekiyoruz
    tasks = Task.objects.all()
    # Şablon adını kesinlikle 'todo/task_list.html' yapıyoruz
    return render(request, 'todo/task_list.html', {'tasks': tasks})
