from django.contrib import admin

from .models import Truck


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
