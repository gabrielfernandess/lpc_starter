from django.db import models
from django.utils import timezone


class ArtigoCientifico(models.Model):
    titulo = models.CharField('titulo', max_length=200)
    evento = models.ForeignKey('EventoCientifico')
    autores = models.ForeignKey('Autor')

    def save(self, *args, **kwargs):
        self.evento = self.evento.upper()
        self.autores = self.local.upper()

    def __str__(self):
        return '{}'.format(self.titulo)

    def __unicode__(self):
        return self.id

class Inscricao(models.Model):
    nome = models.ForeignKey('PessoaFisica')
    evento = models.ForeignKey('Evento')
    dataEHoraDaInscricao = models.DateTimeField('data e hora da inscrição', default=timezone.now)
    tipoDaInscricao = models.CharField('Tipo da Inscricao', max_length=200)

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        self.evento = self.evento.upper()

    def __str__(self):
        return '{}'.format(self.nome)

    def __unicode__(self):
        return self.id

class Evento(models.Model):
    nome = models.CharField('nome', max_length=200)
    eventoPrincipal = models.CharField('evento principal', max_length=200)
    sigla = models.CharField('sigla', max_length=50)
    dataEHoraDeInicio = models.DateTimeField('data e hora de inicio', default=timezone.now)
    palavrasChave = models.CharField('palavras chave',max_length=200)
    logotipo = models.CharField('logotipo',max_length=200)
    realizador=models.ForeignKey('Pessoa')
    cidade = models.CharField('cidade', max_length=200)
    uf = models.CharField('uf', max_length=200)
    endereco = models.CharField('endereço', max_length=200)
    cep = models.CharField('cep', max_length=200)

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        self.eventoPrincipal = self.eventoPrincipal.upper()

        super(Evento, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.nome)

class EventoCientifico(models.Model):
    evento = models.ForeignKey('Evento')
    issn = models.CharField('issn', max_length=200)

    def save(self, *args, **kwargs):
        self.issn = self.issn.upper()
        return super(EventoCientifico, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.issn)

class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=200)
    email = models.EmailField(max_length=70, blank=True)

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()

        if self.email:
            self.email = self.email.upper()

        return super(Pessoa, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome

class PessoaJuridica(models.Model):
    pessoa = models.ForeignKey('Pessoa')
    cnpj = models.CharField('cnpj', max_length=200)
    razaoSocial = models.CharField('razao social', max_length=200)

    def save(self, *args, **kwargs):
        self.cnpj = self.cnpj.upper()
        return super(PessoaJuridica, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.cnpj)

class PessoaFisica(models.Model):
    pessoa = models.ForeignKey('Pessoa')
    cpf = models.CharField('cpf', max_length=200)

    def save(self, *args, **kwargs):
        self.cpf = self.cpf.upper()
        return super(PessoaFisica, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.cpf)

class Autor(models.Model):
    pessoa = models.ForeignKey('Pessoa')
    curriculo = models.CharField('curriculo', max_length=200)
    artigos = models.TextField('Artigo')
    class Meta:
        verbose_name = 'autor'
        verbose_name_plural = 'autores'

    def save(self, *args, **kwargs):
        self.curriculo = self.curriculo.upper()
        return super(Autor, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.curriculo)
