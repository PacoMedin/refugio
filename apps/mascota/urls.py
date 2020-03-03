from django.urls import path
from apps.mascota.views import index_mascota, mascota_view, mascota_list

urlpatterns = [

    path('', index_mascota, name='index'),
    path('nuevo', mascota_view, name='mascota_crear'),
    path('listar', mascota_list, name = 'mascota_listar')
]
