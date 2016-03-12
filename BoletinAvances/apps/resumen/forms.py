from django import forms
from .models import Resumen, NoticiaResumen

class ResumenForm(forms.ModelForm):
    class Meta:
        model = Resumen
        fields = '__all__'

class NoticiaResumenForm(forms.ModelForm):
    class Meta:
        model = NoticiaResumen
        fields = '__all__'
