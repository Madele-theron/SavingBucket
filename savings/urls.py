from django.urls import path
from .views import *
from . import views

app_name = "savings"

urlpatterns = [
    path('', home, name="home"),
    path('goal/<int:pk>', savings_goal, name="savings-goal"),
    path('history', history, name="history"),
    path('contact', contact, name="contact"),
    path("add_goal", views.add_goal, name="add-goal"),
    path("add_account", views.add_account, name="add-account"),
    path("deposit", views.deposit, name="deposit"),
    path('update_goal/<int:goal_id>', views.update_goal, name="update-goal"),
]