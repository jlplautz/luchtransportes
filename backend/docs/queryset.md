>>> Freight.objects.filter(caminhao__placa__icontains='ASP').aggregate(Sum("frete_adiant_valor"))
{'frete_adiant_valor__sum': Decimal('32690.7200000000')}

>>> Freight.objects.filter(caminhao__placa__icontains='ASP').aggregate(Sum("frete_saldo_valor"))
{'frete_saldo_valor__sum': Decimal('8830.08000000000')}

>>> Freight.objects.aggregate(Sum("frete_adiant_valor"))
{'frete_adiant_valor__sum': Decimal('51161.9400000000')}

>>> Freight.objects.aggregate(Sum("frete_saldo_valor"))
{'frete_saldo_valor__sum': Decimal('13409.6600000000')}

>>> clear{'frete_adiant_valor__sum': Decimal('18471.2200000000')}

>>> Freight.objects.filter(caminhao__placa__icontains='M').aggregate(Sum("frete_saldo_valor"))
{'frete_saldo_valor__sum': Decimal('4579.58000000000')}

>>> Freight.objects.filter(data__month=5).count()
18

>>> Freight.objects.filter(data__day=3).count()
2

>>> Freight.objects.values('caminhao').annotate(fadvlr_count=Sum('frete_adiant_valor'), fsdvlr_count=Sum('frete_saldo_valor')).order_by('caminhao')
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


>>> Freight.objects.filter(caminhao__placa__icontains='awp').filter(data__month=7).aggregate(Sum("frete_saldo_valor"))
{'frete_saldo_valor__sum': Decimal('4808.44')}
>>> Freight.objects.filter(caminhao__placa__icontains='awp').filter(data__month=7).aggregate(Sum("frete_adiant_valor"))
{'frete_adiant_valor__sum': Decimal('20785.91')}
>>> TruckFlue.objects.filter(caminhao__placa__icontains='awp').filter(data__month=7).aggregate(Sum("flue_valor"))
{'flue_valor__sum': Decimal('17535.80')}
>>> 

>>> TruckFlue.objects.values('caminhao__placa').filter(data__month=7).annotate(Valor_Total=Sum('flue_valor')).order_by('-caminhao__placa')
<QuerySet [{'caminhao__placa': 'IUD0B73', 'Valor_Total': Decimal('3960.60')}, {'caminhao__placa': 'AWP8J53', 'Valor_Total': Decimal('17660.11')}, {'caminhao__placa': 'ASP6I28', 'Valor_Total': Decimal('2167.88')}]>


>>> TruckFlue.objects.values('caminhao__placa').filter(data__month=7).annotate(Valor_Total=Sum('flue_valor')).order_by('-caminhao__placa')
<QuerySet [{'caminhao__placa': 'IUD0B73', 'Valor_Total': Decimal('3960.60')}, {'caminhao__placa': 'AWP8J53', 'Valor_Total': Decimal('17660.11')}, {'caminhao__placa': 'ASP6I28', 'Valor_Total': Decimal('2167.88')}]

>>> TruckFlue.objects.values('caminhao__placa').filter(data__month=6).annotate(Valor_Total=Sum('flue_valor')).order_by(
'-caminhao__placa')
<QuerySet [{'caminhao__placa': 'MVY2C20', 'Valor_Total': Decimal('928.00')}, {'caminhao__placa': 'KVK8331', 'Valor_Total': Decimal('7266.50')}, {'caminhao__placa': 'IUD0B73', 'Valor_Total': Decimal('5742.18')}, {'caminhao__placa': 'AWP8J53', 'Valor_Total': Decimal('2433.15')}]>


TruckFlue.objects.values('caminhao__placa').annotate(Valor_Total=Sum('flue_valor'))


links para verificar
https://simpleisbetterthancomplex.com/tutorial/2016/12/06/how-to-create-group-by-queries.html
https://beta.ruff.rs/docs/rules/#pep8-naming-n


Comunidade 31/07/23

** ver este setup
AUTH_USER_MODEL = 'base.User', um apenas

https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html


https://docs.djangoproject.com/en/4.2/topics/db/fixtures/

## Verificar instruçoes para o ngnix entender o protocolo usado no acesso
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


