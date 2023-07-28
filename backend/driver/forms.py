from django import forms

from .models import Driver


class CustomDriverForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Driver
        fields = (
            'nome',
            'cpf',
            'cnh',
            'data_nasc',
            'telefone',
            'rua',
            'bairro',
            'cidade',
            'estado',
            'cep',
        )
