from django.db import models

from sales.core.models import BaseModel


class StoreOwner(BaseModel):
    name = models.CharField("Nome", max_length=60, null=False)

    def __str__(self):
        return self.name
