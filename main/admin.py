from django.contrib import admin
from .import models


class ClientAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'email', 'telefone', 'cpf')
    search_fields = ('nome_completo',)


admin.site.register(models.Client, ClientAdmin)
