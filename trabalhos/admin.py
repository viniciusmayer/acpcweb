from django_admin_row_actions import AdminRowActionsMixin
from django.contrib import admin
from trabalhos.models import Trabalho, Arquivo, Evento, EventoTrabalho, Tag, \
    Natureza, Entidade


class EntidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao',)
    search_field = ['nome', 'descricao', ]


admin.site.register(Entidade, EntidadeAdmin)


class NaturezaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao',)
    search_fields = ['nome', 'descricao', ]


admin.site.register(Natureza, NaturezaAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'ordem',)
    search_fields = ['nome', 'descricao', ]


admin.site.register(Tag, TagAdmin)


class TrabalhoAdmin(admin.ModelAdmin):
    list_display = ('ano', 'tag', 'titulo', 'natureza', 'arquivo',)
    list_filter = ['ano', 'tag', 'natureza', ]
    search_fields = ['titulo', ]


admin.site.register(Trabalho, TrabalhoAdmin)


class ArquivoAdmin(admin.ModelAdmin):
    list_display = ('nomeArquivo', 'paginas')
    search_fields = ['arquivo', ]


admin.site.register(Arquivo, ArquivoAdmin)


class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quando',)
    search_fields = ['nome', ]


admin.site.register(Evento, EventoAdmin)


class EventoTrabalhoAdmin(AdminRowActionsMixin, admin.ModelAdmin):
    list_display = ('evento', 'trabalho', 'ordem',)
    list_filter = ['evento']
    actions = ('subir_varios', 'descer_varios',)

    def get_row_actions(self, obj):
        row_actions = [
            {'label': 'Subir', 'action': 'subir', },
            {'label': 'Descer', 'action': 'descer', },
        ]
        row_actions += super(EventoTrabalhoAdmin, self).get_row_actions(obj)
        return row_actions

    def subir_varios(self, request, queryset):
        ids = []
        for q in queryset:
            ids.append(q.id)
        ets = EventoTrabalho.objects.filter(id__in=ids).order_by('ordem')
        for et in ets:
            self.subir(request, et)

    def subir(self, request, obj):
        et = EventoTrabalho.objects.get(id=obj.id)
        net = EventoTrabalho.objects.filter(ordem__lt=et.ordem, evento=et.evento).order_by('-ordem').first()
        if net is not None:
            no = net.ordem
            net.ordem = et.ordem
            net.save()
            et.ordem = no
            et.save()
    
    def descer_varios(self, request, queryset):
        ids = []
        for q in queryset:
            ids.append(q.id)
        ets = EventoTrabalho.objects.filter(id__in=ids).order_by('-ordem')
        for et in ets:
            self.descer(request, et)
        
    def descer(self, request, obj):
        et = EventoTrabalho.objects.get(id=obj.id)
        net = EventoTrabalho.objects.filter(ordem__gt=et.ordem, evento=et.evento).order_by('ordem').first()
        if net is not None:
            no = net.ordem
            net.ordem = et.ordem
            net.save()
            et.ordem = no
            et.save()

    
admin.site.register(EventoTrabalho, EventoTrabalhoAdmin)