## Problema do Luciano
https://leetcode.com/problems/3sum/

input_list = [2,8,12,15]
target = 20

https://leetcode.com/problems/two-sum/

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

busca binaria lib bicsec já implementa



## Como fazer o back no SQLITE3

### no settings.py é necesario deixar a configuração do SQLITE 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

### executar o coamndo 
(luchtransportes-py3.11) ╭─plautz@ProBook-6470b ~/VSCProjects/luchtransportes ‹issue-23●› 
╰─$ python manage.py dumpdata > data.json  -> arquivo data.json é criado formato UTF-8

### depois alterar no setting a configuração 
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': config(
        'DATABASE_URL',
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3'),
        cast=db_url
    )
}

### Para fazer o load do file data.json no POSTGRES
Entrar no terminar do container da aplicação e executar
1- python manage.py shell
2- from django.contrib.contenttypes.models import ContentType
3- ContentType.objects.all().delete() -> não pode ter nenhum registro gravado
4- exit()
python manage.py loaddata data.json



>>> Freight.objects.values('caminhao__placa').annotate(adiant=Sum('frete_adiant_valor'), saldo=Sum('frete_saldo_valor'))
<QuerySet [
    {'caminhao__placa': 'MVY2C20', 'adiant': Decimal('30322.37'), 'saldo': Decimal('24341.61')}, 
    {'caminhao__placa': 'KVK8331', 'adiant': Decimal('20596.62'), 'saldo': Decimal('5694.98')}, 
    {'caminhao__placa': 'AWP8J53', 'adiant': Decimal('71364.86'), 'saldo': Decimal('14318.99')}, 
    {'caminhao__placa': 'IUD0B73', 'adiant': Decimal('48562.38'), 'saldo': Decimal('9759.02')}, 
    {'caminhao__placa': 'ASP6I28', 'adiant': Decimal('58727.72'), 'saldo': Decimal('11443.08')}]>

>>> FreightFee.objects.values('caminhao__placa').annotate(adiant=Sum('valor_adiant_fixo'), saldo=Sum('valor_saldo_fixo'))
<QuerySet [
    {'caminhao__placa': 'MVY2C20', 'adiant': Decimal('18025.00'), 'saldo': Decimal('7530.00')}, 
    {'caminhao__placa': 'KVK8331', 'adiant': Decimal('10150.00'), 'saldo': Decimal('4350.00')}, 
    {'caminhao__placa': 'AWP8J53', 'adiant': Decimal('18690.00'), 'saldo': Decimal('8010.00')}, 
    {'caminhao__placa': 'IUD0B73', 'adiant': Decimal('20300.00'), 'saldo': Decimal('8700.00')}, 
    {'caminhao__placa': 'ASP6I28', 'adiant': Decimal('18025.00'), 'saldo': Decimal('7725.00')}]>    


>>> TruckFlue.objects.values('caminhao__placa').annotate(flue=Sum('flue_valor'), litros=Sum('litros'))
<QuerySet [
    {'caminhao__placa': 'MVY2C20', 'flue': Decimal('12288.80'), 'litros': 2631.3570000000004}, 
    {'caminhao__placa': 'KVK8331', 'flue': Decimal(' 9416.50'), 'litros': 0.0}, 
    {'caminhao__placa': 'AWP8J53', 'flue': Decimal('29663.69'), 'litros': 753.8000000000001}, 
    {'caminhao__placa': 'IUD0B73', 'flue': Decimal('16765.57'), 'litros': 3609.1899999999996}, 
    {'caminhao__placa': 'ASP6I28', 'flue': Decimal('27879.59'), 'litros': 5517.363}]>
>>> 

# ***********************************************
Total Fretes 

'MVY2C20', 'adiant': 30322.37, 'saldo': 24341.61
'KVK8331', 'adiant': 20596.62, 'saldo':  5694.98
'AWP8J53', 'adiant': 71364.86, 'saldo': 14318.99
'IUD0B73', 'adiant': 48562.38, 'saldo':  9759.02
'ASP6I28', 'adiant': 58727.72, 'saldo': 11443.08

