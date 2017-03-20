from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .models import TipoAtividade


def inicio(request):
    html = """<h1>Opções</h1>
                <ul>
                    <li><a href='/eventos'>Eventos</a></li>
                    <li><a href='/atividades'>Atividades</a></li>
                    <li><a href='/tipoatividades'>Tipo de Atividade</a></li>
                </ul>
            """
    return HttpResponse(html)


def listaTipoAtividades(request):
    html = "<h1>Lista de Tipo de Atividades</h1>"
    lista = TipoAtividade.objects.all()
    for tipo in lista:
        html += '<li>{}</li>'.format(tipo.descricao)
    
    return HttpResponse(html)

@csrf_exempt
def addTipoAtividade(request):
    if request.method == 'POST':
        tipo = TipoAtividade()
        tipo.descricao = request.POST['descricao']
        tipo.save()
        return HttpResponse('Tipo Inserido com sucesso')
    else:
        return HttpResponse('Falha na inserção de tipo')


