from django.test import TestCase
from model_mommy import mommy

from sales.customers.models import Customer, CustomerCard


class CustomerTestCase(TestCase):

    def setUp(self) -> None:
        self.customer = mommy.make(Customer)

    def test_create(self):
        self.assertEqual(Customer.objects.count(), 1)
        self.assertIsNotNone(self.customer)

    def test_update(self):
        old_cpf = self.customer.cpf
        self.customer.cpf = "00000000000"
        self.customer.save()

        self.assertNotEqual(self.customer.cpf, old_cpf)

    def test_delete(self):
        CustomerCard.objects.create(
            customer=self.customer,
            number="000000000000000"
        )
        customer_id = self.customer.id
        self.assertGreater(CustomerCard.objects.filter(customer_id=customer_id).count(), 0)

        self.customer.delete()

        self.assertEqual(Customer.objects.count(), 0)
        self.assertEqual(CustomerCard.objects.filter(customer_id=customer_id).count(), 0)

        with self.assertRaises(Customer.DoesNotExist):
            Customer.objects.get(pk=customer_id)
