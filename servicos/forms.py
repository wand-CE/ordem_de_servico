from django import forms
from django.forms import inlineformset_factory

from servicos.models import Cliente, Endereco, Telefone, TelefoneCliente, Produto, Marca, ItemOrdemServico, OrdemServico


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'


class TelefoneForm(forms.ModelForm):
    class Meta:
        model = Telefone
        fields = '__all__'


class ItemOrdemServicoForm(forms.ModelForm):
    class Meta:
        model = ItemOrdemServico
        fields = ['produto', 'quantidade']

    def __init__(self, *args, **kwargs):
        super(ItemOrdemServicoForm, self).__init__(*args, **kwargs)
        self.fields['produto'].queryset = Produto.objects.filter(quantidade__gt=0)


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'sexo', 'nascimento', 'email']
        widgets = {
            'nascimento': forms.DateInput(attrs={'type': 'date'}),
        }


telefone_formset = inlineformset_factory(
    Cliente,
    TelefoneCliente,
    form=TelefoneForm,
    extra=1,
    can_delete=True
)

ordem_de_servico_formset = inlineformset_factory(
    OrdemServico,
    ItemOrdemServico,
    form=ItemOrdemServicoForm,
    extra=1,
    can_delete=True
)


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nome']
