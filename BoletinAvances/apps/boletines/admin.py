from django.contrib import admin
from BoletinAvances.apps.boletines.models import Boletines, Archivos


class ArchivosInlineAdmin(admin.TabularInline):
    verbose_name = "Archivo"
    verbose_name_plural = "Archivos"
    model = Archivos
    extra = 0
    

class BoletinesAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'hora', 'tipo_envio', 'enviadopor', 'status')
    search_fields = ['fecha', 'hora', 'tipo_envio', 'enviadopor', 'status']
    ordering = ('fecha', 'hora', 'tipo_envio', 'enviadopor', 'status')
    fieldsets = (
            ('Campos esenciales', {
                'fields': ('fecha', 'hora', 'tipo_envio', 'status', 'enviadopor', 'listas', 'titulo_mensaje', 'cuerpo_mensaje',)
            }),
        )

    inlines = (ArchivosInlineAdmin,)


class ArchivosAdmin(admin.ModelAdmin):
    list_display = ('documento',)
    search_fields = ['documento',]
    ordering = ('documento', 'boletines',)
    fieldsets = (
            ('Campos esenciales', {
                'fields': ('documento', 'boletines',)
            }),
        )

admin.site.register(Boletines, BoletinesAdmin)
admin.site.register(Archivos, ArchivosAdmin)