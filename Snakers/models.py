from django.db import models
import datetime

class Zapatillas(models.Model):
    nombre = models.CharField( max_length=200 )
    url = models.CharField( max_length=200 )
    img = models.CharField( max_length=200 )
    reintentos = models.IntegerField()

class Zapatilla_Talle(models.Model):
    zapatilla_talle = models.ForeignKey( Zapatillas, on_delete=models.CASCADE, related_name='talles' )
    talle = models.FloatField()

class Zapatilla_Precio(models.Model):
    zapatilla_precio = models.ForeignKey( Zapatillas, on_delete=models.CASCADE, related_name='precios' )
    precio = models.FloatField()
    fecha = models.DateTimeField( default=datetime.datetime.now() )
