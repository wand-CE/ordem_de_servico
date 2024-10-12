# from django.contrib import admin
#
# from gerenciador_base_app.models import Empresa, Endereco, TelefoneEmpresa, Fornecedor, TelefoneFornecedor, Funcionario, \
#     Escolaridade, Cargo, Telefone, TelefoneFuncionario, Produto
#
#
# class TelefoneInline(admin.TabularInline):
#     model = TelefoneEmpresa
#     extra = 1  # Número de telefones em branco a serem exibidos
#
#
# class TelefoneFornecedorInline(admin.TabularInline):
#     model = TelefoneFornecedor
#     extra = 1  # Número de telefones em branco a serem exibidos
#
#
# class TelefoneFuncionarioInline(admin.TabularInline):
#     model = TelefoneFuncionario
#     extra = 1  # Número de telefones em branco a serem exibidos
#
#
# @admin.register(Empresa)
# class EmpresaAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'cnpj', 'get_endereco', 'get_telefones')
#
#     inlines = [TelefoneInline]
#
#     def get_endereco(self, obj):
#         return obj.endereco.endereco_completo()
#
#     get_endereco.short_description = 'Endereço'
#
#     def get_telefones(self, obj):
#         return ", ".join([str(telefone) for telefone in obj.telefones.all()])
#
#     get_telefones.short_description = 'Telefones'
#
#
# @admin.register(Fornecedor)
# class FornecedorAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'cnpj')
#
#     inlines = [TelefoneFornecedorInline]
#
#     def get_endereco(self, obj):
#         return obj.endereco.endereco_completo()
#
#     get_endereco.short_description = 'Endereço'
#
#     def get_telefones(self, obj):
#         return ", ".join([str(telefone) for telefone in obj.telefones.all()])
#
#     get_telefones.short_description = 'Telefones'
#
#
# @admin.register(Funcionario)
# class FuncionarioAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'cpf')
#
#     inlines = [TelefoneFuncionarioInline]
#
#
# admin.site.register(Escolaridade)
# admin.site.register(Cargo)
# admin.site.register(Endereco)
# admin.site.register(Telefone)
# admin.site.register(Produto)
