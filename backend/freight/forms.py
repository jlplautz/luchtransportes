from django import forms

from .models import Freight


class CustomFreightForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Freight
        fields = (
            'contrato',
            'cod_operacao',
            'data',
            'caminhao',
            'motorista',
            'origem',
            'km_origem',
            'destino',
            'km_destino',
            'distancia',
            'pedagio_pgto',
            'pedagio_valor',
            'frete_adiant_valor',
            'frete_saldo_valor',
            'frete_desc_valor',
            'frete_status',
        )
