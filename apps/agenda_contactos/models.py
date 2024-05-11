from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Contacto(models.Model):

    user = models.ForeignKey(User, null=False, on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=100, blank=False, null=False )
    telefono = models.CharField(max_length=10, blank=False, null=False  )

    def __str__(self):
        return self.nombre 

    def get_absolute_url(self):
        return reverse("contacto_detail", kwargs={"pk": self.pk})
