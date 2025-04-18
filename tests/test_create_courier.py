from conftest import courier_setup, courier_api
from test_data.courier_data import CourierData
from test_data.response_messages import LOGIN_ALREADY_EXIST, NOT_ENOUGH_DATA_TO_CREATE
import allure

class TestCourier:
    @allure.title('Создание курьера с валидными данными')
    def test_create_courier(self, courier_setup):
        with allure.step('Отправить POST запрос /courier для создания курьера'):
            response = courier_setup['response']
            result = response.json()
        with allure.step('Проверить статус-код и тело ответа'):
            assert response.status_code == 201
            assert result['ok'] == True

    @allure.title('Создание курьера с уже существующими данными')
    def test_create_existed_courier(self, courier_api, courier_setup):
        with allure.step('Отправить POST запрос /courier с данными существующего курьера'):
            payload = courier_setup['payload']
            response = courier_api.create_courier(payload)
            result = response.json()
        with allure.step('Проверить статус-код и сообщение об ошибке'):
            assert response.status_code == 409
            assert result['message'] == LOGIN_ALREADY_EXIST

    @allure.title('Создание курьера без указания поля пароль в теле запроса')
    def test_create_courier_without_password(self, courier_api):
        with allure.step('Отправить POST запрос /courier без указания поля пароль'):
            payload = CourierData.body_without_password
            response = courier_api.create_courier(payload)
            result = response.json()
        with allure.step('Проверить статус-код и сообщение об ошибке'):
            assert response.status_code == 400
            assert result['message'] == NOT_ENOUGH_DATA_TO_CREATE


