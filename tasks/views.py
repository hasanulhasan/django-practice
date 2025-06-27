from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("WELCOME to the task management system")

def contact(request):
    return HttpResponse("<h1 style='color: red'>This is contact page</h1>")

def show_task(request):
    return HttpResponse("<h1 style='color: red'>This is a task</h1>")

def show_specific_task(request, id):
    print(id)
    return HttpResponse(f'This is a task {id}')