from django.contrib import admin

from .models import Truck, TruckFees


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = (
        'marca',
        'modelo',
        'ano_fab',
        'placa',
        # 'chassis',
    )
    search_fields = ('marca',)


@admin.register(TruckFees)
class TruckFeesAdmin(admin.ModelAdmin):
    list_display = (
        'contrato',
        'cod_operacao',
        'data',
        'caminhao',
        'valor_adiant_fixo',
        'valor_saldo_fixo',
        'valor_desc_fixo',
        'status_fixo',
    )
    search_fields = ('caminhao',)
