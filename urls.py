from django.urls import path
from app_cad_vendas import views

urlpatterns = [
   # rota, view reponsavel, nome de referência
   # vendas.com
   path('',views.home,name='home'),
   # vendas.com/vendas
   path('vendas/',views.vendas, name='vendas'),
   # vendas.com/listavendas
   path('listavendas/',views.listavendas, name='listavendas'),
   # vendas.com/cadclientes
   path('cadclientes/',views.cadclientes, name='cadclientes'),
   # vendas.com/clientes
   path('clientes/',views.clientes, name='clientes'),
   # vendas.com/listaclientes
   path('listaclientes/',views.listaclientes, name='listaclientes'),
]
