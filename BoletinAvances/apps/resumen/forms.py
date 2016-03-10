from django import forms
from .models import Resumen, TagsResumen, UrlResumen

class ResumenForm(forms.ModelForm):
    class Meta:
        model = Resumen
        fields = '__all__'
