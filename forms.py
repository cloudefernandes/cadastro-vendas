from .models import Produto, Vendas
from django import forms

class VendasForm(forms.Form):
    class Meta:
        model = Vendas
        fields = '__all__'
    produto = forms.ModelChoiceField(
        queryset=Produto.objects.all(),
    )