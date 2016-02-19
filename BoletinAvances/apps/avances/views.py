import hashlib
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, DeleteView
from django.contrib import messages

from BoletinAvances.apps.listas.models import Listas
from BoletinAvances.apps.listas.forms import ListasForm
from BoletinAvances.apps.contactos.models import Contactos
from BoletinAvances.apps.contactos.forms import ContactosForm
from BoletinAvances.apps.avances.models import Avances, Diarios, Noticias
from BoletinAvances.apps.avances.forms import AvancesForm, DiariosForm, NoticiasForm, NoticiasFormSet

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, Context
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.template.loader import get_template
import os
from django.conf import settings
from django.shortcuts import get_object_or_404, render


#LISTAR DIARIOS
class DiariosListView(ListView):
    model = Diarios
    queryset = Diarios.objects.order_by('id')
    context_object_name = "Diarios"
    template_name = "Diarios/listaDiarios.html"

#CREAR DIARIOS
class DiarioAddView(FormView):
    form_class = DiariosForm
    success_url = reverse_lazy('ver_diarios')
    template_name = "Diarios/enviarDiarios.html"

    def form_valid(self, form):
        form.save(commit=True)
        messages.success(self.request, 'Diario cargado!', fail_silently=True)
        return super(DiarioAddView, self).form_valid(form)


#INDIVIDUAL DIARIOS
class DiariosDetailView(DetailView):
    model = Diarios
    slug_field = 'id'
    template_name="Diarios/singleDiarios.html"


#ELIMINAR DIARIOS
class DiariosDeleteView(DeleteView):
    model = Diarios
    slug_field = 'id'
    template_name='Diarios/diarios_confirm_delete.html'
    success_url = '/avances/Diariosver'


#LISTAS NOTICIAS
class NoticiasListView(ListView):
    model = Noticias
    queryset = Noticias.objects.order_by('id')
    context_object_name = "Noticias"
    template_name = "Noticias/listaNoticias.html"


#CREAR NOTICIAS
class NoticiasAddView(FormView):
    form_class = NoticiasForm
    success_url = reverse_lazy('ver_noticias')
    template_name = "Noticias/enviarNoticia.html"

    def form_valid(self, form):
        form.instance.status = 'Borrador'
        form.save(commit=True)
        messages.success(self.request, 'Noticia cargada!', fail_silently=True)
        return super(NoticiasAddView, self).form_valid(form)


#INDIVIDUAL NOTICIAS
class NoticiasDetailView(DetailView):
    model = Noticias
    slug_field = 'id'
    template_name="Noticias/singlenoticias.html"


#LISTAS AVANCES
class AvancesListView(ListView):
    model = Avances
    queryset = Avances.objects.order_by('id')
    context_object_name = "Avances"
    template_name = "avances/listaAvances.html"


#CREAR AVANCES
class AvancesAddView(FormView):
    model = Avances
    form_class = AvancesForm
    success_url = reverse_lazy('ver_avances')
    template_name = "avances/enviarAvance.html"


    def get_context_data(self, **kwargs):
        context = super(AvancesAddView, self).get_context_data(**kwargs)
        context["Noticias"] = Noticias.objects.all().filter(status__startswith='Borrador')
        return context


    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
            self.get_context_data(form=form))


    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        avances = form.save()
        if (form.is_valid()):
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form, **kwargs):
        """
        Called if all forms are valid. Creates a Avances instance along with
        associated Noticias and then redirects to a success page.
        """
        form.instance.status = 'Borrador'
        self.object = form.save()
        avance = self.object.id

        #Cambiar estatus a las noticias
        context = self.get_context_data(**kwargs)
        noticias =  context['Noticias']
        for a in noticias:
            print a.id
            b = Noticias.objects.get(id=a.id)
            b.status = "Enviado"
            b.save()

        ### MODIFICAR SENDER
        sender = 'guadarramaangel@gmail.com'
        titulo_mensaje = self.object.titulo_mensaje
        cuerpo_mensaje = self.object.cuerpo_mensaje
        recipients = self.object.listas.all()
        recipients_final = []
        for lista in recipients:
            print 'POR CORREO'
            print recipients
            print lista
            for contacto in Contactos.objects.filter(listas=lista):
                print contacto
                recipients_final.append(contacto.correo)
        #Cambiar estatus a las noticias
        context = self.get_context_data(**kwargs)
        noticias =  context['Noticias']
        for a in noticias:
            n_fecha = a.fecha
            n_hora = a.hora
            n_titulo = a.titulo_noticia
            n_url = a.url
            n_noticia = a.noticia
            data_noticias = {'fecha': n_fecha, 'hora': n_hora, 'titulo': n_titulo,
                            'url': n_url, 'noticia': n_noticia}
            b = Noticias.objects.get(id=a.id)
            b.status = "Enviado"
            b.save()
        #Enviar correo
        htmly = get_template('avances/AvancesEmail.html')
        d = Context({ 'username': 'ANGEL' })
        html_content = htmly.render(d)
        print titulo_mensaje
        print html_content
        print sender
        print recipients_final
        email = EmailMessage(titulo_mensaje, html_content, sender, [], recipients_final)
        email.send()
        ##Cambiar estatus de boletin
        c = Avances.objects.get(id=avance)
        c.status = "Enviado"
        c.save()
        return HttpResponseRedirect("/avances/Avancesver")


    def form_invalid(self, form, formset):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form))


#INDIVIDUAL AVANCES
class AvancesDetailView(DetailView):
    model = Avances
    slug_field = 'id'
    template_name="avances/singleavance.html"

    def get_context_data(self, **kwargs):
        context = super(AvancesDetailView, self).get_context_data(**kwargs)
        avance = self.object
        context["noticias"] = Noticias.objects.filter(avances=avance)
        return context


#ELIMINAR AVANCES
class AvancesDeleteView(DeleteView):
    model = Avances
    slug_field = 'id'
    success_url = '/avances/Avancesver'

    def get_context_data(self, **kwargs):
        context = super(AvancesDeleteView, self).get_context_data(**kwargs)
        avance = self.object
        context["noticias"] = Noticias.objects.filter(avances=avance)
        return context
