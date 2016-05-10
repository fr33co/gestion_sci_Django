from django import forms
from django.forms.models import inlineformset_factory
from BoletinAvances.apps.avances.models import Avances, Diarios, Noticias, EnlaceDiarios


class DiariosForm(forms.ModelForm):
    class Meta:
        model = Diarios
        fields = '__all__'


class AvancesForm(forms.ModelForm):
    class Meta:
        model = Avances
        exclude = ('status',)
        fields = '__all__'


class NoticiasForm(forms.ModelForm):
    class Meta:
        model = Noticias
        exclude = ('avances', 'enviadopor',)
        fields = '__all__'

class EnlaceDiariosForm(forms.ModelForm):
    class Meta:
        model = EnlaceDiarios
        exclude = ('noticias',)
        fields = '__all__'

NoticiasFormSet = inlineformset_factory(Avances, Noticias, fields = '__all__', can_delete=True, extra=0)
item_forms = NoticiasFormSet()
EnlaceDiariosFormSet = inlineformset_factory(Noticias, EnlaceDiarios, fields = '__all__', can_delete=True, extra=0)
