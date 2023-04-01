from django.shortcuts import render

# Create your views here.
def home(request): # this can be the landing page :)
    return render(request, "home.html")

def overview(request):
    return render(request, "overview.html")

def history(request):
    return render(request, "history.html")

def contact(request):
    return render(request, "contact.html")

def savings_goal(request):
    return render(request, "savings_goal.html")