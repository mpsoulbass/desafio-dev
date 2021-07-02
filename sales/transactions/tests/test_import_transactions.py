from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from sales.transactions.models import Transaction


class TransactionImportViewSetTestCase(TestCase):
    fixtures = ["/home/marcus.santos/Projects/sales/fixtures/transactiontype.yaml"]

    def setUp(self) -> None:
        self.api_client = APIClient()

    def test_post(self):
        endpoint = "/transactions-import/"
        data = """3201903010000014200096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO
2201903010000010900232702980568723****9987123333JOSÉ COSTA    MERCEARIA 3 IRMÃOS
8201903010000000200845152540732344****1222123222MARCOS PEREIRAMERCADO DA AVENIDA
2201903010000000500232702980567677****8778141808JOSÉ COSTA    MERCEARIA 3 IRMÃOS
3201903010000019200845152540736777****1313172712MARCOS PEREIRAMERCADO DA AVENIDA"""
        request = self.api_client.post(endpoint, {"file": data})
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 5)
