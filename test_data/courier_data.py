import random
import string


def generate_login():
    digits = ''.join(random.choice(string.digits) for _ in range(10))
    return 'login' + digits


class CourierData:
    body_create_courier = {
        "login": generate_login(),
        "password": "password123",
        "firstName": "Иван"
    }

    body_existed_courier = {
        "login": "login123",
        "password": "password123",
        "firstName": "Иван"
    }

    body_without_password = {
        "login": generate_login(),
        "firstName": "Иван"
    }

    body_courier_login = {
        "login": "login123",
        "password": "password123"
    }

    body_courier_login_without_login = {
        "password": "password123"
    }

    body_courier_login_wrong_password = {
        "login": "login123",
        "password": "123"
    }
