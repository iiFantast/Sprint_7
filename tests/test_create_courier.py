from test_data.courier_data import CourierData

class TestCourier:
    def test_create_courier(self, courier_api):
        payload = CourierData.body_create_courier
        response = courier_api.create_courier(payload)
        result = response.json()
        assert response.status_code == 201
        assert result['ok'] == True

    def test_create_existed_courier(self, courier_api):
        payload = CourierData.body_existed_courier
        response = courier_api.create_courier(payload)
        result = response.json()
        assert response.status_code == 409
        assert result['message'] == 'Этот логин уже используется. Попробуйте другой.'

    def test_create_courier_without_password(self, courier_api):
        payload = CourierData.body_without_password
        response = courier_api.create_courier(payload)
        result = response.json()
        assert response.status_code == 400
        assert result['message'] == 'Недостаточно данных для создания учетной записи'


