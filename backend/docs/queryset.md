>>> Freight.objects.filter(caminhao__placa__icontains='ASP').aggregate(Sum("frete_adiant_valor"))
{'frete_adiant_valor__sum': Decimal('32690.7200000000')}

>>> Freight.objects.filter(caminhao__placa__icontains='ASP').aggregate(Sum("frete_saldo_valor"))
{'frete_saldo_valor__sum': Decimal('8830.08000000000')}

>>> Freight.objects.aggregate(Sum("frete_adiant_valor"))
{'frete_adiant_valor__sum': Decimal('51161.9400000000')}

>>> Freight.objects.aggregate(Sum("frete_saldo_valor"))
{'frete_saldo_valor__sum': Decimal('13409.6600000000')}

>>> Freight.objects.filter(caminhao__placa__icontains='M').aggregate(Sum("frete_adiant_valor"))
{'frete_adiant_valor__sum': Decimal('18471.2200000000')}

>>> Freight.objects.filter(caminhao__placa__icontains='M').aggregate(Sum("frete_saldo_valor"))
{'frete_saldo_valor__sum': Decimal('4579.58000000000')}

>>> Freight.objects.filter(data__month=5).count()
18

>>> Freight.objects.filter(data__day=3).count()
2

>>> Freight.objects.values('caminhao').annotate(fadvlr_count=Sum('frete_adiant_valor'), fsdvlr_count=Sum('frete_saldo_valor')).order_
by('caminhao')
<QuerySet [{'caminhao': 2, 'fadvlr_count': Decimal('32690.7200000000'), 'fsdvlr_count': Decimal('8830.08000000000')}, {'caminhao': 1, 'fadvlr_count': Decimal('18471.2200000000'), 'fsdvlr_count': Decimal('4579.58000000000')}]>

https://docs.python.org/3/library/decimal.html?highlight=decimal#decimal.Decimal

<QuerySet [
    {'caminhao': 1, 'fadvlr_count': Decimal('18471.2200000000'), 'fsdvlr_count': Decimal('4579.58000000000')}, 
    {'caminhao': 2, 'fadvlr_count': Decimal('33390.7200000000'), 'fsdvlr_count': Decimal('9130.data__month=508000000000')}, 
    {'caminhao': 3, 'fadvlr_count': Decimal('24381.6000000000'), 'fsdvlr_count': Decimal('8126.40000000000')}, 
    {'caminhao': 5, 'fadvlr_count': Decimal('33110.2200000000'), 'fsdvlr_count': Decimal('9088.78000000000')}, 
    {'caminhao': 6, 'fadvlr_count': Decimal('3731.84000000000'), 'fsdvlr_count': Decimal('1999.36000000000')}]>
>>> Freight.objects.filter(data__month=5).aggregate(Sum("frete_saldo_valor"))


>>> FreightFee.objects.values('caminhao').annotate(adiant_count=Sum('valor_adiant_fixo'), saldo_count=Sum('valor_saldo_fixo')).order_by('caminhao')
<QuerySet [
    {'caminhao': 2, 'adiant_count': Decimal('18025'), 'saldo_count': Decimal('7725')}, {'caminhao': 3, 'adiant_count': Decimal('22530'), 'saldo_count': Decimal('9270')}, {'caminhao': 5, 'adiant_count': Decimal('20300'), 'saldo_count': Decimal('8700')}, {'caminhao': 6, 'adiant_count': Decimal('10150'), 'saldo_count': Decimal('4350')}, {'caminhao': 1, 'adiant_count': Decimal('18025'), 'saldo_count': Decimal('7530')}]>


>>> total = Freight.objects.filter(data__month=5).aggregate(fat=Sum('frete_adiant_valor'), fsv=Sum('frete_saldo_valor'))
>>> total['fat']+total['fsv']
Decimal('83590.0000000000')
>>> 
>>> total['fat']+total['fsv']
Decimal('0')
>>> total = FreightFee.objects.filter(data__month=5).aggregate(af=Sum('valor_adiant_fixo'), sf=Sum('valor_saldo_fixo'))
>>> total['af']+total['sf']
Decimal('54005')
>>> total = FreightFee.objects.filter(data__month=6).aggregate(af=Sum('valor_adiant_fixo'), sf=Sum('valor_saldo_fixo'))
>>> total['af']+total['sf']
Decimal('56000')
>>> total = FreightFee.objects.filter(data__month=7).aggregate(af=Sum('valor_adiant_fixo'), sf=Sum('valor_saldo_fixo'))
>>> total['af']+total['sf']
Decimal('16600')


>>> Freight.objects.values('caminhao').filter(data__month=5).aggregate(Sum('frete_adiant_valor'))
{'frete_adiant_valor__sum': Decimal('68322.2800000000')}
>>> Freight.objects.values('caminhao').filter(data__month=5).aggregate(Sum('frete_saldo_valor'))
{'frete_saldo_valor__sum': Decimal('15267.7200000000')}
>>> Freight.objects.values('caminhao').filter(data__month=6).aggregate(Sum('frete_adiant_valor'))
{'frete_adiant_valor__sum': Decimal('79191.4600000000')}
>>> Freight.objects.values('caminhao').filter(data__month=6).aggregate(Sum('frete_saldo_valor'))
{'frete_saldo_valor__sum': Decimal('34978.8200000000')}

links para verificar
https://simpleisbetterthancomplex.com/tutorial/2016/12/06/how-to-create-group-by-queries.html
https://beta.ruff.rs/docs/rules/#pep8-naming-n