from django.db import models

class Arquivo(models.Model):
    nome = models.CharField(editable=False, unique=True, max_length=255)
        
class Trabalho(models.Model):
    ano = models.PositiveSmallIntegerField(editable=False)
    titulo = models.CharField(editable=False, max_length=255)
    natureza = models.CharField(editable=False, max_length=255)
    arquivo = models.ForeignKey(Arquivo, on_delete=models.SET_NULL, null=True)