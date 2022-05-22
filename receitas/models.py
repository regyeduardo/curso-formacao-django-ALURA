from django.db import models
from pessoas.models import Pessoa

class Receita(models.Model):
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    date_receita = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)
    pessoa = models.ForeignKey(Pessoa, default='', on_delete=models.CASCADE)
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    publicada = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nome_receita