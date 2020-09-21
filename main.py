import requests


def get_status_200():
    return requests.get("https://httpbin.org/status/200").status_code
    # return 200


def get_status_404():
    return requests.get("https://httpbin.org/status/404").status_code
    # return 404


def get_address_data():
    return requests.get("https://viacep.com.br/ws/80810070/json/").json()
    # {
    #     "cep": "80810-070",
    #     "logradouro": "Rua Solimões",
    #     "complemento": "de 981/982 ao fim",
    #     "bairro": "Mercês",
    #     "localidade": "Curitiba",
    #     "uf": "PR",
    #     "ibge": "4106902",
    #     "gia": "",
    #     "ddd": "41",
    #     "siafi": "7535"
    # }
