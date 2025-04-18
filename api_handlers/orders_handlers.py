import requests

class OrdersApi:
    def __init__(self, url):
        self.url = url

    def create_order(self, body, headers=None):
        response = requests.post(f"{self.url}/api/v1/orders", json=body)
        return response

    def get_orders(self, headers=None):
        response = requests.get(f"{self.url}/api/v1/orders")
        return response