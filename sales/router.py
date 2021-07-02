from rest_framework import routers

from sales.customers.api.router import customer_router

router = routers.DefaultRouter()

# Customer
router.registry.extend(customer_router.registry)