# ***********************************************
Total Fretes Fixos
'MVY2C20', 'adiant': 18025.00, 'saldo':  7530.00
'KVK8331', 'adiant': 10150.00, 'saldo':  4350.00
'AWP8J53', 'adiant': 18690.00, 'saldo':  8010.00
'IUD0B73', 'adiant': 20300.00, 'saldo':  8700.00
'ASP6I28', 'adiant': 18025.00, 'saldo':  7725.00

# ***********************************************
Combustivel
'MVY2C20', 'Valor': 12288.80, 'litros': 2631.357
'KVK8331', 'Valor':  9416.50, 'litros':    0.0
'AWP8J53', 'Valor': 29663.69, 'litros':  753.800
'IUD0B73', 'Valor': 16765.57, 'litros': 3609.189
'ASP6I28', 'Valor': 27879.59, 'litros': 5517.363
# ***********************************************

>>> TruckFlue.objects.values('caminhao__placa').filter(data__month=8).annotate(Valor_Total=Sum('flue_valor')).annotate(litros=Sum('litros'))
<QuerySet [
    {'caminhao__placa': 'ASP6I28', 'Valor_Total': Decimal('3055.47'), 'litros':  671.841}, 
    {'caminhao__placa': 'AWP8J53', 'Valor_Total': Decimal('3148.50'), 'litros':   17.957}, 
    {'caminhao__placa': 'IUD0B73', 'Valor_Total': Decimal('6219.67'), 'litros': 1319.249}, 
    {'caminhao__placa': 'MVY2C20', 'Valor_Total': Decimal('5370.54'), 'litros': 1142.429}]>

>>> TruckFlue.objects.values('caminhao__placa').filter(data__month=7).annotate(Valor_Total=Sum('flue_valor')).annotate(litros=Sum('litros'))
<QuerySet [
    {'caminhao__placa': 'ASP6I28', 'Valor_Total': Decimal(' 2167.88'), 'litros': 470.451}, 
    {'caminhao__placa': 'AWP8J53', 'Valor_Total': Decimal('17660.11'), 'litros': 0.0}, 
    {'caminhao__placa': 'IUD0B73', 'Valor_Total': Decimal(' 3960.60'), 'litros': 842.5230000000001}, {'caminhao__placa': 'MVY2C20', 'Valor_Total': Decimal(' 1905.31'), 'litros': 415.116}]>

>>> TruckFlue.objects.values('caminhao__placa').filter(data__month=6).annotate(Valor_Total=Sum('flue_valor')).annotate(litros=Sum('litros'))
<QuerySet [
    {'caminhao__placa': 'AWP8J53', 'Valor_Total': Decimal('2433.15'), 'litros': 527.088}, 
    {'caminhao__placa': 'IUD0B73', 'Valor_Total': Decimal('5742.18'), 'litros': 1259.6399999999999}, {'caminhao__placa': 'KVK8331', 'Valor_Total': Decimal('7266.50'), 'litros': 0.0}, 
    {'caminhao__placa': 'MVY2C20', 'Valor_Total': Decimal(' 928.00'), 'litros': 200.0}]>

    >>> TruckFlue.objects.values('caminhao__placa').filter(data__month=5).annotate(Valor_Total=Sum('flue_valor')).annotate(litros=Sum('litros'))
<QuerySet [
    {'caminhao__placa': 'ASP6I28', 'Valor_Total': Decimal('15269.57'), 'litros': 2967.481}, 
    {'caminhao__placa': 'AWP8J53', 'Valor_Total': Decimal(' 6421.93'), 'litros': 208.755}, 
    {'caminhao__placa': 'IUD0B73', 'Valor_Total': Decimal('  843.12'), 'litros': 187.778}, 
    {'caminhao__placa': 'KVK8331', 'Valor_Total': Decimal(' 2150.00'), 'litros': 0.0}, 
    {'caminhao__placa': 'MVY2C20', 'Valor_Total': Decimal(' 4084.95'), 'litros': 873.811}]>

>>> TruckFlue.objects.values('caminhao__placa').filter(data__month=4).annotate(Valor_Total=Sum('flue_valor')).annotate(litros=Sum('litros'))
<QuerySet [
    {'caminhao__placa': 'ASP6I28', 'Valor_Total': Decimal('7386.67'), 'litros': 1407.590}]>