from django.urls import path, include
from . import views
from users import views as userViews


urlpatterns = [
    path('', views.home, name='home'),
    path('reg/', userViews.register, name='reg'),
    path('contacts', views.contacts, name='contacts')
]