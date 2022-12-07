from django.contrib import admin

from Colaborador.models import Colaborador

class Colaboradors(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf','sexo', 'endereco','telefone', 'email', 'data_nascimento', 'matricula', 'data_admissao','cargo')
    list_display_links = ('id','nome')
    search_fields = ('nome',)

admin.site.register(Colaborador, Colaboradors)