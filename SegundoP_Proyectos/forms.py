from django import forms
from .models import Helado, Topping

class HeladoForm(forms.ModelForm):
    class Meta:
        model = Helado
        fields = ['tamaño', 'sabor_1', 'sabor_2', 'sabor_3', 'toppings']

class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['nombre', 'precio']

class FacturaForm(forms.Form):
    cliente = forms.CharField(max_length=100)
