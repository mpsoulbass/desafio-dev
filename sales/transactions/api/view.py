from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, ViewSet

from sales.core.views import DefaultViewSetMixin, ProtectedDestroyMixin
from sales.transactions.api.serializer import (
    TransactionSerializer,
    TransactionTypeSerializer,
    TransactionTypeListSerializer,
    TransactionListSerializer,
    TransactionDetailSerializer,
)
from sales.transactions.models import Transaction, TransactionType
from sales.transactions.utils import DataParser, DataValidator


class TransactionTypeViewSet(DefaultViewSetMixin, ProtectedDestroyMixin, ReadOnlyModelViewSet):
    queryset = TransactionType.objects.all()
    serializer_class = TransactionTypeSerializer
    protected_model_name = "transaction-type"
    serializers = {"list": TransactionTypeListSerializer}


class TransactionViewSet(DefaultViewSetMixin, ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    serializers = {"list": TransactionListSerializer, "retrieve": TransactionDetailSerializer}


class TransactionsImportViewSet(ViewSet):
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request):
        if "file" not in request.data.keys():
            raise ValidationError({"file": "Este campo é obrigatório"})

        transactions = request.data["file"]
        for transaction in transactions.split("\n"):
            DataValidator(transaction)
            t = DataParser(transaction).proccess()
            if t is None:
                raise ValidationError(
                    {"transaction": "Erro ao tentar importar a transaction %s" % transaction}
                )

        return Response(
            data={"msg": "Processamento finalizado com sucesso"}, status=status.HTTP_201_CREATED
        )
