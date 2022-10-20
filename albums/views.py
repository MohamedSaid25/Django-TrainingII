from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def roma(request):
    return HttpResponse("ROMA is HERE")
