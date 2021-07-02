from rest_framework.serializers import ModelSerializer

from sales.stores.models import Store, StoreOwner


class StoreOwnerSerializer(ModelSerializer):
    class Meta:
        model = StoreOwner
        fields = ["id", "name"]


class StoreSerializer(ModelSerializer):
    owner = StoreOwnerSerializer()

    class Meta:
        model = Store
        fields = ["id", "name", "owner"]


class StoreSimpleSerializer(ModelSerializer):
    class Meta:
        model = Store
        fields = ["id", "name", ]


class StoreOwnerDetailSerializer(ModelSerializer):
    stores = StoreSimpleSerializer(many=True)

    class Meta:
        model = StoreOwner
        fields = ["id", "name", "stores"]
