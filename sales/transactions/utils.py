import re
from collections import defaultdict
from datetime import datetime
from decimal import Decimal

from rest_framework.exceptions import ValidationError

from sales.customers.models import Customer, CustomerCard
from sales.stores.models import StoreOwner, Store
from sales.transactions.models import TransactionType, Transaction


class DataValidator:
    def __init__(self, data):
        self.data = data
        self.customer_document = slice(19, 30)
        self.customer_card_number = slice(30, 42)
        self.transaction_date = slice(1, 9)
        self.transaction_hour = slice(42, 48)
        self.__validate()

    def __validate(self):
        errors = defaultdict(list)

        document = self.data[self.customer_document]
        card_number = self.data[self.customer_card_number]
        date = self.data[self.transaction_date]
        hour = self.data[self.transaction_hour]

        if not re.match(r"^\d{11}$", document):
            errors["CPF"].append({
                "msg": "Não foi possível extrair o CPF. Arquivo possui transações?"
            })

        if not re.match(r"^\d{4}\*\*\*\*\d{4}$", card_number):
            errors["Cartão de Crédito"].append({
                "msg": "Não foi possível extrair o número do Cartão de Crédito. "
                       "Arquivo possui transações?"
            })

        if not re.match(r"^\d{8}$", date):
            errors["Data"].append({
                "msg": "Não foi possível extrair a Data. Arquivo possui transações?"
            })

        if not re.match(r"^\d{6}$", hour):
            errors["Hora"].append({
                "msg": "Não foi possível extrair o Hora. Arquivo possui transações?"
            })

        if errors:
            raise ValidationError(errors)


class DataParser:
    _DATE_TYPE_HOUR = "hour"
    _DATE_TYPE_DATE = "date"

    def __init__(self, data):
        self.data = data
        self.transaction_type = slice(0, 1)
        self.transaction_date = slice(1, 9)
        self.transaction_hour = slice(42, 48)
        self.transaction_value = slice(9, 19)

        self.customer_document = slice(19, 30)
        self.customer_card_number = slice(30, 42)

        self.store_owner = slice(48, 62)
        self.store_name = slice(62, 81)

    @staticmethod
    def parse_date(date_string, date_type):
        date_format = {
            "date": {
                "input": "%Y%m%d",
                "output": "%Y-%m-%d",
            },
            "hour": {
                "input": "%H%M%S",
                "output": "%H:%M:%S",
            },
        }
        f = date_format.get(date_type)
        d = datetime.strptime(date_string, f["input"])
        return d.strftime(f["output"])

    def proccess(self):
        return self.__get_transaction()

    def __get_customer(self):
        customer, _ = Customer.objects.get_or_create(
            cpf=self.data[self.customer_document]
        )
        return customer

    def __get_customer_card(self):
        customer = Customer.objects.get(cpf=self.data[self.customer_document])

        customer_card, _ = CustomerCard.objects.get_or_create(
            customer=customer,
            number=self.data[self.customer_card_number]
        )
        return customer_card

    def __get_store_owner(self):
        owner, _ = StoreOwner.objects.update_or_create(
            name=self.data[self.store_owner].strip().title()
        )
        return owner

    def __get_store(self):
        store, _ = Store.objects.update_or_create(
            name=self.data[self.store_name].strip().title(),
            owner=self.__get_store_owner()
        )
        return store

    def __get_transaction_type(self):
        return TransactionType.objects.get(
            code=int(self.data[self.transaction_type])
        )

    def __get_transaction_date(self):
        return self.parse_date(self.data[self.transaction_date], date_type=self._DATE_TYPE_DATE)

    def __get_transaction_hour(self):
        return self.parse_date(self.data[self.transaction_hour], date_type=self._DATE_TYPE_HOUR)

    def __get_transaction_value(self):
        return Decimal(self.data[self.transaction_value].lstrip("0"))

    def __get_transaction(self):
        kwargs = {
            "date": self.__get_transaction_date(),
            "hour": self.__get_transaction_hour(),
            "value": self.__get_transaction_value(),
            "type": self.__get_transaction_type(),
            "customer": self.__get_customer(),
            "customer_card": self.__get_customer_card(),
            "store": self.__get_store()

        }
        transaction, _ = Transaction.objects.get_or_create(**kwargs)
        return transaction
