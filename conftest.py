import pytest

from api_handlers.courier_api import CourierApi
from api_handlers.orders_handlers import OrdersApi


@pytest.fixture
def courier_api():
    return CourierApi("https://qa-scooter.praktikum-services.ru")

@pytest.fixture
def orders_api():
    return OrdersApi("https://qa-scooter.praktikum-services.ru")