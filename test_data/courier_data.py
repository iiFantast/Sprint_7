class CourierData:
    body_create_courier = {
        "login": "vgoncharenko12345",
        "password": "password123",
        "firstName": "Иван"
    }

    body_without_password = {
        "login": "vgoncharenko12345",
        "firstName": "Иван"
    }

    body_courier_login_without_login = {
        "password": "password123"
    }

    body_courier_login_wrong_password = {
        "login": "vgoncharenko12345",
        "password": "123"
    }
