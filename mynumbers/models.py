from django.db import models


class Number(models.Model):
    number = models.BigIntegerField(unique=True)


class NumberInfo(models.Model):
    number = models.OneToOneField(Number, on_delete=models.PROTECT)
    sqrt = models.FloatField()
    # digits_sum = models.BigIntegerField()
    # digits_prod = models.BigIntegerField()
    divisors = models.JSONField()
    # powers = models.JSONField()
    is_even = models.BooleanField()
    # is_pi_digits = models.BooleanField()
    # is_prime = models.BooleanField()
    