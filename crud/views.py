from django.shortcuts import ( 
    render, 
    redirect,
    get_object_or_404
     )
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
    message = get_object_or_404(Message, id=editting_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message.message = form.cleaned_data['message']
            message.save()
            return redirect('crud:index')
    else:
        # GETリクエスト時はDBに保存されているデータを表示する
        form = MessageForm({'message': message.message})

    d = {
        'form': form,
    }
    return render(request, 'crud/edit.html', d)

def delete(request):
    return HttpResponse('Delete')