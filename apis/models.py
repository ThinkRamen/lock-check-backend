from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    authorization = models.BooleanField(default=False)

    def __str__(self):
        return self.name
