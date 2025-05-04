from django.urls import path 
from fun_Passenger import views


urlpatterns = [
    path('passList/',views.passenger_list),
    path('passList/<int:pk>',views.passenger_details)
]