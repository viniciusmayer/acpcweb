from django.db import models


class Arquivo(models.Model):
    arquivo = models.FileField(max_length=255, unique=True)
    paginas = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{0}'.format(self.nomeArquivo())
    
    def nomeArquivo(self):
        return self.arquivo.name[self.arquivo.name.rfind('/') + 1:len(self.arquivo.name)]

class Trabalho(models.Model):
    ano = models.PositiveSmallIntegerField()
    titulo = models.CharField(max_length=255)
    natureza = models.CharField(max_length=255)
    arquivo = models.ForeignKey(Arquivo, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ('ano', 'titulo', 'natureza')
        
    def __str__(self):
        return '{0}, {1}, {2}'.format(self.ano, self.titulo, self.natureza)

class Evento(models.Model):
    nome = models.CharField(max_length=255)
    quando = models.DateField()
    trabalhos = models.ManyToManyField(Trabalho, through='EventoTrabalho')
    
    class Meta:
        unique_together = ('nome', 'quando')

    def __str__(self):
        return '{0}, {1}'.format(self.nome, self.quando)

class EventoTrabalho(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    trabalho = models.ForeignKey(Trabalho, on_delete=models.CASCADE)
    ordem = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('evento', 'trabalho', 'ordem')

    #def __str__(self):
    #    return '{0}, {1}, {2}'.format(self.quando, self.nome)
