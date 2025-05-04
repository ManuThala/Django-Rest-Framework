from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def employeeview(request):
    emp={
        'id':1,
        'name':'manu',
        'sal':10000
    }
    return JsonResponse(emp)