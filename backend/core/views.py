from datetime import datetime

from django.db.models import Sum
from django.shortcuts import render

from backend.freight.models import Freight, FreightFee
from backend.truck.models import TruckFlue


def index(request):
    template_name = 'core/index.html'
    return render(request, template_name)


def dashboard(request):
    template_name = 'core/dashboard.html'

    # mostra o faturamento nos ultimos 12 meses
    frete = Freight.objects.all()
    fretefee = FreightFee.objects.all()
    truckflue = TruckFlue.objects.all()

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
    dataflue = []
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
                i.frete_adiant_valor + i.frete_saldo_valor
                for i in frete
                if i.data.month == mes and i.data.year == ano
            ]
        )

        y1 = sum(
            [
                i.valor_adiant_fixo + i.valor_saldo_fixo
                for i in fretefee
                if i.data.month == mes and i.data.year == ano
            ]
        )

        y2 = sum(
            [
                i.flue_valor
                for i in truckflue
                if i.data.month == mes and i.data.year == ano
            ]
        )

        labels.append(meses[mes - 1])
        data.append(y)
        datafee.append(y1)
        dataflue.append(y2)
        cont += 1

    fretetotal = {
        'chart': {'type': 'column'},
        'title': {'text': 'FRETES - TOTAL'},
        'xAxis': {'categories': labels[::-1]},
        'series': [
            {
                'name': 'Fretes',
                'data': [float(total) for total in data[::-1]],
            },
            {
                'name': 'Fretes Fixos',
                'data': [float(total) for total in datafee[::-1]],
            },
            {
                'name': 'Combustível',
                'data': [float(total) for total in dataflue[::-1]],
            },
        ],
    }

    fretefeetotal = {
        'chart': {'type': 'column'},
        'title': {'text': 'FRETES FIXOS - TOTAL'},
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
        'title': {'text': 'FRETES - MAIO/23'},
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
        'title': {'text': 'FRETES-FIXO - MAIO/23'},
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

    # ********************************************************************

    datasetJun23 = (
        frete.values('caminhao__placa')
        .filter(data__month=6)  # lockup
        .annotate(
            fadvlrJun23_count=Sum('frete_adiant_valor'),
            fsdvlrJun23_count=Sum('frete_saldo_valor'),
            distanciaJun23_count=Sum('distancia'),
        )
        .order_by('caminhao')
    )

    datasetfixoJun23 = (
        fretefee.values('caminhao__placa')  # lockup
        .filter(data__month=6)
        .annotate(
            adiantfixoJun23_count=Sum('valor_adiant_fixo'),
            saldofixoJun23_count=Sum('valor_saldo_fixo'),
            descfixoJun23_count=Sum('valor_desc_fixo'),
        )
        .order_by('caminhao')
    )

    categories = list()
    fadvlrJun23_series_data = list()
    fsdvlrJun23_series_data = list()
    distanciaJun23_series_data = list()
    adiantfixoJun23_series_data = list()
    saldofixoJun23_series_data = list()
    descfixoJun23_series_data = list()

    for entry in datasetJun23:
        categories.append(entry['caminhao__placa'])
        fadvlrJun23_series_data.append(entry['fadvlrJun23_count'])
        fsdvlrJun23_series_data.append(entry['fsdvlrJun23_count'])
        distanciaJun23_series_data.append(entry['distanciaJun23_count'])

    for entry in datasetfixoJun23:
        categories.append(entry['caminhao__placa'])
        adiantfixoJun23_series_data.append(entry['adiantfixoJun23_count'])
        saldofixoJun23_series_data.append(entry['saldofixoJun23_count'])
        descfixoJun23_series_data.append(entry['descfixoJun23_count'])

    dataJun23 = {
        'chart': {'type': 'column'},
        'title': {'text': 'FRETES - JUNHO/23'},
        'xAxis': {'categories': categories},
        # 'xAxis': {'categories':  labels[::-1]},
        'series': [
            {
                'name': 'Adiantamento',
                'data': [
                    float(adiantamento)
                    for adiantamento in fadvlrJun23_series_data
                ],
            },
            {
                'name': 'Saldo',
                'data': [float(saldo) for saldo in fsdvlrJun23_series_data],
            },
            {
                'name': 'KMs_Rodado',
                'data': [float(kms) for kms in distanciaJun23_series_data],
            },
        ],
    }

    datafixoJun23 = {
        'chart': {'type': 'column'},
        'title': {'text': 'FRETES-FIXO - JUNHO/23'},
        'xAxis': {'categories': categories},
        'series': [
            {
                'name': 'Adiantamento',
                'data': [
                    float(adiantamento)
                    for adiantamento in adiantfixoJun23_series_data
                ],
            },
            {
                'name': 'Saldo',
                'data': [float(saldo) for saldo in saldofixoJun23_series_data],
            },
            {
                'name': 'Desconto',
                'data': [float(desc) for desc in descfixoJun23_series_data],
            },
        ],
    }

    # Jul23****************************************************************

    datasetJul23 = (
        frete.values('caminhao__placa')
        .filter(data__month=7)  # lockup
        .annotate(
            fadvlrJul23_count=Sum('frete_adiant_valor'),
            fsdvlrJul23_count=Sum('frete_saldo_valor'),
            distanciaJul23_count=Sum('distancia'),
        )
        .order_by('caminhao')
    )

    datasetfixoJul23 = (
        fretefee.values('caminhao__placa')  # lockup
        .filter(data__month=7)
        .annotate(
            adiantfixoJul23_count=Sum('valor_adiant_fixo'),
            saldofixoJul23_count=Sum('valor_saldo_fixo'),
            descfixoJul23_count=Sum('valor_desc_fixo'),
        )
        .order_by('caminhao')
    )

    categories = list()
    fadvlrJul23_series_data = list()
    fsdvlrJul23_series_data = list()
    distanciaJul23_series_data = list()
    adiantfixoJul23_series_data = list()
    saldofixoJul23_series_data = list()
    descfixoJul23_series_data = list()

    for entry in datasetJul23:
        categories.append(entry['caminhao__placa'])
        fadvlrJul23_series_data.append(entry['fadvlrJul23_count'])
        fsdvlrJul23_series_data.append(entry['fsdvlrJul23_count'])
        distanciaJul23_series_data.append(entry['distanciaJul23_count'])

    for entry in datasetfixoJul23:
        categories.append(entry['caminhao__placa'])
        adiantfixoJul23_series_data.append(entry['adiantfixoJul23_count'])
        saldofixoJul23_series_data.append(entry['saldofixoJul23_count'])
        descfixoJul23_series_data.append(entry['descfixoJul23_count'])

    dataJul23 = {
        'chart': {'type': 'column'},
        'title': {'text': 'FRETES - JULHO/23'},
        'xAxis': {'categories': categories},
        # 'xAxis': {'categories':  labels[::-1]},
        'series': [
            {
                'name': 'Adiantamento',
                'data': [
                    float(adiantamento)
                    for adiantamento in fadvlrJul23_series_data
                ],
            },
            {
                'name': 'Saldo',
                'data': [float(saldo) for saldo in fsdvlrJul23_series_data],
            },
            {
                'name': 'KMs_Rodado',
                'data': [float(kms) for kms in distanciaJul23_series_data],
            },
        ],
    }

    datafixoJul23 = {
        'chart': {'type': 'column'},
        'title': {'text': 'FRETES-FIXO - JULHO/23'},
        'xAxis': {'categories': categories},
        'series': [
            {
                'name': 'Adiantamento',
                'data': [
                    float(adiantamento)
                    for adiantamento in adiantfixoJul23_series_data
                ],
            },
            {
                'name': 'Saldo',
                'data': [float(saldo) for saldo in saldofixoJul23_series_data],
            },
            {
                'name': 'Desconto',
                'data': [float(desc) for desc in descfixoJul23_series_data],
            },
        ],
    }

    # Ago23*******************************************************************

    datasetAgo23 = (
        frete.values('caminhao__placa')
        .filter(data__month=8)  # lockup
        .annotate(
            fadvlrAgo23_count=Sum('frete_adiant_valor'),
            fsdvlrAgo23_count=Sum('frete_saldo_valor'),
            distanciaAgo23_count=Sum('distancia'),
        )
        .order_by('caminhao')
    )

    datasetfixoAgo23 = (
        fretefee.values('caminhao__placa')  # lockup
        .filter(data__month=8)
        .annotate(
            adiantfixoAgo23_count=Sum('valor_adiant_fixo'),
            saldofixoAgo23_count=Sum('valor_saldo_fixo'),
            descfixoAgo23_count=Sum('valor_desc_fixo'),
        )
        .order_by('caminhao')
    )

    categories = list()
    fadvlrAgo23_series_data = list()
    fsdvlrAgo23_series_data = list()
    distanciaAgo23_series_data = list()
    adiantfixoAgo23_series_data = list()
    saldofixoAgo23_series_data = list()
    descfixoAgo23_series_data = list()

    for entry in datasetAgo23:
        categories.append(entry['caminhao__placa'])
        fadvlrAgo23_series_data.append(entry['fadvlrAgo23_count'])
        fsdvlrAgo23_series_data.append(entry['fsdvlrAgo23_count'])
        distanciaAgo23_series_data.append(entry['distanciaAgo23_count'])

    for entry in datasetfixoAgo23:
        categories.append(entry['caminhao__placa'])
        adiantfixoAgo23_series_data.append(entry['adiantfixoAgo23_count'])
        saldofixoAgo23_series_data.append(entry['saldofixoAgo23_count'])
        descfixoAgo23_series_data.append(entry['descfixoAgo23_count'])

    dataAgo23 = {
        'chart': {'type': 'column'},
        'title': {'text': 'FRETES - Agosto/23'},
        'xAxis': {'categories': categories},
        # 'xAxis': {'categories':  labels[::-1]},
        'series': [
            {
                'name': 'Adiantamento',
                'data': [
                    float(adiantamento)
                    for adiantamento in fadvlrAgo23_series_data
                ],
            },
            {
                'name': 'Saldo',
                'data': [float(saldo) for saldo in fsdvlrAgo23_series_data],
            },
            {
                'name': 'KMs_Rodado',
                'data': [float(kms) for kms in distanciaAgo23_series_data],
            },
        ],
    }

    datafixoAgo23 = {
        'chart': {'type': 'column'},
        'title': {'text': 'FRETES-FIXO - Agosto/23'},
        'xAxis': {'categories': categories},
        'series': [
            {
                'name': 'Adiantamento',
                'data': [
                    float(adiantamento)
                    for adiantamento in adiantfixoAgo23_series_data
                ],
            },
            {
                'name': 'Saldo',
                'data': [float(saldo) for saldo in saldofixoAgo23_series_data],
            },
            {
                'name': 'Desconto',
                'data': [float(desc) for desc in descfixoAgo23_series_data],
            },
        ],
    }

    return render(
        request,
        template_name,
        {
            'data': data,
            'datafixo': datafixo,
            'dataJun23': dataJun23,
            'datafixoJun23': datafixoJun23,
            'dataJul23': dataJul23,
            'datafixoJul23': datafixoJul23,
            'dataAgo23': dataAgo23,
            'datafixoAgo23': datafixoAgo23,
            'fretetotal': fretetotal,
            'fretefeetotal': fretefeetotal,
        },
    )
