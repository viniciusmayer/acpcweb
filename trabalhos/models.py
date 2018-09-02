from django.db import models


class Entidade(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['nome']

    def __str__(self):
        return '{s}'.format(s=self.nome)
    

class Arquivo(models.Model):
    arquivo = models.FileField(max_length=255, unique=True)
    paginas = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['arquivo']

    def __str__(self):
        return '{0}'.format(self.nomeArquivo())
    
    def nomeArquivo(self):
        return self.arquivo.name[self.arquivo.name.rfind('/') + 1:len(self.arquivo.name)]


class Tag(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.CharField(max_length=255)
    ordem = models.PositiveSmallIntegerField(unique=True)
    
    class Meta:
        ordering = ['nome']
    
    def __str__(self):
        return '{0}'.format(self.nome)


class Natureza(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['nome']
    
    def __str__(self):
        return '{0}'.format(self.nome)


class Trabalho(models.Model):
    ano = models.PositiveSmallIntegerField()
    ano_fim = models.PositiveSmallIntegerField(null=True, blank=True)
    titulo = models.CharField(max_length=255)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)
    natureza = models.ForeignKey(Natureza, on_delete=models.SET_NULL, null=True, blank=True)
    arquivo = models.ForeignKey(Arquivo, on_delete=models.SET_NULL, null=True, blank=True)
    entidade = models.ForeignKey(Entidade, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ('ano', 'titulo', 'natureza', 'tag')
        ordering = ['titulo']

    def __str__(self):
        return '{0}, {1}, {2}'.format(self.ano, self.nomeTrabalho(), self.tag)

    def nomeTrabalho(self):
        nomeTrabalho = self.titulo
        i = nomeTrabalho.find(':') 
        if i > 0:
            nomeTrabalho = nomeTrabalho[0:i]
        return '{0}...'.format(nomeTrabalho if len(nomeTrabalho) < 65 else nomeTrabalho[0:64])


class Evento(models.Model):
    nome = models.CharField(max_length=255)
    quando = models.DateField()
    trabalhos = models.ManyToManyField(Trabalho, through='EventoTrabalho')
    
    class Meta:
        unique_together = ('nome', 'quando')
        ordering = ['nome']

    def __str__(self):
        return '{0}'.format(self.nome)


class EventoTrabalho(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    trabalho = models.ForeignKey(Trabalho, on_delete=models.CASCADE)
    ordem = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('evento', 'trabalho', 'ordem')
