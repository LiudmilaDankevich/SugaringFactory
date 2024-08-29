from datetime import datetime
from http.client import responses

import requests
from datetime import datetime

from pages.base_page import BasePage



def create_user_api(browser):
    url = 'https://test.sugaringfactory.com/index.php?route=account%2Fregister'
    email = f"user_{datetime.now().strftime('%d%m%Y_%H_%M_%f')}@gmail.com"
    password = "11111"
    data = {
        "firstname": "vbg",
        "lastname": "vv",
        "email": email,
        "telephone": "+375297774477",
        "fax": "258",
        "company": "254",
        "customer_group_id": "1",
        "company_id": "258",
        "tax_id": "125",
        "address_1": "Zudro 5-47",
        "address_2": "test",
        "city": "Minsk",
        "postcode": "10001",
        "country_id": "209",
        "zone_id": "3198",
        "password": password,
        "confirm": password,
        "newsletter": "0",
        "captcha": "da6d51"
    }
    response = requests.post(url=url, data=data)
    assert response.status_code == 200
    return email, password
