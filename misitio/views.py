import datetime

from django.shortcuts import render

from .forms import ClienteForm, ConciertoForm
from .models import Cliente, Concierto
from django.utils import timezone
from django.views.generic import CreateView
# Create your views here.


def conciertos_list(request):
    conciertos = Concierto.objects.order_by('fecha')
    return render(request, 'misitio/conciertos_list.html', {'conciertos': conciertos})

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
        form = ConciertoForm(request.POST)
        if form.is_valid():
            concierto = form.save()
            concierto.save()
    else:
        form = ConciertoForm()
    return render(request, 'misitio/concierto_new.html', {'form': form})

