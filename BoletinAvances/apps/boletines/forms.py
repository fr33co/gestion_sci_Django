from django import forms
from django.forms.models import inlineformset_factory
from BoletinAvances.apps.boletines.models import Boletines, Archivos


class BoletinesForm(forms.ModelForm):
    class Meta:
        model = Boletines
        exclude = ('status',)
        fields = '__all__'
        
        
class ArchivosForm(forms.ModelForm):
    class Meta:
        model = Archivos
        fields = '__all__'

ArchivosFormSet = inlineformset_factory(Boletines, Archivos, fields = '__all__', can_delete=True, extra=0)
item_forms = ArchivosFormSet() 