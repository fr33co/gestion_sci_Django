from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, DeleteView

from .models import Resumen, TagsResumen, UrlResumen
from .forms import ResumenForm

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
        context["Resumenes"] = Resumen.objects.filter(titulo_resumen=resumen)
        return context


#ELIMINAR RESUMEN
class ResumenDeleteView(DeleteView):
    pass
    
