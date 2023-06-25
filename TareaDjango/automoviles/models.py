from django.db import models

# Create your models here.
class Automovil(models.Model):
    """
    Modelo que representa un automovil
    """
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    numero_puertas = models.IntegerField()
    numero_asientos = models.IntegerField()
    trasmision =  models.CharField(max_length=20)
    color = models.CharField(max_length=20)

    def __str__(self):
        return """Marca: %s \n Modelo: %s - Numero de puertas: %d \n
                Numero de asientos: %d - Trasmision: %s \n Color: %s
                """ % (self.marca,self.modelo, self.numero_puertas, self.numero_asientos, self.trasmision, self.color)