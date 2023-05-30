from django import forms

from .models import Driver


class CustomDriverForm(forms.ModelForm):
    required_css_class = 'required'
    # nome = forms.CharField(label='Motorista', max_length=30)
    # cpf = forms.CharField(label='CPF', max_length=11)
    # cnh = forms.CharField(label='CNH', max_length=11)
    # data_nasc = forms.DateField(label='Nascimento')
    # telefone = forms.CharField(label='Telefone', max_length=15)
    # rua = forms.CharField(label='Rua', max_length=50)
    # bairro = forms.CharField(label='Bairro', max_length=30)
    # cidade = forms.CharField(label='Cidade', max_length=15)
    # estado = forms.CharField(label='Estado', max_length=30)
    # cep = forms.CharField(label='CEP', max_length=10)

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
