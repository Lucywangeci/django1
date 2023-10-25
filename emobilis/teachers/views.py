from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return HttpResponse("welcome to emobilis")

def about(request):
    return HttpResponse("about emobilis")

def Contact(request):
    return HttpResponse("Contact page")

def Help(request):
    return HttpResponse("Help")