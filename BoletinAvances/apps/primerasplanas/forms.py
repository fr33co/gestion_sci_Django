from django import forms
from django.forms.models import inlineformset_factory
from BoletinAvances.apps.primerasplanas.models import PrimerasPlanas, Archivos


class PrimerasPlanasForm(forms.ModelForm):
    class Meta:
        model = PrimerasPlanas
        exclude = ('status',)
        fields = '__all__'
        
        
class ArchivosForm(forms.ModelForm):
    class Meta:
        model = Archivos
        fields = '__all__'
        widgets = {'documento': forms.HiddenInput()}


ArchivosFormSet = inlineformset_factory(PrimerasPlanas, Archivos, fields = '__all__', can_delete=True, extra=0)
item_forms = ArchivosFormSet() 