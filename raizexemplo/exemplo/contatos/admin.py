from django.contrib import admin
from .models import Pessoa

# Register your models here.

admin.site.register(Pessoa) # Possibilita gerenciar o modelo Pessoa na interface admin do Django
