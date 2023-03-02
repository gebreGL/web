from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.conciertos_list, name='conciertos_list'),
    path('concierto/new', views.conciertos_new, name='concierto_new'),
    path('info', views.sobre_nosotros, name='sobre_nosotros'),
    path('concierto/delete', views.conciertos_list_borrar, name='delete_conciertos'),
    path('delete/<str:pk>', views.delete_concierto, name='delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout, name="logout"),
    path('su/opciones', views.opciones_admin, name='opciones_admin'),
]
