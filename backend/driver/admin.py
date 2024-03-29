from django.contrib import admin

from .models import Driver


@admin.register(Driver)
class FreightAdmin(admin.ModelAdmin):
    list_display = (
        'cpf',
        'cnh',
        'data_nasc',
        'telefone',
        'motorista',
    )
    search_fields = ('motorista',)
