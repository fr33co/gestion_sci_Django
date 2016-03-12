from django.contrib import admin
from BoletinAvances.apps.resumen.models import Resumen, NoticiaResumen
# Register your models here.

class ResumenInlineAdmin(admin.TabularInline):
    verbose_name = "Resumen"
    verbose_name_plural = "Resumenes"
    model = Resumen
    extra = 0

class ResumenAdmin(admin.ModelAdmin):
    list_display = ('titulo_mensaje','fecha', 'status', 'enviadopor',)
    search_list = ['fecha', 'status',]
    ordering = ('fecha', 'status', 'enviadopor',)
    fieldsets = (
            ('Campos', {
                'fields' : ('titulo_mensaje', 'cuerpo_mensaje', 'fecha', 'status', 'enviadopor',)
            }),
    )
    inline = ResumenInlineAdmin

class NoticiaResumenAdmin(admin.ModelAdmin):
    list_display = ('titulo_noticia_resumen', 'cuerpo_noticia_resumen', 'tag_noticia_resumen', 'url_noticia_resumen',)
    search_list = ['tag_noticia_resumen',]


admin.site.register(Resumen, ResumenAdmin)
admin.site.register(NoticiaResumen, NoticiaResumenAdmin)
