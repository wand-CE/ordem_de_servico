from django import forms
from django.forms import inlineformset_factory

from ordens_de_servico.models import ItemOrdemServico, OrdemServico
from produtos.models import Produto


class ItemOrdemServicoForm(forms.ModelForm):
    class Meta:
        model = ItemOrdemServico
        fields = ['produto', 'quantidade']

    def __init__(self, *args, **kwargs):
        super(ItemOrdemServicoForm, self).__init__(*args, **kwargs)
        self.fields['produto'].queryset = Produto.objects.filter(quantidade__gt=0)


ordem_de_servico_formset = inlineformset_factory(
    OrdemServico,
    ItemOrdemServico,
    form=ItemOrdemServicoForm,
    extra=1,
    can_delete=True
)
