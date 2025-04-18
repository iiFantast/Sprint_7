from conftest import orders_api
import pytest
import allure

class TestGetOrders:
    @allure.title('Получение списка всех заказов')
    def test_get_orders(self, orders_api):
        with allure.step('Отправить GET запрос на /orders'):
            response = orders_api.get_orders()
            result = response.json()
        with allure.step('Проверить статус-код ответа и тело ответа'):
            assert response.status_code == 200
            assert 'orders' in result
