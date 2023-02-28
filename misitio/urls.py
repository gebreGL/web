from django.urls import path
from . import views

urlpatterns = [
    path('', views.conciertos_list, name='conciertos_list'),
    path('concierto/new', views.conciertos_new, name='concierto_new'),
    path('info', views.sobre_nosotros, name='sobre_nosotros'),
    path('concierto/delete', views.conciertos_list_borrar, name='delete_conciertos'),
    path('delete/<str:pk>', views.delete_concierto, name='delete'),
]
