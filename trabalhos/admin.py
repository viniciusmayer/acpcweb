from django.contrib import admin
from trabalhos.models import Trabalho, Arquivo


class TrabalhoAdmin(admin.ModelAdmin):
    list_display = ('ano', 'titulo', 'natureza',)
    list_filter = ['ano', 'natureza',]
    search_fields = ['titulo',]
admin.site.register(Trabalho, TrabalhoAdmin)

class ArquivoAdmin(admin.ModelAdmin):
    list_display = ('arquivo', 'paginas')
    search_fields = ['arquivo',]
admin.site.register(Arquivo, ArquivoAdmin)