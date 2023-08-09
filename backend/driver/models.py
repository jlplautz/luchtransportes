from django.db import models
from django.urls import reverse_lazy

from backend.accounts.models import User


class Driver(models.Model):
    motorista = models.OneToOneField(
        User,
        related_name='drivers',
        verbose_name='motorista',
        on_delete=models.DO_NOTHING,
        max_length=3,
        null=True,
    )
    cpf = models.CharField(max_length=11)
    cnh = models.CharField(max_length=11)
    data_nasc = models.DateField()
    telefone = models.CharField(max_length=15)
    rua = models.CharField(max_length=50, blank=True)
    bairro = models.CharField(max_length=30, blank=True)
    cidade = models.CharField(max_length=30, default='Curitiba')
    estado = models.CharField(max_length=30, default='Paraná')
    cep = models.CharField(max_length=10, blank=True)

    class Meta:
        ordering = ('motorista',)
        verbose_name = 'driver'
        verbose_name_plural = 'drivers'

    def __str__(self):
        return self.motorista.first_name

    def get_absolute_url(self):
        # return reverse_lazy('driver:driver_detail', kwargs={'pk': self.pk})
        return reverse_lazy('driver:driver_list')

    @property
    def verbose_name(self):
        return self._meta.verbose_name

    @property
    def verbose_name_plural(self):
        return self._meta.verbose_name_plural
