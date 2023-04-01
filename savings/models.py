from django.db import models
from djmoney.models.fields import MoneyField, CurrencyField
import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save


class Balance(models.Model):
    name = models.CharField(max_length=100)
    amount = MoneyField(
        max_digits=10, decimal_places=2, default_currency="ZAR", default=0
    )

    def __str__(self):
        return f"{self.name} - {self.amount}"


class Goal(models.Model):
    STATUS_CHOICES = (
        ("locked", "Locked"),
        ("unlocked", "Unlocked"),
        ("completed", "Completed"),
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_added = models.DateField(default=datetime.date.today)
    cost = MoneyField(
        max_digits=10, decimal_places=2, default_currency="ZAR", default=0
    )
    image = models.ImageField(upload_to="savings/media/goal/", blank=True, null=True)
    url_link = models.URLField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="locked")
    total_saved = models.ForeignKey(Balance, on_delete=models.CASCADE)
    date_completed = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.cost} - {self.status}"

    # goal will unlock when enough money has been saved
    def is_unlocked(self):
        return self.total_saved.amount >= self.cost
    
    # completed goal will be credited from savings account
    def save(self, *args, **kwargs):
        if self.status == "completed":
            post_save.connect(credit_balance, sender=Goal)
        elif self.is_unlocked():
            self.status = "unlocked"
        super().save(*args, **kwargs)


class Deposit(models.Model):
    amount = MoneyField(
        max_digits=10, decimal_places=2, default_currency="ZAR", default=0
    )
    date_added = models.DateField(default=datetime.date.today)
    total_saved = models.ForeignKey(Balance, on_delete=models.CASCADE)

    def __str__(self):
        return f"Amount added: {self.amount}. Balance: {self.total_saved.amount}"


# Signals / Triggers / Logic


# Add deposit to balance
@receiver(post_save, sender=Deposit)
def debit_balance(sender, instance, **kwargs):
    balance = instance.total_saved
    balance.amount += instance.amount
    balance.save()


# Credit balance when goal is completed
def credit_balance(sender, instance, **kwargs):
    balance = instance.total_saved
    balance.amount -= instance.cost
    balance.save()
