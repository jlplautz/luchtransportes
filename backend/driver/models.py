from django.db import models
from django.urls import reverse_lazy

from backend.accounts.models import User


class Driver(models.Model):
    cpf = models.CharField(max_length=11)
    cnh = models.CharField(max_length=11)
    data_nasc = models.DateField()
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    cep = models.CharField(max_length=10)
    nome = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.cpf

    def get_absolute_url(self):
        return reverse_lazy('driver_detail', kwargs={'pk': self.pk})
