from django.urls import path
from firstapp import views
from firstapp.models import Emp

urlpatterns = [
    path('emps/',views.employeeview)
]