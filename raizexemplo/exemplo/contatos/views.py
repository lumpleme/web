from django.shortcuts import render, get_object_or_404
from contatos.models import Pessoa
from django.views.generic.base import View
from contatos.forms import ContatoModel2Form
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy

# Create your views here.

class ContatoListView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all().order_by('nome')
        
        contexto = { 'pessoas': pessoas } # Dicionário que será passado para o template
        # Valor da chave é o objeto com todas as pessoas
        
        return render(
            request,
            'contatos/listaContatos.html',
            contexto
        )

class ContatoCreateView(View):
    def get(self, request, *args, **kwargs):
        contexto = { 'formulario': ContatoModel2Form, }
        return render(request, "contatos/criaContato.html", contexto)

    def post(self, request, *args, **kwargs):
        formulario = ContatoModel2Form(request.POST)
        if formulario.is_valid():
            contato = formulario.save()
            contato.save()
            return HttpResponseRedirect(reverse_lazy("contatos:lista-contatos"))
        else:
            contexto = { 'formulario': formulario, 'mensagem': 'Erro ao salvar o contato!'}
            return render(request, "contatos/criaContato.html", contexto)
        
class ContatoUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        pessoa = Pessoa.objects.get(pk=pk)
        formulario = ContatoModel2Form(instance=pessoa)
        contexto = {'pessoa': formulario, 
                    'titulo': 'Atualiza Contato', }
        return render(request, 'contatos/atualizaContato.html', contexto)

    def post(self, request, pk, *args, **kwargs):
        pessoa = get_object_or_404(Pessoa, pk=pk)
        formulario = ContatoModel2Form(request.POST, instance=pessoa)
        if formulario.is_valid():
            pessoa = formulario.save() # atualiza uma pessoa com os dados do formulário
            pessoa.save() # salva uma pessoa no banco de dados
            return HttpResponseRedirect(reverse_lazy("contatos:lista-contatos"))
        else:
            contexto = {'pessoa': formulario, }
            return render(request, 'contatos/atualizaContato.html', contexto)

class ContatoDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        pessoa = Pessoa.objects.get(pk=pk)
        contexto = { 'pessoa': pessoa, }
        return render(request, 'contatos/apagaContato.html', contexto)
    
    def post(self, request, pk, *args, **kwargs):
        pessoa = Pessoa.objects.get(pk=pk)
        pessoa.delete()
        return HttpResponseRedirect(reverse_lazy("contatos:lista-contatos"))