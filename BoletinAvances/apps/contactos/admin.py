from django.contrib import admin
from BoletinAvances.apps.contactos.models import Contactos


class ContactosAdmin(admin.ModelAdmin):
    list_display = ('nombre_contacto', 'institucion', 'telefono', 'correo',)
    search_fields = ['nombre_contacto', 'institucion',]
    ordering = ('nombre_contacto', 'institucion',)
    fieldsets = (
            ('Campos esenciales', {
                'fields': ('nombre_contacto', 'institucion', 'telefono', 'correo', 'listas')
            }),
        )
    

admin.site.register(Contactos, ContactosAdmin)