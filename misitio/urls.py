from django.urls import path
from . import views

urlpatterns = [
    path('', views.conciertos_list, name='conciertos_list'),
    path('concierto/new', views.conciertos_new, name='concierto_new'),
]
