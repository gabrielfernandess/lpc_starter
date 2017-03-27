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

                </ul>
            """
    return HttpResponse(html)


def listaAutor(request):
    html = "<h1>Lista de Tipo de Atividades</h1>"
    lista= Autores.objects.all()
    for tipo in lista:
        html += '<li>{}</li>'.format(tipo.curriculo)

    return HttpResponse(html)

def listaArtigoCientifico(request):
    html = "<h1>Lista de Artigos Cientificos</h1>"
    lista = ArtigoCientifico.objects.all()
    for tipo in lista:
        html += '<li>{}</li>'.format(tipo.titulo)

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
