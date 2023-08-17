from django.contrib import admin

from .models import Truck, TruckFlue, TruckRepair


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
        'descricao',
    )
    search_fields = ('caminhao',)


@admin.register(TruckRepair)
class TruckRepairAdmin(admin.ModelAdmin):
    list_display = (
        'caminhao',
        'data',
        'repair_valor',
        'descricao',
        'cidade',
    )
    search_fields = ('caminhao',)
