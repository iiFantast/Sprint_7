from conftest import courier_api
from test_data.courier_data import CourierData


class TestCourierLogin:

    def test_courier_login(self, courier_api):
        payload = CourierData.body_courier_login
        response = courier_api.courier_login(payload)
        result = response.json()
        assert response.status_code == 200
        assert result['id'] == 13842

    def test_courier_login_without_password(self, courier_api):
        payload = CourierData.body_courier_login_without_login
        response = courier_api.courier_login(payload)
        result = response.json()
        assert response.status_code == 400
        assert result['message'] == 'Недостаточно данных для входа'

    def test_courier_login_with_wrong_password(self, courier_api):
        payload = CourierData.body_courier_login_wrong_password
        response = courier_api.courier_login(payload)
        result = response.json()
        assert response.status_code == 404
        assert result['message'] == 'Учетная запись не найдена'