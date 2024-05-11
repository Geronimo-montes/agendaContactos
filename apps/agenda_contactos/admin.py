from django.contrib import admin

from apps.agenda_contactos.models import Contacto

# Register your models here.
class ContactoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contacto, ContactoAdmin)