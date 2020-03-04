from django.urls import path
from apps.mascota.views import index_mascota, mascota_view, mascota_list, mascota_edit,mascota_delete

urlpatterns = [

    path('', index_mascota, name='index'),
    path('nuevo', mascota_view, name ='mascota_crear'),
    path('listar', mascota_list, name = 'mascota_listar'),
    #Expresion regular id de la mascota >   (?P<id_mascota>[0-9]+)/$
    path('editar/<int:id_mascota>/', mascota_edit, name = 'mascota_editar'),
    path('eliminar/<int:id_mascota>/', mascota_delete, name = 'mascota_eliminar'),
]
