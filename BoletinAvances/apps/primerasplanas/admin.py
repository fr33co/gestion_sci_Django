from django.contrib import admin
from BoletinAvances.apps.primerasplanas.models import PrimerasPlanas, Archivos


class ArchivosInlineAdmin(admin.TabularInline):
    verbose_name = "Archivo"
    verbose_name_plural = "Archivos"
    model = Archivos
    extra = 0
    

class PrimerasPlanasAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'enviadopor', 'status')
    search_fields = ['fecha', 'enviadopor', 'status']
    ordering = ('fecha', 'enviadopor', 'status')
    fieldsets = (
            ('Campos esenciales', {
                'fields': ('fecha', 'status', 'titulo_mensaje', 'cuerpo_mensaje', 'enviadopor', 'listas',)
            }),
        )

    inlines = (ArchivosInlineAdmin,)


class ArchivosAdmin(admin.ModelAdmin):
    list_display = ('documento',)
    search_fields = ['documento',]
    ordering = ('documento', 'primeraplana', 'categoria')
    fieldsets = (
            ('Campos esenciales', {
                'fields': ('documento', 'categoria', 'primeraplana')
            }),
        )

admin.site.register(PrimerasPlanas, PrimerasPlanasAdmin)
admin.site.register(Archivos, ArchivosAdmin)