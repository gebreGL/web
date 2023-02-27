import datetime
import os

from django.shortcuts import render, redirect, get_object_or_404

from .forms import ClienteForm, ConciertoForm
from .models import Cliente, Concierto
# Create your views here.


def conciertos_list(request):
    conciertos = Concierto.objects.order_by('fecha')
    return render(request, 'misitio/conciertos_list.html', {'conciertos': conciertos})

def conciertos_list_borrar(request):
    conciertos = Concierto.objects.order_by('fecha')
    return render(request, 'misitio/delete_conciertos.html', {'conciertos': conciertos})

'''def clientes_new(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            cliente.save()
    else:
        form = ClienteForm()
    return render(request, 'misitio/concierto_new.html', {'form': form})'''

def conciertos_new(request):
    if request.method == 'POST':
        form = ConciertoForm(request.POST, request.FILES)
        if form.is_valid():
            concierto = form.save()
            concierto.save()
            return redirect('/')
    else:
        form = ConciertoForm()
    return render(request, 'misitio/concierto_new.html', {'form': form})

def sobre_nosotros(request):
    return render(request, 'misitio/conciertos_list.html')

def delete_concierto(request, pk):
    concierto = get_object_or_404(Concierto, nombre=pk)
    os.remove(concierto.imagen.path)
    concierto.delete()
    return redirect('delete_conciertos')

