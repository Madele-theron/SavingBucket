from django.urls import path
from .views import dashboard

app_name = "savings"

urlpatterns = [
    path("", dashboard, name="dashboard"),
]
