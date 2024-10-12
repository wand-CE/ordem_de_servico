from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from produtos.forms import ProdutoForm, MarcaForm
from produtos.models import Produto


class CadastrarProduto(LoginRequiredMixin, CreateView):
    model = Produto
    template_name = 'produtos/criar.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('listar_produtos')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['marca_form'] = MarcaForm()
        return ctx


class EditarProduto(LoginRequiredMixin, UpdateView):
    model = Produto
    template_name = 'produtos/editar.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('listar_produtos')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['marca_form'] = MarcaForm()
        return ctx


class ListarProdutoView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = "produtos/listar.html"
    context_object_name = "produtos"
    queryset = Produto.objects.all()


class CadastrarMarca(LoginRequiredMixin, CreateView):
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


class ExcluirProduto(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'produtos/excluir.html'
    success_url = reverse_lazy('listar_produtos')
