from django.shortcuts import render
from .models import Goal, Balance, Deposit

# Create your views here.
def home(request): # this can be the landing page :) // or just the main over view page??
    goals = Goal.objects.all()
    accounts = Balance.objects.all()
    return render(request, "home.html", {"goals": goals, "accounts":accounts})

def overview(request):
    return render(request, "overview.html")

def history(request):
    completed_goals = Goal.objects.filter(status="completed")
    return render(request, "history.html", {"completeedgoals": completed_goals})

def contact(request):
    return render(request, "contact.html")

# this will be the page to view and edit an individual goal
def savings_goal(request, pk):
    goal = Goal.objects.get(pk=pk)
    return render(request, "savings_goal.html", {"goal": goal})

