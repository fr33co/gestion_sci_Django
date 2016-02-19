from django.contrib import admin
from BoletinAvances.apps.avances.models import Avances, Diarios, Noticias


class NoticiasInlineAdmin(admin.TabularInline):
    verbose_name = "Noticia"
    verbose_name_plural = "Noticias"
    model = Noticias
    extra = 0
    

class AvancesAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'tipo_envio', 'enviadopor', 'status')
    search_fields = ['fecha', 'tipo_envio', 'enviadopor', 'status']
    ordering = ('fecha', 'hora', 'tipo_envio', 'enviadopor', 'status')
    fieldsets = (
            ('Campos esenciales', {
                'fields': ('fecha', 'hora', 'tipo_envio', 'status', 'enviadopor', 'listas', 'titulo_mensaje', 'cuerpo_mensaje',)
            }),
        )

    inlines = (NoticiasInlineAdmin,)


class DiariosAdmin(admin.ModelAdmin):
    list_display = ('nombre_diario',)
    search_fields = ['nombre_diario',]
    ordering = ('nombre_diario',)
    fieldsets = (
            ('Campos esenciales', {
                'fields': ('nombre_diario',)
            }),
        )

class NoticiasAdmin(admin.ModelAdmin):
    list_display = ('status', 'enviadopor', 'fecha', 'titulo_noticia', 'url', 'noticia',)
    search_fields = ['status', 'enviadopor', 'fecha', 'titulo_noticia', 'url', 'noticia',]
    ordering = ('status', 'enviadopor', 'fecha', 'titulo_noticia', 'url', 'noticia',)
    fieldsets = (
            ('Campos esenciales', {
                'fields': ('avances', 'status', 'enviadopor', 'fecha', 'hora', 'titulo_noticia', 'url', 'noticia',)
            }),
        )

admin.site.register(Avances, AvancesAdmin)
admin.site.register(Diarios, DiariosAdmin)
admin.site.register(Noticias, NoticiasAdmin)