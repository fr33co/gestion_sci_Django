from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, DeleteView

from .models import Resumen, NoticiaResumen
from .forms import ResumenForm, NoticiaResumenForm

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
    pass

#INDIVIDUAL RESUMEN
class ResumenDetailView(DetailView):
    model = Resumen
    slug_field = 'id'
    template_name="resumen/singleResumen.html"

    def get_context_data(self, **kwargs):
        context = super(ResumenDetailView, self).get_context_data(**kwargs)
        resumen = self.object
        context["Resumenes"] = Resumen.objects.filter(resumenes=resumen)
        return context


#ELIMINAR RESUMEN
class ResumenDeleteView(DeleteView):
    pass
