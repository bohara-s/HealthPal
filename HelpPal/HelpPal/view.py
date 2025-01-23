from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")
def symptom(request):
     return render(request,"symptom.html")
def first_aid(request):
    return render(request,"first_aid.html")
def login(request):
    return render(request,"login.html")
def signin(request):
    return render(request,"signin.html")