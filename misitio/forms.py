from django import forms
from .models import Cliente, Concierto


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [ 'dni', 'nombre', 'fechaAlta', 'direccion', 'movil']

        # también se podría hacer  --> ya que queremos todos los campos
        # class Meta:
        #   model = Canciones
        #   fields = '__all__'

class ConciertoForm(forms.ModelForm):
    class Meta:
        model = Concierto
        fields = [ 'nombre', 'fecha', 'lugar', 'precio', 'imagen']