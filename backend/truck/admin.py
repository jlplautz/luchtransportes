from django.contrib import admin

from .models import Truck, TruckFlue


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


@admin.register(TruckFlue)
class TruckFlueAdmin(admin.ModelAdmin):
    list_display = (
        'caminhao',
        'data',
        'flue_valor',
        'km_atual',
        'litros',
    )
    search_fields = ('caminhao',)
