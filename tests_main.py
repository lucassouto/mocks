# import pytest
from test_mock.main import get_status_200, get_address_data
from unittest import mock
import vcr

# def test_get_status_200_funcionou_sem_mock():
#     response = get_status_200()

#     assert response == 200


def test_get_status_200_funcionou_com_mock():
    response = mock.Mock()
    response = 200

    assert response == 200


@mock.patch("test_mock.main.get_status_200")
def test_get_status_200_funcionou_com_pytest_mock(mock_get_status_200):
    mock_get_status_200.return_value = 200
    response = mock_get_status_200()

    assert response == 200


@mock.patch("test_mock.main.get_address_data")
def test_get_address_data_com_pytest_mock(mock_get_address_data):
    mock_get_address_data.return_value = {
        "cep": "80810-070",
        "logradouro": "Rua Solimões",
        "complemento": "Apto 307 Bloco F",
        "bairro": "Mercês",
        "localidade": "Curitiba",
        "uf": "PR",
        "ibge": "4106902",
    }

    response = mock_get_address_data()

    expected_return = {
        "cep": "80810-070",
        "logradouro": "Rua Solimões",
        "complemento": "Apto 307 Bloco F",
        "bairro": "Mercês",
        "localidade": "Curitiba",
        "uf": "PR",
        "ibge": "4106902",
    }

    assert response == expected_return


@vcr.use_cassette('fixtures/vcr_cassettes/test_get_address_data_com_vcr.yaml')
def test_get_address_data_com_vcr():
    response = get_address_data()

    expected_return = {
        "cep": "80810-070",
        "logradouro": "Rua Solimões",
        "complemento": "de 981/982 ao fim",
        "bairro": "Mercês",
        "localidade": "Curitiba",
        "uf": "PR",
        "ibge": "4106902",
        "gia": "",
        "ddd": "41",
        "siafi": "7535"
    }

    assert response == expected_return
