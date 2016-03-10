from django.contrib import admin
from BoletinAvances.apps.resumen.models import Resumen, UrlResumen, TagsResumen
# Register your models here.

class ResumenInlineAdmin(admin.TabularInline):
    verbose_name = "Resumen"
    verbose_name_plural = "Resumenes"
    model = Resumen
    extra = 0

class ResumenAdmin(admin.ModelAdmin):
    list_display = ('tag_resumen', 'titulo_resumen', 'texto_resumen', 'get_url_resumen',)
    search_list = ['tag_resumen',]
    ordering = ('tag_resumen',)
    fieldsets = (
            ('Campos', {
                'fields' : ('tag_resumen', 'titulo_resumen', 'texto_resumen', 'url_resumen')
            }),
    )
    inline = ResumenInlineAdmin

class UrlResumenAdmin(admin.ModelAdmin):
    list_display = ('url',)

admin.site.register(Resumen, ResumenAdmin)
admin.site.register(UrlResumen, UrlResumenAdmin)
admin.site.register(TagsResumen)
