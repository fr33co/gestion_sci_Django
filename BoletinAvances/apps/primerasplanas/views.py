import hashlib
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, DeleteView
from django.contrib import messages

from BoletinAvances.apps.listas.models import Listas
from BoletinAvances.apps.listas.forms import ListasForm
from BoletinAvances.apps.contactos.models import Contactos
from BoletinAvances.apps.contactos.forms import ContactosForm
from BoletinAvances.apps.primerasplanas.models import PrimerasPlanas, Archivos
from BoletinAvances.apps.primerasplanas.forms import PrimerasPlanasForm, ArchivosForm, ArchivosFormSet

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import EmailMessage, send_mail
import os
from django.conf import settings
from django.shortcuts import get_object_or_404, render


#LISTAS
class PrimerasPlanasListView(ListView):
    model = PrimerasPlanas
    queryset = PrimerasPlanas.objects.order_by('id')
    context_object_name = "PrimerasPlanas"
    template_name = "primerasplanas/listaPrimerasPlanas.html"
    
    
#CREAR
class PrimerPlanaAddView(FormView):
    model = PrimerasPlanas
    form_class = PrimerasPlanasForm
    formset = ArchivosFormSet()
    success_url = reverse_lazy('ver_primerasplanas')
    template_name = "primerasplanas/enviarPrimeraPlana.html"
    
    
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = ArchivosFormSet(instance=PrimerasPlanas())
        return self.render_to_response(
            self.get_context_data(form=form,
                                  formset=formset))


    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        primeraplana = form.save()
        formset = ArchivosFormSet(request.POST, request.FILES, instance=primeraplana)
        if (form.is_valid() and formset.is_valid()):
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)


    def form_valid(self, form, formset):
        """
        Called if all forms are valid. Creates a Primeras planas instance along with
        associated Archivos and then redirects to a success page.
        """
        form.instance.status = 'Borrador'
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        primeraplana = self.object.id
        #### MODIFICAR SENDER
        sender = 'guadarramaangel@gmail.com'
        titulo_mensaje = self.object.titulo_mensaje
        cuerpo_mensaje = self.object.cuerpo_mensaje
        recipients = self.object.listas.all()
        recipients_final = []
        for lista in recipients:
            for contacto in Contactos.objects.filter(listas=lista):
                recipients_final.append(contacto.correo)
        #Enviar correo
        email = EmailMessage(titulo_mensaje, cuerpo_mensaje, sender, [], recipients_final)
        for b in Archivos.objects.filter(primeraplana=self.object.id):
            dir_path = os.path.join(settings.MEDIA_ROOT, '')
            archivo_final =  dir_path + str(b)
            email.attach_file(archivo_final)
        email.send()
        #Cambiar estatus de primera plana
        c = PrimerasPlanas.objects.get(id=self.object.id)
        c.status = "Enviado"
        c.save()
        return HttpResponseRedirect("/primerasplanas/ver")


    def form_invalid(self, form, formset):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  formset=formset))

    
#INDIVIDUAL
class PrimeraPlanaDetailView(DetailView):
    model = PrimerasPlanas
    slug_field = 'id'
    template_name="primerasplanas/singleprimeraplana.html"

    def get_context_data(self, **kwargs):
        context = super(PrimeraPlanaDetailView, self).get_context_data(**kwargs)
        primeraplana = self.object
        context["archivos"] = Archivos.objects.filter(primeraplana=primeraplana)
        return context
    
    
#ELIMINAR
class PrimeraPlanaDeleteView(DeleteView):
    model = PrimerasPlanas
    slug_field = 'id'
    success_url = '/primerasplanas/ver'
    
    def get_context_data(self, **kwargs):
        context = super(PrimeraPlanaDeleteView, self).get_context_data(**kwargs)
        primeraplana = self.object
        context["archivos"] = Archivos.objects.filter(primeraplana=primeraplana)
        return context