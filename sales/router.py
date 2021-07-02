from rest_framework import routers

from sales.customers.api.router import customer_router
from sales.stores.api.router import store_router
from sales.transactions.api.router import transaction_router

router = routers.DefaultRouter()

# Customer
router.registry.extend(customer_router.registry)

# Store
router.registry.extend(store_router.registry)

# Transaction
router.registry.extend(transaction_router.registry)