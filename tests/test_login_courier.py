from conftest import courier_api, courier_setup
from test_data.courier_data import CourierData
from test_data.response_messages import LOGIN_NOT_FOUND, NOT_ENOUGH_DATA_TO_LOGIN
import allure

class TestCourierLogin:
    @allure.title('Логин курьера с валидными данными')
    def test_courier_login(self, courier_api, courier_setup):
        with allure.step('Отправить валидный POST запрос /login'):
            payload = courier_setup['payload']
            response = courier_api.courier_login(payload)
            result = response.json()
        with allure.step('Проверить статус-код и тело ответа'):
            assert response.status_code == 200
            assert 'id' in result

    @allure.title('Логин курьера без указания поля пароль в запросе')
    def test_courier_login_without_password(self, courier_api, courier_setup):
        with allure.step('Отправить POST запрос /login без поля пароль'):
            payload = CourierData.body_courier_login_without_login
            response = courier_api.courier_login(payload)
            result = response.json()
        with allure.step('Проверить статус-код и тело ответа'):
            assert response.status_code == 400
            assert result['message'] == NOT_ENOUGH_DATA_TO_LOGIN

    @allure.title('Логин курьера с неправильным паролем')
    def test_courier_login_with_wrong_password(self, courier_api, courier_setup):
        with allure.step('Отправить POST запрос /login с неверным паролем'):
            payload = courier_setup['payload']
            payload['password'] = '123'
            response = courier_api.courier_login(payload)
            result = response.json()
        with allure.step('Проверить статус-код и тело ответа'):
            assert response.status_code == 404
            assert result['message'] == LOGIN_NOT_FOUND
