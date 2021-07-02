from django.db import models

from sales.core.models import BaseModel


class CustomerCard(BaseModel):
    customer = models.ForeignKey("Customer",
                                 related_name="credit_cards",
                                 on_delete=models.CASCADE,
                                 null=False)
    number = models.CharField("Card Number", max_length=15, null=False)


class Customer(BaseModel):
    cpf = models.CharField("CPF", max_length=11, null=False, unique=True)

    def __str__(self):
        return self.cpf
