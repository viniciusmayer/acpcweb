from django.contrib import admin
from trabalhos.models import Trabalho, Arquivo, Evento, EventoTrabalho


class TrabalhoAdmin(admin.ModelAdmin):
    list_display = ('ano', 'ano_fim', 'titulo', 'natureza', 'tag', 'arquivo',)
    list_filter = ['ano', 'ano_fim', 'natureza', 'tag',]
    search_fields = ['titulo',]
admin.site.register(Trabalho, TrabalhoAdmin)

class ArquivoAdmin(admin.ModelAdmin):
    list_display = ('nomeArquivo', 'paginas')
    search_fields = ['arquivo',]
admin.site.register(Arquivo, ArquivoAdmin)

class EventoTrabalhoInline(admin.StackedInline):
    model = EventoTrabalho
    extra = 3

class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quando', )
    search_fields = ['nome', ]
    inlines = [EventoTrabalhoInline]
admin.site.register(Evento, EventoAdmin)

