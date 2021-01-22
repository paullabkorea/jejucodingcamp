from django.contrib import admin
from django.urls import path
from main.views import index, about, write, cafelist, cafedetails
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('write/', write, name='write'),
    path('cafelist/', cafelist, name='cafelist'),
    path('cafelist/<int:pk>/', cafedetails, name='cafedetails'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
