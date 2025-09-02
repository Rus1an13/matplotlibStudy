from django.shortcuts import render
from .models import News

def home(request):
    data = {
        'news': News.objects.all(),
        'title': 'Main page'
    }
    return render(request, 'blog/home.html', data)

def contacts(request):
    return render(request, 'blog/contacts.html', {'title': 'Contacts page!'})
