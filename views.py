from django.shortcuts import render
from .models import Vendas
def home(request):
    return render(request,'vendas/home.html')
def vendas(request):
    # salvar os dados da tela para o banco de dados
    nova_venda= Vendas()
    nova_venda.data = request.POST.get('data')
    nova_venda.produto = request.POST.get('produto')
    nova_venda.cliente = request.POST.get('cliente')
    nova_venda.save()
    # exibir as novas vendas em uma nova página
    vendas = {
        'vendas': Vendas.objects.all()
    }
    # retornar os dados para página de listagem de vendas.
    return render(request,'vendas/vendas.html',vendas)