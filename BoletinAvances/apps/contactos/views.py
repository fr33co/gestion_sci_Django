import hashlib
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, DeleteView, UpdateView
from django.views.generic.edit import UpdateView
from django.contrib import messages

from BoletinAvances.apps.contactos.models import Contactos
from BoletinAvances.apps.contactos.forms import ContactosForm

import os
from django.conf import settings
from django.shortcuts import render, redirect, render_to_response
import csv
import codecs
from django.contrib.auth.decorators import login_required


#CREAR MANUAL    
class ContactosManualAddView(FormView):
    form_class = ContactosForm
    success_url = reverse_lazy('contactos')
    template_name = "contactos/addContactos.html"

    def form_valid(self, form):
        form.save(commit=True)
        messages.success(self.request, 'Contacto cargado!', fail_silently=True)
        return super(ContactosManualAddView, self).form_valid(form) 


#CREAR MASIVO
@login_required(login_url='/') 
def upload_data_contactos(request):
    if request.POST and request.FILES:
        csvfile = request.FILES['file']
        dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
        csvfile.open()
        reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)
        for row in reader:
            if row[0] != 'nombre_contacto': # Ignore the header row, import everything else
                contactos = Contactos()
                contactos.nombre_contacto = row[0]
                contactos.institucion = row[1]
                contactos.telefono = row[2]
                contactos.correo = row[3]
                contactos.save()
                contactos.listas = row[4]
        return redirect('contactos')
 
    return render(request, "contactos/addContactosmasivos.html", locals())


#LISTAS
class ContactosListView(ListView):
    model = ContactosForm
    queryset = Contactos.objects.order_by('id')
    context_object_name = "Contactos"
    template_name = "contactos/contactos.html"
    

#VER INDIVIDUAL
class ContactosDetailView(DetailView):
    model = Contactos
    slug_field = 'id'
    template_name="contactos/singleContactos.html"

    def get_context_data(self, **kwargs):
        context = super(ContactosDetailView, self).get_context_data(**kwargs)
        return context


#ELIMINAR
class ContactosDeleteView(DeleteView):
    model = Contactos
    slug_field = 'id'
    success_url = '/administracion/contactos'


#ACTUALIZAR
class ContactosUpdate(UpdateView):
    model = Contactos
    fields = ['nombre_contacto', 'institucion', 'telefono', 'correo', 'listas']
    slug_field = 'id'
    template_name_suffix = '_update_form'
    success_url = '/administracion/contactos'