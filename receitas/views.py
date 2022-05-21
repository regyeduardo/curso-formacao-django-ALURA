from django.shortcuts import render, get_object_or_404
from .models import Receita


def index(request):
    receitas = Receita.objects.all()

    dados = {"receitas": receitas}

    return render(request, "index.html", dados)


def receita(request, identification):
    specific_receita = get_object_or_404(Receita, id=identification)

    data = {"receita": specific_receita}
    return render(request, "receita.html", data)
