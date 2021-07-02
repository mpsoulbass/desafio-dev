from django.db import models

from sales.core.models import BaseModel
from sales.customers.models import Customer, CustomerCard
from sales.stores.models import Store


class TransactionType(BaseModel):
    NATURE_INPUT = "e"
    NATURE_OUTPUT = "s"

    nature_choices = (
        (NATURE_INPUT, "Entrada"),
        (NATURE_OUTPUT, "Saída"),
    )

    description = models.CharField("Descrição", max_length=30, unique=True)
    code = models.PositiveSmallIntegerField("Código", null=True)
    nature = models.CharField("Natureza", max_length=1, null=False, choices=nature_choices)
    signal = models.CharField("Sinal", max_length=1, null=False)

    def __str__(self):
        return self.description
