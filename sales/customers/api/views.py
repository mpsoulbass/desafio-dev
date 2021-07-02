from rest_framework.viewsets import ModelViewSet

from sales.core.views import DefaultViewSetMixin
from sales.customers.api.serializer import (
    CustomerSerializer, CustomerCardSerializer,
    CustomerDetailSerializer,
)
from sales.customers.models import Customer, CustomerCard


class CustomerViewSet(DefaultViewSetMixin, ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    serializers = {
        "retrieve": CustomerDetailSerializer
    }


class CustomerCardViewSet(DefaultViewSetMixin, ModelViewSet):
    queryset = CustomerCard.objects.all()
    serializer_class = CustomerCardSerializer
