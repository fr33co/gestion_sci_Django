from django.contrib import admin
from BoletinAvances.apps.avances.models import Avances, Diarios, Noticias, EnlaceDiarios


class NoticiasInlineAdmin(admin.TabularInline):
    verbose_name = "Noticia"
    verbose_name_plural = "Noticias"
    model = Noticias
    extra = 0

class AvancesAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'hora', 'tipo_envio', 'enviadopor', 'status',)
    search_fields = ['fecha', 'hora', 'tipo_envio', 'enviadopor', 'status']
    ordering = ('fecha', 'hora', 'tipo_envio', 'enviadopor', 'status',)
    fieldsets = (
            ('Campos esenciales', {
                'fields': ('fecha', 'hora', 'tipo_envio', 'status', 'enviadopor', 'listas', 'titulo_mensaje', 'cuerpo_mensaje',)
            }),
        )

    inlines = (NoticiasInlineAdmin,)


class DiariosAdmin(admin.ModelAdmin):
    list_display = ('pais', 'estado', 'nombre_diario',)
    search_fields = ['pais', 'estado', 'nombre_diario',]
    ordering = ('pais', 'estado', 'nombre_diario',)
    fieldsets = (
            ('Campos esenciales', {
                'fields': ('pais', 'estado', 'nombre_diario',)
            }),
        )


class EnlaceDiariosAdmin(admin.ModelAdmin):
    list_display = ('diario', 'noticia', 'url')
    search_fields = ['diario', 'noticia','url']
    ordering = ('diario', 'noticia', 'url',)
    fieldsets = (
        ('Campos', {
            'fields': ('diario', 'noticia', 'url',)
        }),
    )


class EnlaceDiariosInlineAdmin(admin.TabularInline):
    verbose_name = "Enlace"
    verbose_name_plural = "Enlaces"
    model = EnlaceDiarios
    extra = 0


class NoticiasAdmin(admin.ModelAdmin):
    list_display = ('status', 'enviadopor', 'tag', 'fecha', 'titulo_noticia', 'noticia',)
    search_fields = ['status', 'enviadopor', 'tag', 'fecha', 'titulo_noticia', 'noticia',]
    ordering = ('status', 'enviadopor', 'tag', 'fecha', 'titulo_noticia', 'noticia',)
    fieldsets = (
            ('Campos esenciales', {
                'fields': ('tag', 'avances', 'status', 'enviadopor', 'fecha', 'antetitulo_noticia', 'titulo_noticia', 'noticia',)
            }),
        )

    inline = EnlaceDiariosInlineAdmin

admin.site.register(Avances, AvancesAdmin)
admin.site.register(Diarios, DiariosAdmin)
admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(EnlaceDiarios, EnlaceDiariosAdmin)
