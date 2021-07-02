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


class Transaction(BaseModel):
    date = models.DateField("Data da Compra")
    hour = models.TimeField("Hora da Compra")
    value = models.DecimalField("Valor da Compra", decimal_places=2, max_digits=10)

    # Relationships
    type = models.ForeignKey(TransactionType, on_delete=models.PROTECT, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    customer_card = models.ForeignKey(CustomerCard, on_delete=models.SET_NULL, null=True)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"[{self.date} {self.hour}] {self.type}, {self.customer}, {self.store}"

    class Meta:
        unique_together = ["date", "hour", "value", "type", "customer", "customer_card"]
