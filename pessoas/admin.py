from django.contrib import admin
from .models import Pessoa

class PessoaAdminPanel(admin.ModelAdmin):
    list_display = ('nome', 'email')
    list_display_links = ('nome', 'email')

admin.site.register(Pessoa, PessoaAdminPanel)