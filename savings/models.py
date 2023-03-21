from django.db import models
from djmoney.models.fields import MoneyField, CurrencyField
import datetime


class Balance(models.Model):
    name = models.CharField(max_length=100)
    amount = MoneyField(
        max_digits=10, decimal_places=2, default_currency="ZAR", default=0
    )

    def __str__(self):
        return f"{self.name} - {self.amount}"


class SavingGoal(models.Model):
    STATUS_CHOICES = (
        ("locked", "Locked"),
        ("unlocked", "Unlocked"),
        ("completed", "Completed"),
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_added = models.DateField(default=datetime.date.today)
    image = models.ImageField(upload_to="media/goal/", blank=True, null=True)
    url_link = models.URLField(blank=True)
    cost = MoneyField(
        max_digits=10, decimal_places=2, default_currency="ZAR", default=0
    )
    date_completed = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="locked")

    def __str__(self):
        return f"{self.name} - {self.cost} - {self.status}"


class Deposit(models.Model):
    amount = MoneyField(
        max_digits=10, decimal_places=2, default_currency="ZAR", default=0
    )
    date_added = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"Amount added: {self.amount}"
