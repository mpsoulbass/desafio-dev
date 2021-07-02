from django.test import TestCase
from model_mommy import mommy

from sales.customers.models import Customer, CustomerCard


class CustomerCardTestCase(TestCase):
    def setUp(self) -> None:
        self.card = mommy.make(CustomerCard)

    def test_create(self):
        self.assertEqual(CustomerCard.objects.count(), 1)
        self.assertIsNotNone(self.card)
        self.assertIsNotNone(self.card.customer)

    def test_update_number(self):
        old_number = self.card.number
        self.card.number = "000000000000000"
        self.card.save()

        self.assertNotEqual(self.card.number, old_number)

    def test_update_customer(self):
        new_customer = mommy.make(Customer)
        old_customer = self.card.customer

        self.card.customer = new_customer
        self.card.save()

        self.assertNotEqual(self.card.customer, old_customer)
        self.assertEqual(self.card.customer, new_customer)

    def test_delete_customer(self):
        customer_id = self.card.customer.id
        card_id = self.card.id

        self.card.customer.delete()

        with self.assertRaises(Customer.DoesNotExist):
            Customer.objects.get(pk=customer_id)

        with self.assertRaises(CustomerCard.DoesNotExist):
            CustomerCard.objects.get(pk=card_id)

        self.assertEqual(CustomerCard.objects.count(), 0)

    def test_delete(self):
        card_id = self.card.id
        self.card.delete()

        with self.assertRaises(CustomerCard.DoesNotExist):
            CustomerCard.objects.get(pk=card_id)

        self.assertEqual(CustomerCard.objects.count(), 0)
