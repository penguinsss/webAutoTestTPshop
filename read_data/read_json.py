import json

from config import BASE_DIR


def build_login_data():
    with open(BASE_DIR + '/data/login.json', encoding='utf-8') as f:
        data = json.load(f)
        data_list = []
        for i in data:
            data_list.append((i.get('username'),
                              i.get('password'),
                              i.get('verify_code'),
                              i.get('except')))
        return data_list


def build_join_cart_data():
    with open(BASE_DIR + '/data/joinCart.json', encoding='utf-8') as f:
        data = json.load(f)
        data_list = []
        for i in data:
            data_list.append((i.get('kw'),
                              i.get('locationInfo'),
                              i.get('except')))
        return data_list
