import copy

import allure

from conftest import orders_api
from test_data.order_data import OrderData
import pytest

class TestCreateOrder:
    @allure.title('Создание заказа')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], [], ['BLACK', 'GREY']])
    def test_create_order(self, orders_api, color):
        with allure.step('Отправить POST запрос на /orders'):
            payload = copy.deepcopy(OrderData.body_create_order)
            payload['color'] = color
            print(payload)
            response = orders_api.create_order(payload)
            print(response.text)
            result = response.json()
        with allure.step('Проверить статус-код и тело ответа'):
            assert response.status_code == 201
            assert 'track' in result
