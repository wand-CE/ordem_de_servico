from django.contrib import admin

from empresas.models import Empresa, TelefoneEmpresa, EnderecoEmpresa


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    class Meta:
        model = Empresa
        fields = '__all__'


@admin.register(TelefoneEmpresa)
class TelefoneEmpresaAdmin(admin.ModelAdmin):
    class Meta:
        model = TelefoneEmpresa
        fields = '__all__'


@admin.register(EnderecoEmpresa)
class EnderecoEmpresaAdmin(admin.ModelAdmin):
    class Meta:
        model = EnderecoEmpresa
        fields = '__all__'
