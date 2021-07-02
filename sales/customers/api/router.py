from rest_framework.routers import DefaultRouter

from sales.customers.api.views import CustomerViewSet, CustomerCardViewSet

customer_router = DefaultRouter()
customer_router.register("customer", CustomerViewSet)
customer_router.register("customer-card", CustomerCardViewSet)
