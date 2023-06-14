# core/views.py
# from chartkick.django import ColumnChart

from chartkick.django import LineChart
from django.db.models import Count, Q
from django.shortcuts import render

from backend.freight.models import Freight


def index(request):
    template_name = 'core/index.html'
    return render(request, template_name)


def dashboard(request):
    template_name = 'core/dashboard.html'

    fretes = Freight.objects.values_list('data', 'frete_adiant_valor')

    saldo = [(data.isoformat(), float(vsf)) for data, vsf in fretes]

    chart = LineChart(dict(saldo))

    return render(request, template_name, {'chart': chart, 'dados': saldo})
