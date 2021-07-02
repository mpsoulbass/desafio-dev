from django.db import models
from django.db.models import Manager, Q

from sales.core.models import BaseModel


class StoreOwner(BaseModel):
    name = models.CharField("Nome", max_length=60, null=False)

    def __str__(self):
        return self.name


class StoreFilterManager(Manager):

    def search(self, query):
        queryset = super(StoreFilterManager, self).get_queryset()
        return queryset.filter(
            Q(name__icontains=query) | Q(owner__name__icontains=query)
        ).order_by("name").distinct()


class Store(BaseModel):
    name = models.CharField("Nome", max_length=60, null=False)
    owner = models.ForeignKey(StoreOwner,
                              related_name="stores",
                              on_delete=models.PROTECT,
                              null=False)

    objects = StoreFilterManager()

    def __str__(self):
        return f"<{self.owner}> {self.name}"
