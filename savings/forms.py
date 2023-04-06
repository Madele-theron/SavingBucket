from django import forms
from django.forms import ModelForm
from .models import Goal, Balance, Deposit


# Create a form to add a savings goal
class GoalForm(ModelForm):
    account = forms.ModelChoiceField(queryset=Balance.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model  = Goal
        fields = (
            "name",
            "description",
            "date_added",
            "cost",
            "image",
            "url_link",
            "account",
        )
        labels = {
            "name": "",
            "description": "",
            "date_added": "",
        }
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Savings Goal Name*"}),
            "description": forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Description*"}),
            "date_added": forms.DateInput(attrs={'class': 'form-control', 'placeholder': "Date Added", 'readonly': True}),
            # "cost": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Cost"}), 
            "image": forms.FileInput(attrs={'class': 'form-control', 'placeholder': "Image"}),
            "url_link": forms.URLInput(attrs={'class': 'form-control', 'placeholder': "Link"}),
            "account": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Account"}),
        }
        
# Create a form to add a savings account
class AccountForm(ModelForm):
    class Meta:
        model  = Balance
        fields = (
            "name",
            "amount",
        )
        
        labels = {
            "name": "",
            "amount": "",
        }
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Savings Account Name*"}),
            # "amount": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Amount"}),
        }
        
# Deposit money into savings account
class DepositForm(ModelForm):
    account = forms.ModelChoiceField(queryset=Balance.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    # date_added = forms.DateField(widget=forms.DateInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Date Added',
    #     'type': 'date',  # add this attribute to show a date picker widget
    # }))
    
    class Meta:
        model  = Deposit
        fields = (
            "amount",
            # "date_added",
            "account",
        )
        
        labels = {
            "name": "",
            # "date_added": "",
            "account": "",
        }
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Savings Account Name*"}),
            # "date_added": forms.DateInput(attrs={'class': 'form-control', 'placeholder': "Date Added"}),
            # "amount": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Amount"}),
        }