from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def home(request):
# processamento antes de mostrar a home page
    #return HttpResponse("Olá, mundo!")
    return render(request, 'meuapp/home.html')

def segundaPagina(request):
    return render(request, 'meuapp/segunda.html')
