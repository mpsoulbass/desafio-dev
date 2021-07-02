from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from sales.stores.models import Store
from sales.transactions.models import Transaction


class TransactionReportViewSet(ViewSet):

    @staticmethod
    def get_real_value(value, signal):
        mult = -1 if signal == '-' else 1
        return value * mult

    def list(self, request):
        # Filters
        store = request.query_params.get("store", "")

        # Data
        all_stores = Store.objects.search(store)
        all_transactions = Transaction.objects.all().order_by("store", "date", "hour").distinct()

        # Controllers
        balance = 0
        data = []
        store_transactions = []

        for store in all_stores:
            for transaction in all_transactions:
                if store != transaction.store:
                    continue

                value = self.get_real_value(transaction.value, transaction.type.signal)
                balance += float(value)
                store_transactions.append({
                    "date": transaction.date.strftime("%d/%m/%Y"),
                    "hour": transaction.hour,
                    "value": value,
                    "type": transaction.type.description,
                    "signal": transaction.type.signal,
                    "customer": transaction.customer.cpf,
                    "customer_card": transaction.customer_card.number,
                    "current_balance": balance
                })

            # Accum Results
            data.append({
                "store": store.name,
                "owner": store.owner.name,
                "owner_id": store.owner.id,
                "balance": balance,
                "transactions": store_transactions,
            })
            balance = 0
            store_transactions = []

        return Response(
            data={"transactions_by_store": data},
            status=status.HTTP_200_OK,
        )


"""
    ===============================================================================
    CONSULTA SQL PARA VALIDACAO DOS VALORES
    ===============================================================================
    WITH base as (
    SELECT
           t.value        as "value",
           tt.signal      as signal,
           ss.name        as store,
           s.name         as store_owner
    FROM transactions_transaction t
             INNER JOIN stores_store ss on ss.id = t.store_id
             INNER JOIN stores_storeowner s on s.id = ss.owner_id
             INNER JOIN transactions_transactiontype tt on tt.id = t.type_id
    order by store, date, hour
    )
    SELECT 
        store, 
        store_owner,
        SUM(case b.signal when '-' then b.value * -1 else b.value end) as balance
    from base b
    GROUP BY store, store_owner
    ORDER BY balance DESC
"""
