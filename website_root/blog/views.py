from django.shortcuts import render
from .models import News, Masters
from django.views.generic import ListView

def home(request):
    data = {
        'masters': Masters.objects.all(),
        'title': 'MasterOk'
    }
    return render(request, 'blog/home.html', data)

def mastersList(request):
    data = {
        'masters': Masters.objects.all(),
        'title': 'MasterOk'
    }
    return render(request, 'blog/mastersList.html', data)

class ShowMasterView(ListView):
    model = Masters
    template_name = 'blog/mastersList.html'
    context_object_name = 'masters'
    ordering = ['id']
    
    def get_context_data(self, **kwargs):
        ctx = super(ShowMasterView, self).get_context_data(**kwargs)
        
        ctx['title'] = 'Главная страница сайта!'
        ctx['masters'] = 'Главная страница сайта!'
        return ctx

def masterList(request):
    data = {
        'masters': Masters.objects.all(),
        'title': 'MasterOk'
    }
    return render(request, 'blog/mastersList.html', {'title': Masters.master})
