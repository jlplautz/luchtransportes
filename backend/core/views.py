# core/views.py
# from chartkick.django import ColumnChart

from django.db.models import Count, Q, Sum
from django.shortcuts import render

from backend.freight.models import Freight


def index(request):
    template_name = 'core/index.html'
    return render(request, template_name)


def dashboard(request):
    template_name = 'core/dashboard.html'

    # fretes = Freight.objects.values_list('data', 'frete_adiant_valor')
    # saldo = [(data.isoformat(), float(vsf)) for data, vsf in fretes]
    # chart = ColumnChart(dict(saldo))
    # return render(request, template_name, {'chart': chart, 'dados': saldo})
    dataset = (
        Freight.objects.values('caminhao__placa')  # lockup
        .annotate(
            fadvlr_count=Sum('frete_adiant_valor'),
            fsdvlr_count=Sum('frete_saldo_valor'),
        )
        .order_by('caminhao')
    )

    categories = list()
    fadvlr_series_data = list()
    fsdvlr_series_data = list()

    for entry in dataset:
        categories.append(entry['caminhao__placa'])
        print(categories)
        # categories.append(entry['caminhao'])
        fadvlr_series_data.append(entry['fadvlr_count'])
        fsdvlr_series_data.append(entry['fsdvlr_count'])

    # categories = Freight.objects.select_related('caminhao'=categories)

    print(categories)

    data = {
        'chart': {'type': 'column'},
        'title': {'text': 'FRETES DE MAIO/23'},
        'xAxis': {'categories': categories},
        'series': [
            {
                'name': 'Adiantamento',
                'data': [
                    float(adiantamento) for adiantamento in fadvlr_series_data
                ],
            },
            {
                'name': 'Saldo',
                'data': [float(saldo) for saldo in fsdvlr_series_data],
            },
        ],
    }

    # totalset = (
    #     Freight.objects.all().(Sum('frete_adiant_valor'))
    # )
    return render(request, template_name, {'data': data})
