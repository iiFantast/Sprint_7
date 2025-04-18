from test_data.courier_data import CourierData
import allure

class TestCourier:
    @allure.title('Создание курьера с валидными данными')
    def test_create_courier(self, courier_api):
        with allure.step('Отправить POST запрос /courier для создания курьера'):
            payload = CourierData.body_create_courier
            response = courier_api.create_courier(payload)
            result = response.json()
        with allure.step('Проверить статус-код и тело ответа'):
            assert response.status_code == 201
            assert result['ok'] == True

    @allure.title('Создание курьера с уже существующими данными')
    def test_create_existed_courier(self, courier_api):
        with allure.step('Отправить POST запрос /courier с данными существующего курьера'):
            payload = CourierData.body_existed_courier
            response = courier_api.create_courier(payload)
            result = response.json()
        with allure.step('Проверить статус-код и сообщение об ошибке'):
            assert response.status_code == 409
            assert result['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Создание курьера без указания поля пароль в теле запроса')
    def test_create_courier_without_password(self, courier_api):
        with allure.step('Отправить POST запрос /courier без указания поля пароль'):
            payload = CourierData.body_without_password
            response = courier_api.create_courier(payload)
            result = response.json()
        with allure.step('Проверить статус-код и сообщение об ошибке'):
            assert response.status_code == 400
            assert result['message'] == 'Недостаточно данных для создания учетной записи'


