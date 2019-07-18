from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'crud/index.html', {})

def add(request):
    return render(request, 'crud/edit.html', {})

def edit(request, editting_id):
    return render(request, 'crud/edit.html', {})

def delete(request):
    return HttpResponse('Delete')