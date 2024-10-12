from django import forms
from django.forms import inlineformset_factory

from clientes.models import Cliente, TelefoneCliente


class TelefoneClienteForm(forms.ModelForm):
    class Meta:
        model = TelefoneCliente
        fields = '__all__'


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'sexo', 'nascimento', 'email']
        widgets = {
            'nascimento': forms.DateInput(attrs={'type': 'date'}),
        }


telefone_cliente_formset = inlineformset_factory(
    Cliente,
    TelefoneCliente,
    form=TelefoneClienteForm,
    extra=1,
    can_delete=True,
)
