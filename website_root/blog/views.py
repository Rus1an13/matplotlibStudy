from django.shortcuts import render
from .models import News, Masters
from django.views.generic import ListView, DetailView, CreateView

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
    
    def get_context_data(self, **kwards):
        ctx = super(ShowMasterView, self).get_context_data(**kwards)
        
        ctx['title'] = 'Главная страница сайта!'
        # ctx['masters'] = 'Главная страница сайта!'
        return ctx

class MasterDetailView(DetailView):
    model = Masters

    def get_context_data(self, **kwards):
        ctx = super(MasterDetailView, self).get_conetext_data(**kwards)
        
        ctx['master'] = Masters.objects.get(pr=self.kwargs['pk'])
        return ctx
        
        return super().get_context_data(**kwards)

class CreateMastersView(CreateView):
    model = Masters
    template_name = 'blog/create_master.html'
    
    fields = ['master', 'img']

def masterList(request):
    data = {
        'masters': Masters.objects.all(),
        'title': 'MasterOk'
    }
    return render(request, 'blog/mastersList.html', {'title': Masters.master})
