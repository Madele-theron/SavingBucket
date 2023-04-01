from django.urls import path
from .views import home, overview, savings_goal, history, contact

app_name = "savings"

urlpatterns = [
    path('', home, name="home"),
    path('overview', overview, name="overview"),
    path('goal/<int:pk>', savings_goal, name="savings_goal"),
    path('history', history, name="history"),
    path('contact', contact, name="contact"),
] 