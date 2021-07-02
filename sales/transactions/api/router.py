from rest_framework import routers

from sales.transactions.api.view import (
    TransactionTypeViewSet,
    TransactionViewSet,
    TransactionsImportViewSet,
)

transaction_router = routers.DefaultRouter()
transaction_router.register("transaction-type", TransactionTypeViewSet)
transaction_router.register("transaction", TransactionViewSet)
transaction_router.register("transactions-import",
                            TransactionsImportViewSet,
                            basename="transactions-import")
