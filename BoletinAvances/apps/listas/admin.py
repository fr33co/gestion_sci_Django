from django.contrib import admin
from BoletinAvances.apps.listas.models import Listas


class ListasAdmin(admin.ModelAdmin):
    list_display = ('tipo_lista', 'nombre_lista',)
    search_fields = ['tipo_lista', 'nombre_lista',]
    ordering = ('tipo_lista', 'nombre_lista', )
    fieldsets = (
            ('Campos esenciales', {
                'fields': ('tipo_lista', 'nombre_lista', 'descripcion_lista',)
            }),
        )
    

admin.site.register(Listas, ListasAdmin)