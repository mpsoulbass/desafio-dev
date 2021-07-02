import datetime

from django.db.models import ProtectedError
from django.test import TestCase
from model_mommy import mommy

from sales.customers.models import Customer, CustomerCard
from sales.stores.models import Store
from sales.transactions.models import Transaction, TransactionType


class TransactionTestCase(TestCase):
    def setUp(self) -> None:
        self.transaction = mommy.make(Transaction)
        customer = mommy.make(Customer)
        customer_card = mommy.make(CustomerCard)
        store = mommy.make(Store)
        type = mommy.make(TransactionType)

        self.transaction.type = type
        self.transaction.customer = customer
        self.transaction.customer_card = customer_card
        self.transaction.store = store

        self.transaction.save()

    def test_create_transaction(self):
        self.assertIsNotNone(self.transaction)

        self.assertIsNotNone(self.transaction.date)
        self.assertIsNotNone(self.transaction.hour)
        self.assertIsNotNone(self.transaction.value)

        self.assertIsNotNone(self.transaction.customer)
        self.assertIsNotNone(self.transaction.customer_card)
        self.assertIsNotNone(self.transaction.store)
        self.assertIsNotNone(self.transaction.type)
        self.assertEqual(Transaction.objects.count(), 1)

    def test_to_string(self):
        to_string = (
            f"[{self.transaction.date} {self.transaction.hour}] "
            f"{self.transaction.type}, {self.transaction.customer}, "
            f"{self.transaction.store}"
        )
        self.assertIsNotNone(str(self.transaction))
        self.assertEqual(str(self.transaction), to_string)

    def test_update_transaction(self):
        new_date = datetime.datetime(2021, 6, 1).date()
        old_date = self.transaction.date

        self.transaction.date = new_date

        self.assertEqual(self.transaction.date, new_date)
        self.assertNotEqual(self.transaction.date, old_date)
        self.assertEqual(1, Transaction.objects.count())

    def test_delete_transaction(self):
        transaction_id = self.transaction.id

        with self.assertRaises(ProtectedError):
            self.transaction.type.delete()

        self.transaction.delete()

        with self.assertRaises(Transaction.DoesNotExist):
            Transaction.objects.get(pk=transaction_id)

        self.assertEqual(Transaction.objects.count(), 0)
