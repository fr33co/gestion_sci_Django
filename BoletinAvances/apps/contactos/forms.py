from django import forms

from BoletinAvances.apps.contactos.models import Contactos


class ContactosForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = '__all__'