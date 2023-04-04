from .serializers import *
from .models import *
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponseRedirect
from .forms import GoalForm, AccountForm, DepositForm


# Create your views here.

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

class GoalList(APIView):
        def get(self, request):
            data = Goal.objects.all()
            return Response(
                GoalSerializer(
                    data, context={"request": request}, many=True).data
            )

        def post(self, request):
            serializer = GoalSerializer(data=request.data)
            data = serializer
            goal = Goal.objects.create(
                name=data["name"],
                description=["description"],
                date_added=data["date_added"],
                cost=data["cost"],
                image=data["image"],
                url_link=data["url_link"],
                status=data["status"],
                account=data["account"],
                date_completed=data["date_completed"],
            )

class BalanceList(APIView):
    def get(self, request):
            data = Balance.objects.all()
            return Response(
                BalanceSerializer(
                    data, context={"request": request}, many=True).data
            )

    def post(self, request):
        serializer = BalanceSerializer(data=request.data)
        data = serializer
        balance = Balance.objects.create(
            name=data["name"],
            amount=["amount"],
        )
    
    
def home(request): # TODO this can be the landing page :) // or just the main over view page??
    goals = Goal.objects.all()
    accounts = Balance.objects.all()
    return render(request, "home.html", {"goals": goals, "accounts":accounts})

def history(request):
    completed_goals = Goal.objects.filter(status="completed")
    return render(request, "history.html", {"completed_goals": completed_goals})

def contact(request):
    return render(request, "contact.html")

# this will be the page to view and edit an individual goal
def savings_goal(request, pk):
    goal = Goal.objects.get(pk=pk)
    return render(request, "savings_goal.html", {"goal": goal})
