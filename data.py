import random as r
from faker import Faker

fake = Faker()


class TestDataCurrier:
    CREATE_COURIER_BODY = {
        "login": fake.user_name(),
        "password": fake.password(),
        "firstName": fake.first_name()
    }

    CREATE_COURIER_BODY2 = {
        "login": fake.user_name(),
        "password": fake.password(),
        "firstName": fake.first_name()
    }

    NULL_BODY = {
        "login": '',
        "password": '',
        "firstName": ''
    }


class TestDataCreateOrder:
    DATA_ORDER = {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": r.randint(1, 100),
        "phone": fake.phone_number(),
        "rentTime": r.randint(1, 100),
        "deliveryDate": fake.date(),
        "comment": fake.text(),
        "color": [
            "BLACK"
        ]}


class TestDataGetListOrder:
    PARAMS_ORDERS = {
        "limit": "10",
        "page": "0"

    }
