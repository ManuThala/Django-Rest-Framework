from django.shortcuts import render
from . models import Customer,Order
from nestedapp.serializers import CustomerSerializer,OrderSerializer
from rest_framework import viewsets
from rest_framework.decorators import APIView


# Create your views here.


class orderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class customerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
