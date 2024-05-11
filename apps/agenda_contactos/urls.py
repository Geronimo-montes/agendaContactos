from django.urls import path

from apps.agenda_contactos.views import ContactoListView
from apps.agenda_contactos.views import ContactoCreateView
from apps.agenda_contactos.views import ContactoUpdateView
from apps.agenda_contactos.views import ContactoDetailView
from apps.agenda_contactos.views import ContactoDeleteView


urlpatterns = [
    path("lista/", ContactoListView.as_view(), name="contacto_list"),
    path("create/", ContactoCreateView.as_view(), name="contacto_create"),
    path("<int:pk>/update/", ContactoUpdateView.as_view(), name="contacto_update"),
    path('<int:pk>/detail/', ContactoDetailView.as_view(), name="contacto_detail"),
    path('<int:pk>/delete/', ContactoDeleteView.as_view(), name="contacto_delete"),
]