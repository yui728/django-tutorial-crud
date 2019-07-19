from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Message
from .forms import MessageForm

def index(request):
    d = {
        'messages': Message.objects.all(),
    }
    return render(request, 'crud/index.html', d)

def add(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        Message.objects.create(**form.cleaned_data)
        return redirect('crud:index')
    
    d = {
        'form': form,
    }
    return render(request, 'crud/edit.html',d)

def edit(request, editting_id):
    return render(request, 'crud/edit.html', {})

def delete(request):
    return HttpResponse('Delete')