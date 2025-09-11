from django.urls import path
from contatos import views

app_name = "contatos"

urlpatterns = [
    path('lista/', views.ContatoListView.as_view(),
    name='lista-contatos'),
    path('', views.ContatoListView.as_view(),
    name='home-contatos'),
    path('cria/', views.ContatoCreateView.as_view(),
    name='cria-contato'),
    path('atualiza/<int:pk>/', views.ContatoUpdateView.as_view(),
    name='atualiza-contato'),
    path('apaga/<int:pk>/', views.ContatoDeleteView.as_view(),
     name='apaga-contato'),
]