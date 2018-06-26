from django.contrib import admin
from trabalhos.models import Trabalho, Arquivo, Evento, EventoTrabalho, Tag, \
    Natureza, Entidade


class EntidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', )
    search_field = ['nome', 'descricao', ]
admin.site.register(Entidade, EntidadeAdmin)

class NaturezaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao',)
    search_fields = ['nome', 'descricao',]
admin.site.register(Natureza, NaturezaAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'ordem',)
    search_fields = ['nome', 'descricao',]
admin.site.register(Tag, TagAdmin)

class TrabalhoAdmin(admin.ModelAdmin):
    list_display = ('ano', 'titulo', 'entidade', 'natureza', 'tag', 'arquivo',)
    list_filter = ['ano', 'ano_fim', 'entidade', 'natureza', 'tag',]
    search_fields = ['titulo',]
admin.site.register(Trabalho, TrabalhoAdmin)

class ArquivoAdmin(admin.ModelAdmin):
    list_display = ('nomeArquivo', 'paginas')
    search_fields = ['arquivo',]
admin.site.register(Arquivo, ArquivoAdmin)

class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quando', )
    search_fields = ['nome', ]
admin.site.register(Evento, EventoAdmin)

class EventoTrabalhoAdmin(admin.ModelAdmin):
    list_display = ('evento', 'trabalho', 'ordem',)
    list_filter = ['evento']
admin.site.register(EventoTrabalho, EventoTrabalhoAdmin)
