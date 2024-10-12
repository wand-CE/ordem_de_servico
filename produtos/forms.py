from django import forms

from produtos.models import Produto, Marca


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nome']
