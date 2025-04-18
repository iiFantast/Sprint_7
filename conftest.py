import pytest
from test_data.courier_data import CourierData
from api_handlers.courier_api import CourierApi
from api_handlers.orders_api import OrdersApi


@pytest.fixture
def courier_api():
    return CourierApi("https://qa-scooter.praktikum-services.ru")

@pytest.fixture
def orders_api():
    return OrdersApi("https://qa-scooter.praktikum-services.ru")


@pytest.fixture
def courier_setup(courier_api):
    payload = CourierData.body_create_courier
    response = courier_api.create_courier(payload)
    login = courier_api.courier_login(payload)
    courier_id = login.json().get("id")
    yield {"response": response, "payload": payload}
    delete_response = courier_api.delete_courier(courier_id)
    assert delete_response.status_code == 200