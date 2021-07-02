from django.test import TestCase
from model_mommy import mommy

from sales.stores.models import StoreOwner


class StoreOwnerTestCase(TestCase):
    def setUp(self) -> None:
        self.owner = mommy.make(StoreOwner)

    def test_create_owner(self):
        self.assertIsNotNone(self.owner)
        self.assertIsNotNone(self.owner.name)

    def test_bulk_create_owner(self):
        mommy.make(StoreOwner, _quantity=100)
        self.assertEqual(StoreOwner.objects.count(), 101)

    def test_update_owner_name(self):
        self.owner.name = "Jhon Coltrane"
        self.owner.save()

        self.assertEqual(self.owner.name, "Jhon Coltrane")

    def test_delete_owner(self):
        oid = self.owner.id
        self.owner.delete()
        with self.assertRaises(StoreOwner.DoesNotExist):
            StoreOwner.objects.get(pk=oid)

    def test_remove_all(self):
        StoreOwner.objects.all().delete()
        self.assertEqual(StoreOwner.objects.count(), 0)
