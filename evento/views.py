__autor__ = 'ESANTIAGO'

from django.http import HttpResponse, Http404
from evento.models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()
    retorno_pessoa = ''

    for pessoa in pessoas:
        retorno_pessoa += "<li>" + pessoa.nome + "</li>"

    return HttpResponse(retorno_pessoa)

def detail(request, pk):

    try:
        pessoas = Pessoa.objects.get(pk=pk)
    except Pessoa.DoesNotExist:
        raise Http404("Pessoa não existe.")

    return HttpResponse(pessoas.nome + ' - ' + pessoas.cidade + ' - ' + pessoas.estado)