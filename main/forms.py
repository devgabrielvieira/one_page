from django import forms
from . import models


class ClientForm(forms.ModelForm):

    class Meta:
        model = models.Client
        fields = ['nome_completo', 'email', 'telefone', 'cpf']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'rows': 3}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'rows': 3}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'nome_completo': 'Nome completo',
            'email': 'Email',
            'telefone': 'Telefone',
            'cpf': 'CPF',
        }
