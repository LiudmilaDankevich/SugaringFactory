import requests

def create_user_api():
    url = 'https://test.sugaringfactory.com/index.php?route=account%2Fregister'
    data = {
        "firstname": "vbg",
        "lastname": "vv",
        "email": "bgt@gmail.com",
        "telephone": "37529752478",
        "fax": "258",
        "company": "254",
        "customer_group_id": "1",
        "company_id": "258",
        "tax_id": "125",
        "address_1": "vgyt",
        "address_2": "test",
        "city": "test",
        "postcode": "123456",
        "country_id": "209",
        "zone_id": "3198",
        "password": "251020",
        "confirm": "251020",
        "newsletter": "0",
        "captcha": "da6d51"
    }
    requests.post(url=url, data=data)
