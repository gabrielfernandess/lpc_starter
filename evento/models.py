__autor__ = 'ESANTIAGO'

from django.db import models

class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=200)
    endereco = models.IntegerField('endereco')
    cep = models.CharField('cep', max_length=8)
    telefone = models.CharField('telefone', max_length=9)
    cidade = models.CharField('cidade', max_length=200)
    estado = models.CharField('estado', max_length=200)

    def __repr__(self):
        return self.nome