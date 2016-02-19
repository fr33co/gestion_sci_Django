from django import forms

from BoletinAvances.apps.listas.models import Listas


class ListasForm(forms.ModelForm):
    class Meta:
        model = Listas
        fields = '__all__'