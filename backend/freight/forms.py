from django import forms

from .models import Freight


class CustomFreightForm(forms.ModelForm):
    contrato = forms.CharField(label='Contrato', max_length=15)
    cod_operacao = forms.CharField(label='Cod_Operação', max_length=15)
    # data = forms.DateField(label='Data')
    caminhao = forms.CharField(label='Caminhão', max_length=15)
    motorista = forms.CharField(label='Motorista', max_length=50)
    origem = forms.CharField(label='Origem', max_length=30)
    km_origem = forms.IntegerField(label='Km_Origem')
    destino = forms.CharField(label='Destino', max_length=30)
    km_destino = forms.IntegerField(label='Km_Destino')
    pedagio_pgto = forms.CharField(label='Pedágio_Pgto', max_length=2)
    # pedagio_valor = forms.CharField(label='Pedágio_Valor', max_length=10)
    # frete_adiant_valor = forms.CharField(label='Frete_Adiant', max_length=10)
    # frete_saldo_valor = forms.CharField(label='Frete_Saldo', max_length=10)
    pedagio_valor = forms.DecimalField(
        label='Pedágio_Valor',
        max_digits=5,
        decimal_places=2,
    )
    frete_adiant_valor = forms.DecimalField(
        label='Frete_Adiantamento',
        max_digits=7,
        decimal_places=2,
    )
    frete_saldo_valor = forms.DecimalField(
        label='Frete_Saldo',
        max_digits=7,
        decimal_places=2,
    )
    frete_status = forms.CharField(label='Frete_Status', max_length=2)

    class Meta:
        model = Freight
        fields = (
            'contrato',
            'cod_operacao',
            # 'data',
            'caminhao',
            'motorista',
            'origem',
            'km_origem',
            'destino',
            'km_destino',
            'pedagio_pgto',
            'pedagio_valor',
            'frete_adiant_valor',
            'frete_saldo_valor',
            'frete_status',
        )
