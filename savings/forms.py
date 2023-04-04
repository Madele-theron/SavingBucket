from django import forms
from django.forms import ModelForm
from .models import Goal, Balance, Deposit


# Create a form to add a savings goal
class GoalForm(ModelForm):
    class Meta:
        model  = Goal
        fields = (
            "name",
            "description",
            "date_added",
            "cost",
            "image",
            "url_link",
            "status",
            "account",
            "date_completed",
        )
        
# Create a form to add a savings account
class AccountForm(ModelForm):
    class Meta:
        model  = Balance
        fields = (
            "name",
            "amount",
        )
        
# Deposit money into savings account
class DepositForm(ModelForm):
    class Meta:
        model  = Deposit
        fields = (
            "amount",
            "date_added",
            "account",
        )