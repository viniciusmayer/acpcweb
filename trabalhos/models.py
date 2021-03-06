from django.db import models


class Entidade(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['nome']

    def __str__(self):
        return '{s}'.format(s=self.nome)
    

class Arquivo(models.Model):
    arquivo = models.FileField(max_length=255, unique=True)
    paginas = models.PositiveSmallIntegerField()
    ativo = models.BooleanField(default=True)

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
    ativo = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['nome']
    
    def __str__(self):
        return '{0}'.format(self.nome)


class Natureza(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)
    
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
    ativo = models.BooleanField(default=True)

    class Meta:
        unique_together = ('ano', 'titulo', 'natureza', 'tag')
        ordering = ['ano', 'tag', 'titulo']

    def __str__(self):
        return '{0}, {1}, {2}, {3}'.format(self.ano, self.tag, self.nomeTrabalho(), self.natureza)

    def nomeTrabalho(self):
        return self.titulo if len(self.titulo) < 71 else '{0}...'.format(self.titulo[0:70])


class Evento(models.Model):
    nome = models.CharField(max_length=255)
    quando = models.DateField()
    trabalhos = models.ManyToManyField(Trabalho, through='EventoTrabalho')
    ativo = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('nome', 'quando')
        ordering = ['nome']

    def __str__(self):
        return '{0}'.format(self.nome)


class EventoTrabalho(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    trabalho = models.ForeignKey(Trabalho, on_delete=models.CASCADE) #limit_choices_to=Trabalho.objects.exclude(id__in=EventoTrabalho.objects.select_related('trabalho')).filter(evento=evento))
    ordem = models.PositiveSmallIntegerField()
    ativo = models.BooleanField(default=True)

    class Meta:
        unique_together = ('evento', 'trabalho', 'ordem')
        ordering = ['ordem']
