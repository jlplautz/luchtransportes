from django.db import models
from django.urls import reverse_lazy


class Driver(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=20, blank=True)
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
        ordering = ('nome',)
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        # return reverse_lazy('driver:driver_detail', kwargs={'pk': self.pk})
        return reverse_lazy('driver:driver_list')

    @property
    def verbose_name(self):
        return self._meta.verbose_name

    @property
    def verbose_name_plural(self):
        return self._meta.verbose_name_plural
