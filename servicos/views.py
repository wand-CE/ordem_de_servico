import json

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView, View

from servicos.forms import ClienteForm, EnderecoForm, telefone_formset, TelefoneForm, ProdutoForm, MarcaForm, \
    ItemOrdemServicoForm, ordem_de_servico_formset
from servicos.models import Cliente, Telefone, TelefoneCliente, Produto, OrdemServico, ItemOrdemServico, Funcionario


class CadastroClienteView(CreateView):
    model = Cliente
    template_name = 'cliente/cadastrarCliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('listar_clientes')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx['endereco_form'] = EnderecoForm(self.request.POST or None)
        ctx['telefone_formset'] = telefone_formset(self.request.POST or None, instance=self.object)

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


class ListarClienteView(ListView):
    model = Cliente
    template_name = "cliente/listar_clientes.html"
    context_object_name = "clientes"
    queryset = Cliente.objects.all()


class EditarClienteView(UpdateView):
    model = Cliente
    template_name = 'cliente/editar_cliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('listar_clientes')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        endereco = self.object.endereco

        ctx['endereco_form'] = EnderecoForm(self.request.POST or None, instance=endereco)
        ctx['telefone_formset'] = telefone_formset(self.request.POST or None, instance=self.object)

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


class ExcluirClienteView(DeleteView):
    model = Cliente
    template_name = 'cliente/excluir_cliente.html'
    success_url = reverse_lazy('listar_clientes')


class HomePageView(TemplateView):
    template_name = 'home.html'


class LogarFuncionario(LoginView):
    template_name = 'funcionarios/login.html'
    success_url = reverse_lazy('home')


class DeslogarFuncionarioView(View):
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            messages.success(self.request, f'Usuário Deslogado!')
        return redirect(self.success_url)


class CadastrarProduto(CreateView):
    model = Produto
    template_name = 'produtos/criar.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('listar_produtos')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['marca_form'] = MarcaForm()
        return ctx


class EditarProduto(UpdateView):
    model = Produto
    template_name = 'produtos/editar.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('listar_produtos')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['marca_form'] = MarcaForm()
        return ctx


class ListarProdutoView(ListView):
    model = Produto
    template_name = "produtos/listar.html"
    context_object_name = "produtos"
    queryset = Produto.objects.all()


class CadastrarMarca(CreateView):
    def post(self, request, *args, **kwargs):
        form = MarcaForm(request.POST)
        if form.is_valid():
            marca = form.save()
            return JsonResponse(
                {'success': True, 'message': 'Marca cadastrada com sucesso!', 'id': marca.id, 'nome': marca.nome})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

    def get(self, request, *args, **kwargs):
        return JsonResponse({'success': False, 'message': 'Método não permitido.'})


class ExcluirProduto(DeleteView):
    model = Produto
    template_name = 'produtos/excluir.html'
    success_url = reverse_lazy('listar_produtos')


class CadastrarOrdem(CreateView):
    model = OrdemServico
    template_name = "ordens_servico/criar.html"
    fields = ['cliente', 'descricao', ]
    success_url = reverse_lazy('listar_ordens')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['item_formset'] = ordem_de_servico_formset(self.request.POST or None, instance=self.object)

        return ctx

    def form_valid(self, form):
        form_produto_factory = inlineformset_factory(OrdemServico, ItemOrdemServico, form=ItemOrdemServicoForm)
        form_produto = form_produto_factory(self.request.POST, instance=self.object)

        current_user = self.request.user
        funcionario = Funcionario.objects.filter(user=current_user) or None

        if form_produto.is_valid() and funcionario:
            ordem = form.save(commit=False)
            ordem.tecnico = funcionario.first()  # Atribui o técnico
            ordem.valor_total = 0
            ordem.save()  # Salva a ordem de serviço

            valor_total = 0

            for item in form_produto:
                # Cria uma nova instância de ItemOrdemServico
                item_instance = ItemOrdemServico()
                item_instance.produto = item.cleaned_data.get('produto')  # Obtém o produto do formulário
                item_instance.quantidade = item.cleaned_data.get('quantidade')  # Obtém a quantidade
                item_instance.valor_total = item_instance.produto.preco * item_instance.quantidade  # Calcula o valor total do item
                item_instance.ordem_servico = ordem  # Associa o item à ordem de serviço

                # Atualiza a quantidade do produto
                produto = item_instance.produto
                if produto.quantidade >= item_instance.quantidade:
                    produto.quantidade -= item_instance.quantidade  # Diminui a quantidade no estoque
                    produto.save()  # Salva a atualização do produto
                    item_instance.save()  # Salva o item da ordem de serviço
                    valor_total += item_instance.valor_total  # Acumula o valor total
                else:
                    form_produto.add_error('quantidade',
                                           f'Quantidade insuficiente em estoque para o produto {produto.nome}')

            ordem.valor_total = valor_total  # Atualiza o valor total da ordem
            ordem.save()  # Salva a ordem de serviço novamente com o valor total

            return super().form_valid(form)

        return self.form_invalid(form)


class EditarOrdem(UpdateView):
    model = OrdemServico
    template_name = "ordens_servico/editar.html"
    fields = ['cliente', 'descricao', ]
    success_url = reverse_lazy('listar_ordens')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.POST:
            ctx['item_formset'] = ordem_de_servico_formset(self.request.POST, instance=self.object)
        else:
            ctx['item_formset'] = ordem_de_servico_formset(instance=self.object)

        return ctx

    def form_valid(self, form):
        form_produto_factory = inlineformset_factory(OrdemServico, ItemOrdemServico, form=ItemOrdemServicoForm)
        form_produto = form_produto_factory(self.request.POST, instance=self.object)

        current_user = self.request.user
        funcionario = Funcionario.objects.filter(user=current_user) or None

        if form_produto.is_valid() and funcionario:
            ordem = form.save(commit=False)
            ordem.tecnico = funcionario.first()  # Atribui o técnico
            ordem.valor_total = 0
            ordem.save()  # Salva a ordem de serviço

            valor_total = 0

            for item in form_produto:
                # Cria uma nova instância de ItemOrdemServico
                item_instance = ItemOrdemServico()
                item_instance.produto = item.cleaned_data.get('produto')  # Obtém o produto do formulário
                item_instance.quantidade = item.cleaned_data.get('quantidade')  # Obtém a quantidade
                item_instance.valor_total = item_instance.produto.preco * item_instance.quantidade  # Calcula o valor total do item
                item_instance.ordem_servico = ordem  # Associa o item à ordem de serviço

                # Atualiza a quantidade do produto
                produto = item_instance.produto
                if produto.quantidade >= item_instance.quantidade:
                    produto.quantidade -= item_instance.quantidade  # Diminui a quantidade no estoque
                    produto.save()  # Salva a atualização do produto
                    item_instance.save()  # Salva o item da ordem de serviço
                    valor_total += item_instance.valor_total  # Acumula o valor total
                else:
                    form_produto.add_error('quantidade',
                                           f'Quantidade insuficiente em estoque para o produto {produto.nome}')

            ordem.valor_total = valor_total  # Atualiza o valor total da ordem
            ordem.save()  # Salva a ordem de serviço novamente com o valor total

            return super().form_valid(form)

        return super().form_invalid(form)


class ListarOrdens(ListView):
    model = OrdemServico
    template_name = "ordens_servico/listar.html"
    context_object_name = "ordens"
    queryset = OrdemServico.objects.all()


class ExcluirOrdem(DeleteView):
    model = OrdemServico
    template_name = 'ordens_servico/excluir.html'
    success_url = reverse_lazy('listar_ordens')
    context_object_name = 'ordem'
