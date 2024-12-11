from django.shortcuts import render
from .models import Todo

# Create your views here.
def create_todo(request):
    if request.method == 'POST':
        task = request.POST['task']
        Todo.objects.create(task=task)