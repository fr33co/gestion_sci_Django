from django.db import models
from datetime import datetime

# Create your models here.

class UrlResumen(models.Model):
    url = models.CharField(max_length=400)

    def __unicode__(self):
        return self.url

class TagsResumen(models.Model):
    tag = models.CharField(max_length=40)

    def __unicode__(self):
        return self.tag

class Resumen(models.Model):

    tag_resumen = models.ForeignKey(TagsResumen, unique = True, blank = True)
    titulo_resumen = models.CharField(max_length=150)
    texto_resumen = models.TextField()
    url_resumen = models.ManyToManyField(UrlResumen, blank=True, default = '')
    fecha = models.DateField(default=datetime.now, blank=True, null=True)
    hora = models.TimeField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(max_length=110, verbose_name='Status', blank=True, null=True)

    def get_url_resumen(self):
        return "\n".join([p.url for p in self.url_resumen.all()])

    def __unicode__(self):
        return self.titulo_resumen
