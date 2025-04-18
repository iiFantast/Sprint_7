from conftest import courier_api
from test_data.courier_data import CourierData
import allure

class TestCourierLogin:
    @allure.title('Логин курьера с валидными данными')
    def test_courier_login(self, courier_api):
        with allure.step('Отправить валидный POST запрос /login'):
            payload = CourierData.body_courier_login
            response = courier_api.courier_login(payload)
            result = response.json()
        with allure.step('Проверить статус-код и тело ответа'):
            assert response.status_code == 200
            assert result['id'] == 13842

    @allure.title('Логин курьера без указания поля пароль в запросе')
    def test_courier_login_without_password(self, courier_api):
        with allure.step('Отправить POST запрос /login без поля пароль'):
            payload = CourierData.body_courier_login_without_login
            response = courier_api.courier_login(payload)
            result = response.json()
        with allure.step('Проверить статус-код и тело ответа'):
            assert response.status_code == 400
            assert result['message'] == 'Недостаточно данных для входа'

    @allure.title('Логин курьера с неправильным паролем')
    def test_courier_login_with_wrong_password(self, courier_api):
        with allure.step('Отправить POST запрос /login с неверным паролем'):
            payload = CourierData.body_courier_login_wrong_password
            response = courier_api.courier_login(payload)
            result = response.json()
        with allure.step('Проверить статус-код и тело ответа'):
            assert response.status_code == 404
            assert result['message'] == 'Учетная запись не найдена'
