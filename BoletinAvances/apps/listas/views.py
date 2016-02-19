import hashlib
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, FormView, UpdateView, DetailView, DeleteView
from django.contrib import messages

from BoletinAvances.apps.listas.models import Listas
from BoletinAvances.apps.listas.forms import ListasForm
from BoletinAvances.apps.contactos.models import Contactos
from BoletinAvances.apps.contactos.forms import ContactosForm
from BoletinAvances.apps.boletines.models import Boletines
from BoletinAvances.apps.boletines.forms import BoletinesForm

import os
from django.conf import settings
from django.shortcuts import render, redirect
import csv
import codecs
from django.contrib.auth.decorators import login_required


#CREAR MANUAL
class ListasManualAddView(FormView):
    form_class = ListasForm
    success_url = reverse_lazy('listas')
    template_name = "listas/addListas.html"

    def form_valid(self, form):
        form.save(commit=True)
        messages.success(self.request, 'Lista cargada!', fail_silently=True)
        return super(ListasManualAddView, self).form_valid(form)
    
    
#CREAR MASIVAS 
@login_required(login_url='/') 
def upload_data_list(request):
    if request.POST and request.FILES:
        print request
        csvfile = request.FILES['file']
        dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
        csvfile.open()
        reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)
        for row in reader:
            if row[0] != 'tipo_lista': # Ignore the header row, import everything else
                listas = Listas()
                listas.tipo_lista = row[0]
                listas.nombre_lista = row[1]
                listas.descripcion_lista = row[2]
                listas.save()
                return redirect('/administracion/listas')
 
    return render(request, "listas/addListasmasivos.html", locals())


#LISTAS
class ListasListView(ListView):
    model = ListasForm
    queryset = Listas.objects.order_by('id')
    context_object_name = "Listas"
    template_name = "listas/listas.html"


#VER INDIVIDUAL
class ListasDetailView(DetailView):
    model = Listas
    slug_field = 'id'
    template_name="listas/singleListas.html"

    def get_context_data(self, **kwargs):
        context = super(ListasDetailView, self).get_context_data(**kwargs)
        return context


#ELIMINAR
class ListaDeleteView(DeleteView):
    model = Listas
    slug_field = 'id'
    success_url = '/administracion/listas'


#ACTUALIZAR
class ListasUpdate(UpdateView):
    model = Listas
    fields = ['tipo_lista', 'nombre_lista', 'descripcion_lista']
    slug_field = 'id'
    template_name_suffix = '_update_form'
    success_url = '/administracion/listas'