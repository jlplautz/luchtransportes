from django.contrib import admin

from .models import Freight


@admin.register(Freight)
class FreightAdmin(admin.ModelAdmin):
    list_display = (
        'data',
        'caminhao',
        'motorista',
        'origem',
        'destino',
    )
    search_fields = ('data',)
