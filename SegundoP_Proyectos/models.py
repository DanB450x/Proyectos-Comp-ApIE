from django.db import models

class Helado(models.Model):
    SABORES = (
        ('CH', 'Chocolate'),
        ('VA', 'Vainilla'),
        ('FR', 'Fresa'),
        ('LI', 'Limón'),
        ('MA', 'Mango'),
        ('CO', 'Coco'),
    )

    tamaño = models.CharField(max_length=10)
    sabor_1 = models.CharField(max_length=2, choices=SABORES)
    sabor_2 = models.CharField(max_length=2, choices=SABORES, blank=True)
    sabor_3 = models.CharField(max_length=2, choices=SABORES, blank=True)
    toppings = models.ManyToManyField('Topping')

class Topping(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

class Factura(models.Model):
    helado = models.ForeignKey(Helado, on_delete=models.CASCADE)
    cliente = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=6, decimal_places=2)
