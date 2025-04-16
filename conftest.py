import pytest

from api_handlers.courier_api import CourierApi


@pytest.fixture
def courier_api():
    return CourierApi("https://qa-scooter.praktikum-services.ru")