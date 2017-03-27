from django.db import models
from django.utils import timezone


class ArtigoCientifico(models.Model):
    titulo = models.CharField('titulo', max_length=200)
    evento = models.ForeignKey('EventoCientifico')
    autores = models.TextField('Autor')



class Evento(models.Model):
    nome = models.CharField('nome', max_length=200)
    eventoPrincipal = models.CharField('evento rincipal', max_length=200)
    sigla = models.CharField('sigla', max_length=50)
    dataEHoraDeInicio = models.DateTimeField('data e hora de inicio', default=timezone.now)
    palavrasChave = models.CharField('palavras chave',max_length=200)
    logotipo = models.CharField('logotipo',max_length=200)
    realizador=models.ForeignKey('Pessoa')
    cidade = models.CharField('cidade', max_length=200)
    uf = models.CharField('uf', max_length=200)
    endereco = models.CharField('endereço', max_length=200)
    cep = models.DateTimeField('cep', max_length=200)

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        self.local = self.local.upper()

        super(Evento, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.nome)

class EventoCientifico(models.Model):
    evento = models.ForeignKey('Evento')
    issn = models.CharField('issn', max_length=200)

class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=200)
    email = models.EmailField(max_length=70, blank=True)

class PessoaJuridica(models.Model):
    pessoa = models.ForeignKey('Pessoa')
    cnpj = models.CharField('cnpj', max_length=200)
    razaoSocial = models.CharField('cnpj', max_length=200)

class PessoaFisica(models.Model):
    pessoa = models.ForeignKey('Pessoa')
    cpf = models.CharField('cpf', max_length=200)

class Autor(models.Model):
    pessoa = models.ForeignKey('Pessoa')
    curriculo = models.CharField('curriculo', max_length=200)
    artigos = models.TextField('Artigo')
    class Meta:
        verbose_name = 'autor'
        verbose_name_plural = 'autores'

    def save(self, *args, **kwargs):
        self.pessoa = self.pessoa.upper()
        return super(Autor, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.pessoa)
