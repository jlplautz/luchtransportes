from django import forms

from .models import Truck, TruckFees


class CustomTruckForm(forms.ModelForm):
    marca = forms.CharField(label='Marca', max_length=20)
    modelo = forms.CharField(label='Modelo', max_length=20)
    ano_fab = forms.DateField(label='Ano_Fab')
    placa = forms.CharField(label='Placa', max_length=10)
    Chassis = forms.CharField(label='Chassis', max_length=20)
    odometro = forms.CharField(label='Odometro')

    class Meta:
        model = Truck
        fields = (
            'marca',
            'modelo',
            'ano_fab',
            'placa',
            'Chassis',
            'odometro',
        )


class CustomTruckFeesForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = TruckFees
        fields = (
            'contrato',
            'cod_operacao',
            'data',
            'caminhao',
            'valor_adiant_fixo',
            'valor_saldo_fixo',
            'valor_desc_fixo',
            'status_fixo',
        )
