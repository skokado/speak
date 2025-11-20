from django.test import Client
from django.urls import reverse_lazy


client = Client()


class TestAccountRouter:
    path = reverse_lazy("api-1.0.0:account_root")

    def test_root(self):
        response = client.get(self.path)
        assert response.status_code == 200
        assert response.json() == {"message": "it works."}
