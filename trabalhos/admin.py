from django.contrib import admin
from trabalhos.models import Trabalho, Arquivo


class TrabalhoAdmin(admin.ModelAdmin):
    list_display = ('ano', 'titulo', 'natureza', 'arquivo',)
    list_filter = ['ano', 'natureza',]
    search_fields = ['titulo',]
admin.site.register(Trabalho, TrabalhoAdmin)

class ArquivoAdmin(admin.ModelAdmin):
    list_display = ('nomeArquivo', 'paginas')
    search_fields = ['arquivo',]
admin.site.register(Arquivo, ArquivoAdmin)