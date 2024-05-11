from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Contacto(models.Model):

    user = models.ForeignKey(User, null=False, on_delete=models.RESTRICT)
    subfijo = models.CharField(max_length=100, blank=False, null=True )
    apodo = models.CharField(max_length=100, blank=False, null=True )
    nombre = models.CharField(max_length=100, blank=False, null=False )
    apellido = models.CharField(max_length=100, blank=False, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=False, null=False)
    telefono_trabajo = models.CharField(max_length=10, blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    direccion_trabajo = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.nombre 

    def get_absolute_url(self):
        return reverse("contacto_detail", kwargs={"pk": self.pk})
