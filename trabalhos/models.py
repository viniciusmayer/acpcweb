from django.db import models


class Arquivo(models.Model):
    arquivo = models.FileField(upload_to='uploads/', max_length=255, unique=True)
        
class Trabalho(models.Model):
    ano = models.PositiveSmallIntegerField()
    titulo = models.CharField(max_length=255)
    natureza = models.CharField(max_length=255)
    arquivo = models.ForeignKey(Arquivo, on_delete=models.SET_NULL, null=True)

class Evento(models.Model):
    nome = models.CharField(max_length=255)
    trabalhos = models.ManyToManyField(Trabalho, through='EventoTrabalho')
    
class EventoTrabalho(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    trabalho = models.ForeignKey(Trabalho, on_delete=models.CASCADE)
    ordem = models.PositiveSmallIntegerField()
