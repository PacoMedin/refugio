from django.urls import path
from apps.mascota.views import index_mascota, mascota_view, mascota_list,\
    mascota_edit,mascota_delete, MascotaList,MascotaCreate,MacotaUpdate,MacotaDelete


urlpatterns = [

    path('', index_mascota, name='index'),
    path('nuevo', MascotaCreate.as_view(), name ='mascota_crear'),
    path('listar', MascotaList.as_view(), name = 'mascota_listar'),
    #Expresion regular id de la mascota >   (?P<id_mascota>[0-9]+)/$
    path('editar/<int:pk>/', MacotaUpdate.as_view(), name = 'mascota_editar'),
    path('eliminar/<int:pk>/', MacotaDelete.as_view(), name = 'mascota_eliminar'),
]
