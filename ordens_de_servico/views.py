from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from funcionarios.models import Funcionario
from ordens_de_servico.forms import ItemOrdemServicoForm, ordem_de_servico_formset
from ordens_de_servico.models import OrdemServico, ItemOrdemServico


class CadastrarOrdem(LoginRequiredMixin, CreateView):
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

                # Calcula o valor total do item:
                item_instance.valor_total = item_instance.produto.preco * item_instance.quantidade
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


class EditarOrdem(LoginRequiredMixin, UpdateView):
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

                # Calcula o valor total do item:
                item_instance.valor_total = item_instance.produto.preco * item_instance.quantidade
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


class ListarOrdens(LoginRequiredMixin, ListView):
    model = OrdemServico
    template_name = "ordens_servico/listar.html"
    context_object_name = "ordens"
    queryset = OrdemServico.objects.all()


class ExcluirOrdem(LoginRequiredMixin, DeleteView):
    model = OrdemServico
    template_name = 'ordens_servico/excluir.html'
    success_url = reverse_lazy('listar_ordens')
    context_object_name = 'ordem'
