from django.shortcuts import render
from django.http import HttpResponse
from .models import Helado, Topping, Factura

def index(request):
    # Obtener todos los helados de la base de datos
    helados = Helado.objects.all()

    # Obtener todos los toppings de la base de datos
    toppings = Topping.objects.all()

    # Si se recibió un POST
    if request.method == 'POST':
        # Obtener los datos del formulario
        tamaño = request.POST.get('tamaño')
        sabor_1 = request.POST.get('sabor_1')
        sabor_2 = request.POST.get('sabor_2')
        sabor_3 = request.POST.get('sabor_3')
        toppings_ids = request.POST.getlist('toppings')

        # Calcular el precio del helado
        helado = Helado.objects.get(tamaño=tamaño, sabor_1=sabor_1, sabor_2=sabor_2, sabor_3=sabor_3)
        precio_helado = helado.get_precio()

        # Calcular el precio de los toppings
        precio_toppings = 0
        for topping_id in toppings_ids:
            topping = Topping.objects.get(id=topping_id)
            precio_toppings += topping.precio

        # Calcular el total de la factura
        total = precio_helado + precio_toppings

        # Crear la nueva factura en la base de datos
        factura = Factura(helado=helado, cliente='Nuevo cliente', total=total)
        factura.save()

        # Redirigir al usuario a la página de la factura
        return HttpResponse(f'<h1>Total de la factura: Q{total:.2f}</h1>')

    # Si se recibió un GET
    else:
        # Renderizar el template con los datos de los helados y toppings
        context = {
            'helados': helados,
            'toppings': toppings,
        }
        return render(request, 'heladeria/index.html', context)
