from rest_framework.serializers import ModelSerializer

from sales.customers.models import Customer, CustomerCard


class CustomerCardSerializer(ModelSerializer):
    class Meta:
        model = CustomerCard
        fields = ["id", "number", "customer"]


class CustomerCardWithoutCustomerSerializer(ModelSerializer):
    class Meta:
        model = CustomerCard
        fields = ["id", "number"]


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "cpf"]


class CustomerDetailSerializer(ModelSerializer):
    credit_cards = CustomerCardSerializer(many=True)

    class Meta:
        model = Customer
        fields = ["id", "cpf", "credit_cards"]
