from django.shortcuts import render, get_object_or_404
from .models import Receita


def index(request):
    receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)

    dados = {"receitas": receitas}

    return render(request, "index.html", dados)


def receita(request, identification):
    specific_receita = get_object_or_404(Receita, id=identification)

    data = {"receita": specific_receita}
    return render(request, "receita.html", data)

def buscar(request):
    lista_receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']

        if nome_a_buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'buscar.html', dados)
