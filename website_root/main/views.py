# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("New list of advertising will be shown here!")

from django.shortcuts import render

def main(request):
    data = {
        
    }
    return render(request, 'main/main.html', data)