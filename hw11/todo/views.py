from django.shortcuts import render
from .models import TodoItem #

def index(request): 
    
    todos = TodoItem.objects.all() 
    
    return render(request, 'todo/index.html', {'todos': todos})