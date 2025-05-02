import shortuuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Flavour(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    img_path = models.CharField(max_length=200, blank=True)


class Stock(models.Model):
    flavour = models.OneToOneField('Flavour', on_delete = models.CASCADE)
    amount = models.PositiveSmallIntegerField(
        default = 40,
        validators = [
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )


class Command(models.Model):
    code = models.CharField(max_length=22, default=shortuuid.uuid(), blank=False, null=False)
    content = models.JSONField(blank=True, null=True)
    price = models.PositiveIntegerField(null=False, default=0)
