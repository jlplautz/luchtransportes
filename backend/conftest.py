import pytest

from backend.accounts.models import User
from backend.driver.models import Driver
from backend.freight.models import Freight


@pytest.fixture
def new_user(db):
    user = User.objects.create(
        first_name='Jorge',
        last_name='Plautz',
        email='plautz@email.com',
    )
    return user


@pytest.fixture
def new_driver(db):
    driver = Driver.objects.create(
        # nome='Plautz',
        data_nasc='1958-10-01',
        # email='plautz@email.com',
        cpf='30172152968',
        telefone='41996514346',
        cnh='112345678901',
        endereco='Castro Alves, 820',
        bairro='Agua Verde',
        cidade='Curitiba',
        estado='Parana',
        cep='80240270',
    )
    return driver


@pytest.fixture
def new_freight(db):
    freight = Freight.objects.create(
        contrato='GPWC-2828',
        cod_operacao='805156844205',
        data='10-05-2023',
        caminhao='AXB-8606',
        motorista='Plautz',
        origem='Curitiba',
        Km_origem='80678',
        destino='São Paulo',
        Km_destino='81079',
        # pedagio_pgto='SP',
        pedagio_valor='350',
        adiantamento_valor='1306',
        saldo_valor='400',
        # frete_status='FS',
    )
    return freight
