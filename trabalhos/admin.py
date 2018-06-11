# Register your models here.
from django.contrib import admin
from trabalhos.models import Trabalho


class TrabalhoAdmin(admin.ModelAdmin):
    list_display = ('ano', 'titulo', 'natureza')
    list_filter = ['ano', 'natureza']
    search_fields = ['titulo']
admin.site.register(Trabalho, TrabalhoAdmin)