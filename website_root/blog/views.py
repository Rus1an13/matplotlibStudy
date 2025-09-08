from django.shortcuts import render
from .models import News, Masters

def home(request):
    data = {
        'masters': Masters.objects.all(),
        'title': 'MasterOk'
    }
    return render(request, 'blog/home.html', data)

def contacts(request):
    return render(request, 'blog/contacts.html', {'title': 'Contacts page!'})
