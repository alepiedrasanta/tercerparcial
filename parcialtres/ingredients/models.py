from django.db import models
 
class Category(models.Model):
    marca = models.CharField(max_length=200)
    detalles = models.CharField(max_length=500)
    precio = models.CharField(max_length=500)
 
    def __str__(self):
        return self.name
