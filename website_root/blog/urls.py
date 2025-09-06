from django.urls import path, include
from . import views
from users import views as userViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('reg/', userViews.register, name='reg'),
    path('contacts', views.contacts, name='contacts')
]

# подключение статических файло в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)