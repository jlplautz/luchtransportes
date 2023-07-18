from django.contrib import admin

from .models import Freight, FreightFee


@admin.register(Freight)
class FreightAdmin(admin.ModelAdmin):
    list_display = (
        'data',
        'caminhao',
        'motorista',
        'origem',
        'destino',
        'distancia',
    )
    search_fields = ('data',)


@admin.register(FreightFee)
class FreightFeeAdmin(admin.ModelAdmin):
    list_display = (
        'data',
        'caminhao',
        'valor_adiant_fixo',
        'valor_saldo_fixo',
        'valor_desc_fixo',
        'frete_status',
    )
    search_fields = ('data',)
