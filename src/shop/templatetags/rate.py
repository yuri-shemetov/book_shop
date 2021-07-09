import requests
from django import template

register = template.Library()

DOLLAR_RUB = 'https://www.nbrb.by/api/exrates/rates/840?parammode=1'

@register.simple_tag
def currency_rate():
    response = requests.get(DOLLAR_RUB)
    try:
        response.raise_for_status()
        res = requests.get(DOLLAR_RUB)
        digits = res.json().get('Cur_OfficialRate')
        usd = ('1 USD = ' + str(digits) + ' BYN')
    except:
        usd = ''
    return usd