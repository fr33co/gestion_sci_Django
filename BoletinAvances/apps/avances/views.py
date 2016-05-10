import hashlib
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, DeleteView
from django.contrib import messages

from BoletinAvances.apps.listas.models import Listas
from BoletinAvances.apps.listas.forms import ListasForm
from BoletinAvances.apps.contactos.models import Contactos
from BoletinAvances.apps.contactos.forms import ContactosForm
from BoletinAvances.apps.avances.models import Avances, Diarios, Noticias, EnlaceDiarios
from BoletinAvances.apps.avances.forms import AvancesForm, DiariosForm, NoticiasForm, NoticiasFormSet, EnlaceDiariosFormSet

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
    model = Noticias
    success_url = reverse_lazy('ver_noticias')
    template_name = "Noticias/enviarNoticia.html"
    formset = EnlaceDiariosFormSet()

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = EnlaceDiariosFormSet(instance=Noticias())
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
        if form.is_valid():
            noticia = form.save(commit=False)
            formset = EnlaceDiariosFormSet(request.POST, instance=noticia)
            if (form.is_valid() and formset.is_valid()):
                return self.form_valid(form, formset)
            else:
                return self.form_invalid(form, formset)


    def form_valid(self, form):
        form.instance.status = 'Borrador'
        noticia = form.save(commit=True)
        formset.instance = self.object
        formset.save()
        noti = self.object.id
        # return super(NoticiasAddView, self).form_valid(form)
        return HttpResponseRedirect('/avances/Noticiasenviar')

    def form_invalid(self, form, formset):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  formset=formset))



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

        ### MODIFICAR SENDER
        sender = 'guadarramaangel@gmail.com'
        titulo_mensaje = self.object.titulo_mensaje
        cuerpo_mensaje = self.object.cuerpo_mensaje
        recipients = self.object.listas.all()
        recipients_final = []
        for lista in recipients:
            for contacto in Contactos.objects.filter(listas=lista):
                recipients_final.append(contacto.correo)
        #Pasar datos a plantilla
        context = self.get_context_data(**kwargs)
        noticias =  context['Noticias']
        indices = self.request.POST['feeds']
        indices = indices.split(',')
        container = []
        for a in noticias:
            for i in indices:
                if i == str(a.pk):
                    feed = {}
                    feed['id'] = a.pk
                    feed['fecha'] = a.fecha
                    feed['hora'] = a.hora
                    feed['titulo'] = a.titulo_noticia
                    #feed['url'] = a.url
                    feed['noticia'] = a.noticia
                    diarios_lista = a.diarios.all()
                    feed['diarios'] = diarios_lista
                    #Cambiar el status:
                    b = Noticias.objects.get(pk = a.pk)
                    b.status = "Enviado"
                    b.save()
                    #Llenando lista con noticias
                    container.append(feed)
        #Render context a plantilla
        htmly = get_template('avances/AvancesEmail.html')
        d = {'titulo_mensaje': titulo_mensaje,
             'cuerpo_mensaje': cuerpo_mensaje,
             'data_noticias': container}
        html_content = htmly.render(d)
        #Enviar correo
        email = EmailMessage(titulo_mensaje, html_content, sender, [], recipients_final)
        email.content_subtype = 'html'
        email.send()
        # #Cambiar estatus de boletin
        # c = Avances.objects.get(id=avance)
        # c.status = "Enviado"
        # c.save()
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
