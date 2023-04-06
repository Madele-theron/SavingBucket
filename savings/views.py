from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import GoalForm, AccountForm, DepositForm
import datetime

# buy / "complete" a savings goal
def complete_goal(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    goal.status = "completed"
    goal.date_completed = datetime.date.today()
    goal.save()
    
    return redirect('savings:history')

# delete savings account
def delete_account(request, account_id):
    account = Balance.objects.get(id=account_id)
    account.delete()
    
    return redirect('savings:home')

# delete savings goal
def delete_goal(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    goal.delete()
    
    return redirect('savings:home')
    
def update_goal(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    form = GoalForm(request.POST or None, instance=goal)
    if form.is_valid():
        form.save()
        return redirect('savings:home')
    return render(request, "update_goal.html", {"goal": goal, "form": form})

def deposit(request):
    submitted = False
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/deposit?submitted=True")
    else:
        form = DepositForm()
        if 'submitted' in request.GET:
            submitted = True
        
    return render(request, 'deposit.html', {"form": form, "submitted": submitted})

def add_goal(request):
    submitted = False
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_goal?submitted=True")
    else:
        form = GoalForm()
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'add_goal.html', {"form": form, "submitted": submitted })

def add_account(request):
    submitted = False
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_account?submitted=True")
    else:
        form = AccountForm
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request, 'add_account.html', {"form": form, "submitted": submitted})    
    
def home(request): 
    goals = Goal.objects.all()
    accounts = Balance.objects.all()
    return render(request, "home.html", {"goals": goals, "accounts":accounts})

# history timeline of completed goals ordered by date (descending order)
def history(request):
    completed_goals = Goal.objects.filter(status="completed").order_by('-date_completed')
    return render(request, "history.html", {"completed_goals": completed_goals})

def contact(request):
    return render(request, "contact.html")

# this will be the page to view and edit an individual goal
def savings_goal(request, pk):
    goal = Goal.objects.get(pk=pk)
    return render(request, "savings_goal.html", {"goal": goal})
