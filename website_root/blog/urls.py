from django.urls import path, include
from . import views
from users import views as userViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('reg/', userViews.register, name='reg'),
    path('mastersList/<slug>', views.MasterDetailView.as_view(), name='mastersList'),
    # path('mastersList/<int:pr>', views.MasterDetailView.as_view(), name='masterList-n'),
    # path('masters/add', views.CreateMastersView.as_view(), name='masters-add'),
]

# подключение статических файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)