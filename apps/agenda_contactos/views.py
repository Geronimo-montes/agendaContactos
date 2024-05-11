from typing import Any
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from django.contrib.auth.decorators import login_required
from apps.agenda_contactos.models import Contacto



# Create your views here.
class LoginRequiredMixin(object):
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())


class ContactoListView(ListView, LoginRequiredMixin):
    model = Contacto
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headers"] = [ "Nombre", "Telefono", "Acciones"]
        context["contactos"] = Contacto.objects.filter(user=self.request.user)
        return context
    

class ContactoDetailView(DetailView, LoginRequiredMixin):
    model = Contacto

    
class ContactoCreateView(CreateView, LoginRequiredMixin):
    model = Contacto
    fields = ["nombre", "telefono"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        print(form.as_p)
        return super().form_valid(form)


class ContactoUpdateView(UpdateView, LoginRequiredMixin):
    model = Contacto
    success_url = "/agenda/lista/"
    fields = ["nombre", "telefono"]
    
    
class ContactoDeleteView(DeleteView, LoginRequiredMixin):
    model = Contacto
    success_url ="/agenda/lista/"
    fields = ["nombre", "telefono"]





