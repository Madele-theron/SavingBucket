from django.urls import path
from .views import dashboard, history, goal

app_name = "savings"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("history/", history, name="history"),
    path("goal/<int:pk>", goal, name="goal"),
]
