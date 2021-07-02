from rest_framework.viewsets import ModelViewSet

from sales.core.views import DefaultViewSetMixin, ProtectedDestroyMixin
from sales.stores.api.serializer import (
    StoreSerializer, StoreOwnerSerializer,
    StoreOwnerDetailSerializer,
)
from sales.stores.models import Store, StoreOwner


class StoreViewSet(DefaultViewSetMixin, ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class StoreOwnerViewSet(DefaultViewSetMixin, ProtectedDestroyMixin, ModelViewSet):
    queryset = StoreOwner.objects.all()
    serializer_class = StoreOwnerSerializer
    protected_model_name = "store-owner"
    serializers = {
        "retrieve": StoreOwnerDetailSerializer
    }
