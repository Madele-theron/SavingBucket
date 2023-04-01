from django.shortcuts import render
from .models import Goal, Balance, Deposit


# Create your views here.
def dashboard(request):
    return render(request, "base.html")


def history(request):
    completedgoals = Goal.objects.all()
    return render(
        request, "savings/history_list.html", {"completedgoals": completedgoals}
    )


# individual goals (to edit them)
def goal(request, pk):
    goal = Goal.objects.get(pk=pk)
    return render(request, "savings/goal.html", {"goal": goal})
