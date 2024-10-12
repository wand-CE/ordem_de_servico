from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from clientes.forms import ClienteForm, telefone_cliente_formset
from clientes.models import Cliente, TelefoneCliente
from base_app.forms import EnderecoForm, TelefoneForm


class ListarClienteView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "cliente/listar_clientes.html"
    context_object_name = "clientes"
    queryset = Cliente.objects.all()


class CadastroClienteView(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = 'cliente/cadastrarCliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('listar_clientes')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx['endereco_form'] = EnderecoForm(self.request.POST or None)
        ctx['telefone_cliente_formset'] = telefone_cliente_formset(self.request.POST or None, instance=self.object)

        return ctx

    def form_valid(self, form):
        endereco_form = EnderecoForm(self.request.POST)
        form_telefone_factory = inlineformset_factory(Cliente, TelefoneCliente, form=TelefoneForm)
        form_telefone = form_telefone_factory(self.request.POST)

        if endereco_form.is_valid() and form_telefone.is_valid():
            cliente = form.save(commit=False)

            endereco = endereco_form.save()
            cliente.endereco = endereco

            cliente.save()

            form_telefone.instance = cliente
            form_telefone.save()

            return super().form_valid(form)

        return super().form_invalid(form)

    def form_invalid(self, form):
        print(self.request.POST)
        return super().form_invalid(form)


class EditarClienteView(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = 'cliente/editar_cliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('listar_clientes')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        endereco = self.object.endereco

        ctx['endereco_form'] = EnderecoForm(self.request.POST or None, instance=endereco)
        ctx['telefone_cliente_formset'] = telefone_cliente_formset(self.request.POST or None, instance=self.object)

        return ctx

    def form_valid(self, form):
        endereco_form = EnderecoForm(self.request.POST)
        form_telefone_factory = inlineformset_factory(Cliente, TelefoneCliente, form=TelefoneForm)
        form_telefone = form_telefone_factory(self.request.POST, instance=self.object)

        if endereco_form.is_valid() and form_telefone.is_valid():
            cliente = form.save(commit=False)

            endereco = endereco_form.save()
            cliente.endereco = endereco

            cliente.save()

            form_telefone.instance = cliente
            form_telefone.save()

            return super().form_valid(form)

        return super().form_invalid(form)


class ExcluirClienteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'cliente/excluir_cliente.html'
    success_url = reverse_lazy('listar_clientes')
