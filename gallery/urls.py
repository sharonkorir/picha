from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.show_all_images,name = 'photos'),
    path(r'search/', views.search_results, name='search_results'),
    path('location/<str:location>/', views.filter_images, name='filter_images')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)