from django import forms

from backend.accounts.models import User

from .models import Driver


class CustomDriverForm(forms.ModelForm):
    cpf = forms.CharField(label='CPF', max_length=11)
    cnh = forms.CharField(label='CNH', max_length=11)
    data_nasc = forms.DateField(label='Nascimento')
    telefone = forms.CharField(label='Telefone', max_length=15)
    endereco = forms.CharField(label='Endereço', max_length=50)
    bairro = forms.CharField(label='Bairro', max_length=30)
    cidade = forms.CharField(label='Cidade', max_length=15)
    estado = forms.CharField(label='Estado', max_length=30)
    cep = forms.CharField(label='CEP', max_length=10)
    user = forms.CharField(label='Motorista', max_length=30)

    class Meta:
        model = Driver
        fields = (
            'cpf',
            'cnh',
            'data_nasc',
            'telefone',
            'endereco',
            'bairro',
            'cidade',
            'estado',
            'cep',
            'user',
        )
