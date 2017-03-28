from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .models import *


def inicio(request):
    html = """<h1>Opções</h1>
                <ul>
                    <li><a href='/eventos'>Eventos</a></li>
                    <li><a href='/eventosCientificos'>Eventos Cientificos</a></li>
                    <li><a href='/artigosCientificos'>Artigos Cientificos</a></li>
                    <li><a href='/pessoas'>Pessoas</a></li>
                    <li><a href='/autores'>Autores</a></li>
                    <li><a href='/pessoasFisicas'>Pessoas Fisicas</a></li>
                    <li><a href='/pessoasJuridicas'>Pessoas Juridicas</a></li>
                    <li><a href='/inscricao'>Inscricao</a></li>

                </ul>
            """
    return HttpResponse(html)


def listaAutor(request):
    html = "<h1>Lista de Autores</h1>"
    lista= Autor.objects.all()
    for tipo in lista:
        html += '<li>{}</li>'.format(tipo.curriculo)

    return HttpResponse(html)

def listaEvento(request):
    html = "<h1>Lista de Eventos</h1>"
    lista= Evento.objects.all()
    for tipo in lista:
        html += '<li>{}</li>'.format(tipo.nome)

    return HttpResponse(html)

def listaEventoCientifico(request):
    html = "<h1>Lista de Eventos Cientificos</h1>"
    lista= EventoCientifico.objects.all()
    for tipo in lista:
        html += '<li>{}</li>'.format(tipo.issn)

    return HttpResponse(html)

def listaArtigoCientifico(request):
    html = "<h1>Lista de Artigos Cientificos</h1>"
    lista = ArtigoCientifico.objects.all()
    for tipo in lista:
        html += '<li>{}</li>'.format(tipo.titulo)

    return HttpResponse(html)


def listaPessoa(request):
    html = "<h1>Lista de pessoa</h1>"
    pessoa = Pessoa.objects.all()
    for tipo in pessoa:
        html += '<li>{}</li>'.format(tipo.nome)

    return HttpResponse(html)


@csrf_exempt
def addautor(request):
    if request.method == 'POST':
        autor = Autor()
        autor.pessoa = request.POST['pessoa']
        autor.save()
        return HttpResponse('Autor Inserido com sucesso')
    else:
        return HttpResponse('Falha na inserção do autor')




@csrf_exempt
def addArtigoCientifico(request):
    if request.method == 'POST':
        artCienti = ArtigoCientifico()
        artCienti.titulo = request.POST['titulo']
        artiCienti.save()
        return HttpResponse('Artigo Cientifico Inserido com sucesso')
    else:
        return HttpResponse('Falha na inserção do Artigo Cientifico')
