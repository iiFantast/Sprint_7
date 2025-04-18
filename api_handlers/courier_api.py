import requests

class CourierApi:
    def __init__(self, url):
        self.url = url

    def create_courier(self, body, headers=None):
        response = requests.post(f"{self.url}/api/v1/courier", json=body)
        return response

    def courier_login(self, body, headers=None):
        response = requests.post(f"{self.url}/api/v1/courier/login", json=body)
        return response

    def delete_courier(self, courier_id, headers=None):
        response = requests.delete(f"{self.url}/api/v1/courier/{courier_id}")
        return response