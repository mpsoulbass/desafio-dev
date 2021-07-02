from django.db.models import ProtectedError
from django.test import TestCase
from model_mommy import mommy

from sales.transactions.models import TransactionType, Transaction


class TransactionTypeTestCase(TestCase):
    def setUp(self) -> None:
        self.type = mommy.make(TransactionType)

    def test_create_transaction_type(self):
        self.assertIsNotNone(self.type)
        self.assertEqual(TransactionType.objects.count(), 1)

    def test_update_transaction_type(self):
        new_description = "Depósito em conta"
        self.type.description = new_description
        self.type.nature = TransactionType.NATURE_INPUT
        self.type.save()

        self.assertEqual(self.type.description, new_description)
        self.assertEqual(1, TransactionType.objects.count())
        self.assertIn(self.type.nature, [x[0] for x in TransactionType.nature_choices])

    def test_delete_transaction_type(self):
        p = mommy.make(Transaction)
        tid = p.type.id

        self.assertEqual(2, TransactionType.objects.count())
        self.assertIsNotNone(p.type)

        with self.assertRaises(ProtectedError):
            p.type.delete()

        p.delete()
        p.type.delete()

        with self.assertRaises(TransactionType.DoesNotExist):
            TransactionType.objects.get(pk=tid)

        self.assertEqual(1, TransactionType.objects.count())
