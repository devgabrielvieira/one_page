from django.db import models


class Client(models.Model):
    nome_completo = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.nome_completo
