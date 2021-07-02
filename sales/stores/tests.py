from django.db.models import ProtectedError
from django.test import TestCase
from model_mommy import mommy

from sales.stores.models import StoreOwner, Store


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


class StoreTestCase(TestCase):
    def setUp(self) -> None:
        self.store = mommy.make(Store)

    def test_create_store(self):
        self.assertIsNotNone(self.store)
        self.assertIsNotNone(self.store.owner)

    def test_change_owner(self):
        new_owner = StoreOwner.objects.create(name="Jhon Coltrane")
        older_owner_name = self.store.owner.name
        self.store.owner = new_owner
        self.store.save()

        self.assertNotEqual(self.store.owner.name, older_owner_name)

    def test_remove_owner(self):
        with self.assertRaises(ProtectedError):
            self.store.owner.delete()

    def test_remove_store(self):
        store_id = self.store.id
        owner = self.store.owner
        self.store.delete()

        with self.assertRaises(Store.DoesNotExist):
            Store.objects.get(pk=store_id)

        self.assertIsNotNone(owner)
