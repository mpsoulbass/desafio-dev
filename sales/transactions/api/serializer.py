from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from sales.customers.api.serializer import (
    CustomerSerializer, CustomerCardWithoutCustomerSerializer,
)
from sales.stores.api.serializer import StoreSerializer
from sales.transactions.models import Transaction, TransactionType


# ============[ TRANSACTION TYPE ]=============================
class TransactionTypeListSerializer(ModelSerializer):
    nature = serializers.CharField(source="get_nature_display")

    class Meta:
        model = TransactionType
        fields = ["description", "nature", "signal"]


class TransactionTypeSerializer(ModelSerializer):
    nature = serializers.CharField(source="get_nature_display")

    class Meta:
        model = TransactionType
        fields = "__all__"


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


# ==============[ TRANSACTION ]==============================
class TransactionListSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id", "date", "type", "customer", "store"]


class TransactionDetailSerializer(ModelSerializer):
    type = TransactionTypeSerializer()
    customer = CustomerSerializer()
    customer_card = CustomerCardWithoutCustomerSerializer()
    store = StoreSerializer()

    class Meta:
        model = Transaction
        fields = "__all__"
