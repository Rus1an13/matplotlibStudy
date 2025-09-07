from django.contrib import admin
from django.urls import path, include
from users import views as userViews
from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', userViews.register, name='reg'),
    path('user/', authViews.LoginView.as_view(), name='user'),
    path('exit/', authViews.LogoutView.as_view(), name='exit'),
    path('', include('blog.urls')),
]