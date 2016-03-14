from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, DeleteView

import datetime

from .models import Resumen, NoticiaResumen
from .forms import ResumenForm, NoticiaResumenForm
from BoletinAvances.apps.listas.models import Listas
from BoletinAvances.apps.listas.forms import ListasForm
from BoletinAvances.apps.contactos.models import Contactos
from BoletinAvances.apps.contactos.forms import ContactosForm

#LISTA DE RESUMENES DE NOTICIAS
class NoticiaResumenListView(ListView):
    model = NoticiaResumen
    queryset = NoticiaResumen.objects.order_by('id')
    context_object_name = "NoticiasResumen"
    template_name = "resumen/listaNoticiaResumen.html"

#CREAR RESUMEN DE NOTICIA
class NoticiaResumenAddView(FormView):
    form_class = NoticiaResumenForm
    success_url = reverse_lazy('ver_noticia_resumen')
    template_name = "resumen/enviarNoticiaResumen.html"

    def form_valid(self, form):
        form.instance.status = 'Borrador'
        form.save(commit=True)
        return super(NoticiaResumenAddView, self).form_valid(form)

#DETALLES RESUMEN DE NOTICIA
class NoticiaResumenDetailView(DetailView):
    model = NoticiaResumen
    slug_field = 'id'
    template_name = "resumen/singleNoticiaResumen.html"

#ELIMINAR RESUMEN DE NOTICIA
class NoticiaResumenDeleteView(DeleteView):
    model = NoticiaResumen
    slug_field = 'id'
    template_name = "resumen/noticia_resumen_confirm_delete.html"
    success_url = reverse_lazy('ver_noticia_resumen')

#LISTAS RESUMEN
class ResumenListView(ListView):
    model = Resumen
    queryset = Resumen.objects.order_by('id')
    context_object_name = "Resumenes"
    template_name = "resumen/listaResumen.html"

#CREAR RESUMEN
class ResumenAddView(FormView):
    model = Resumen
    form_class = ResumenForm
    success_url = reverse_lazy('ver_resumen')
    template_name = "resumen/enviarResumen.html"

    #Asignando tipo de  resumen basado en la hora
    momento = str(datetime.datetime.time(datetime.datetime.now()))
    hora = int(momento[0:2])
    horario = ''
    if hora < 10:
        horario = "Matutino I"
    elif hora >=10 and hora <13:
        horario = "Matutino II"
    else:
        horario = "Vespertino"


    def get_context_data(self, **kwargs):
        context = super(ResumenAddView, self).get_context_data(**kwargs)
        context["Resumenes"] = NoticiaResumen.objects.all().filter(status__startswith='Borrador')
        context["horario"] = self.horario
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
        resumenes = form.save()
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
        resumen = self.object.id

        ### MODIFICAR SENDER
        sender = 'guadarramaangel@gmail.com'
        horario = self.horario
        titulo_mensaje = self.object.titulo_mensaje
        cuerpo_mensaje = self.object.cuerpo_mensaje
        recipients = self.object.listas.all()
        recipients_final = []
        for lista in recipients:
            for contacto in Contactos.objects.filter(listas=lista):
                recipients_final.append(contacto.correo)
        #Pasar datos a plantilla
        context = self.get_context_data(**kwargs)
        resumenes =  context['Resumenes']
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
                    feed['titulo'] = a.titulo_noticia_resumen
                    feed['url'] = a.url_noticia_resumen
                    feed['resumenes'] = a.cuerpo_noticia_resumen
                    feed['tag'] = tag_noticia_resumen
                    #Cambiar el status:
                    b = NoticiaResumen.objects.get(pk = a.pk)
                    b.status = "Enviado"
                    b.save()
                    #Llenando lista con noticias
                    container.append(feed)
        #Render context a plantilla
        htmly = get_template('resumen/ResumenEmail.html')
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
        return HttpResponseRedirect("/resumen/Resumenver")


    def form_invalid(self, form, formset):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form))


#INDIVIDUAL RESUMEN
class ResumenDetailView(DetailView):
    model = Resumen
    slug_field = 'id'
    template_name="resumen/singleResumen.html"


#ELIMINAR RESUMEN
class ResumenDeleteView(DeleteView):
    model = Resumen
    slug_field = 'id'
    template_name = "resumen/resumen_confirm_delete.html"
    success_url = reverse_lazy('ver_resumen')
