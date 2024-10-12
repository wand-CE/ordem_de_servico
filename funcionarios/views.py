from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import View


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
