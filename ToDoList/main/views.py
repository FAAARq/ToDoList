from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Tasks
import datetime
import json

# Create your views here.
def index(request):
    data_today = datetime.date.today()
    tasks = Tasks.objects.all()
    return render(request, 'main/index.html', {'date': data_today, 'tasks': tasks})

def create(request):
    if request.method == "POST":
        task_text = request.POST.get('task_text')
        if task_text:
            Tasks.objects.create(title=task_text, date=datetime.date.today())

    return redirect('home')


def delete_task(request, pk):
    task = Tasks.objects.get(pk=pk)
    task.delete()
    return redirect('home')

def set_task_color(request, pk):
    data = json.loads(request.body)
    color = data['color', '']

    task = Tasks.objects.get(pk=pk)
    task.color = color
    task.save()
    return JsonResponse({'status': 'ok'})

