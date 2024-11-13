from django.db import models

# Create your models here.
class Pedidos(models.Model):
    title = models.TextField(max_length=250)
    position = models.TextField(max_length=250, null=True)

    def __str__(self):
        return f"{self.title} - {self.position}" 

class Cliente(models.Model):
    folio = models.TextField(max_length=250)
    nombre = models.TextField(max_length=250)

    def __str__(self):
        return self.folio
    
class Hoja_de_Presupuesto(models.Model):
    folio_pres = models.TextField(max_length=250)
    presupuesto = models.TextField(max_length=250)
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.folio_pres
    