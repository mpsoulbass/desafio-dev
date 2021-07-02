from django.db import models

from sales.core.models import BaseModel

class Customer(BaseModel):
    cpf = models.CharField("CPF", max_length=11, null=False, unique=True)

    def __str__(self):
        return self.cpf
