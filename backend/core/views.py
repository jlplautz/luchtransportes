from datetime import datetime

from django.db.models import Sum
from django.shortcuts import render

from backend.freight.models import Freight, FreightFee


def index(request):
    template_name = 'core/index.html'
    return render(request, template_name)


def dashboard(request):
    template_name = 'core/dashboard.html'

    # mostra o faturamento nos ultimos 12 meses
    frete = Freight.objects.all()
    fretefee = FreightFee.objects.all()

    meses = [
        'jan',
        'fev',
        'mar',
        'abr',
        'mai',
        'jun',
        'jul',
        'ago',
        'set',
        'out',
        'nov',
        'dez',
    ]
    data = []
    datafee = []
    labels = []
    cont = 0
    mes = datetime.now().month + 1
    ano = datetime.now().year

    for i in range(12):
        # pois no python começamos sempre com 0
        mes -= 1
        # relatorio dos ultimos 12 meses. Do mes atual ate o ano anterior
        if mes == 0:
            mes = 12
            ano -= 1

        y = sum(
            [
                i.frete_adiant_valor
                for i in frete
                if i.data.month == mes and i.data.year == ano
            ]
        )

        y += sum(
            [
                i.frete_saldo_valor
                for i in frete
                if i.data.month == mes and i.data.year == ano
            ]
        )

        y1 = sum(
            [
                i.valor_adiant_fixo
                for i in fretefee
                if i.data.month == mes and i.data.year == ano
            ]
        )
        y1 += sum(
            [
                i.valor_saldo_fixo
                for i in fretefee
                if i.data.month == mes and i.data.year == ano
            ]
        )

        labels.append(meses[mes - 1])
        data.append(y)
        datafee.append(y1)
        cont += 1

    fretetotal = {
        'chart': {'type': 'column'},
        'title': {'text': 'Fretes - Total'},
        'xAxis': {'categories': labels[::-1]},
        'series': [
            {
                'name': 'Adiantamento + Saldo',
                'data': [float(total) for total in data[::-1]],
            },
        ],
    }

    fretefeetotal = {
        'chart': {'type': 'column'},
        'title': {'text': 'Fretes Fixos - Total'},
        'xAxis': {'categories': labels[::-1]},
        'series': [
            {
                'name': 'Adiantamento + Saldo',
                'data': [float(total) for total in datafee[::-1]],
            },
        ],
    }

    # ********************************************************************

    dataset = (
        frete.values('caminhao__placa')
        .filter(data__month=5)  # lockup
        .annotate(
            fadvlr_count=Sum('frete_adiant_valor'),
            fsdvlr_count=Sum('frete_saldo_valor'),
            distancia_count=Sum('distancia'),
        )
        .order_by('caminhao')
    )

    datasetfixo = (
        fretefee.values('caminhao__placa')  # lockup
        .filter(data__month=5)
        .annotate(
            adiantfixo_count=Sum('valor_adiant_fixo'),
            saldofixo_count=Sum('valor_saldo_fixo'),
            descfixo_count=Sum('valor_desc_fixo'),
        )
        .order_by('caminhao')
    )

    categories = list()
    fadvlr_series_data = list()
    fsdvlr_series_data = list()
    distancia_series_data = list()
    adiantfixo_series_data = list()
    saldofixo_series_data = list()
    descfixo_series_data = list()

    for entry in dataset:
        categories.append(entry['caminhao__placa'])
        fadvlr_series_data.append(entry['fadvlr_count'])
        fsdvlr_series_data.append(entry['fsdvlr_count'])
        distancia_series_data.append(entry['distancia_count'])

    for entry in datasetfixo:
        categories.append(entry['caminhao__placa'])
        adiantfixo_series_data.append(entry['adiantfixo_count'])
        saldofixo_series_data.append(entry['saldofixo_count'])
        descfixo_series_data.append(entry['descfixo_count'])

    data = {
        'chart': {'type': 'column'},
        'title': {'text': 'FRETES DE MAIO/23'},
        'xAxis': {'categories': categories},
        # 'xAxis': {'categories':  labels[::-1]},
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
            {
                'name': 'KMs_Rodado',
                'data': [float(kms) for kms in distancia_series_data],
            },
        ],
    }

    datafixo = {
        'chart': {'type': 'column'},
        'title': {'text': 'FRETES-FIXO DE MAIO/23'},
        'xAxis': {'categories': categories},
        'series': [
            {
                'name': 'Adiantamento',
                'data': [
                    float(adiantamento)
                    for adiantamento in adiantfixo_series_data
                ],
            },
            {
                'name': 'Saldo',
                'data': [float(saldo) for saldo in saldofixo_series_data],
            },
            {
                'name': 'Desconto',
                'data': [float(desc) for desc in descfixo_series_data],
            },
        ],
    }

    return render(
        request,
        template_name,
        {
            'data': data,
            'datafixo': datafixo,
            'fretetotal': fretetotal,
            'fretefeetotal': fretefeetotal,
        },
    )
