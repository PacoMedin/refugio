from django.urls import path
from apps.mascota.views import index_mascota, mascota_view

urlpatterns = [

    path('', index_mascota, name='index'),
    path('nuevo', mascota_view, name='mascota_crear'),
]
