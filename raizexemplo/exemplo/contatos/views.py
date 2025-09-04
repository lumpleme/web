from django.shortcuts import render
from contatos.models import Pessoa
from django.views.generic.base import View

# Create your views here.

class ContatoListView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        
        contexto = { 'pessoas': pessoas } # Dicionário que será passado para o template
        # Valor da chave é o objeto com todas as pessoas
        
        return render(
            request,
            'contatos/listaContatos.html',
            contexto
        )