from rest_framework.routers import DefaultRouter

from sales.stores.api.views import StoreViewSet, StoreOwnerViewSet

store_router = DefaultRouter()
store_router.register("store", StoreViewSet)
store_router.register("store-owner", StoreOwnerViewSet)
