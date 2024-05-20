from django.shortcuts import render
from .models import Clientes, Vendas
from .forms import VendasForm



def home(request):
    form = VendasForm()

    context={
        "form": form}
    return render(request,'vendas/home.html')
def cadclientes(request):
    return render(request,'vendas/cadclientes.html')
def vendas(request):
    # salvar os dados da tela para o banco de dados
    nova_venda= Vendas()
    nova_venda.data = request.POST.get('data')
    nova_venda.produto = request.POST.get('produto')
    nova_venda.valor = request.POST.get('valor')
    nova_venda.cliente = request.POST.get('cliente')
    nova_venda.save()
    # exibir as novas vendas em uma nova página
    vendas = {
        'vendas': Vendas.objects.all()
    }
    # retornar os dados para página de listagem de vendas.
    return render(request,'vendas/vendas.html',vendas)

def listavendas(request):
    # exibir as novas vendas em uma nova página
    listavendas = {
        'listavendas': Vendas.objects.all()
    }
    # retornar os dados para página de listagem de vendas.
    return render(request,'vendas/listavendas.html',listavendas)

def clientes(request):
    # salvar os dados da tela para o banco de dados
    novo_cliente= Clientes()
    novo_cliente.nome = request.POST.get('nome')
    novo_cliente.email = request.POST.get('email')
    novo_cliente.telefone = request.POST.get('telefone')
    novo_cliente.save()
    # exibir os novos clientes em uma nova página
    clientes = {
        'clientes': Clientes.objects.all()
    }
    # retornar os dados para página de listagem de clientes.
    return render(request,'vendas/clientes.html',clientes)

def listaclientes(request):
    # exibir as novas vendas em uma nova página
    listaclientes = {
        'listaclientes': Clientes.objects.all()
    }
    # retornar os dados para página de listagem de vendas.
    return render(request,'vendas/listaclientes.html',listaclientes)

