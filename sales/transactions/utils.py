import re
from collections import defaultdict

from rest_framework.exceptions import ValidationError


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
