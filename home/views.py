from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
    context = {
        "name":"Aditya",
        "age":22
    }
    messages.success(request,"this is a test message")
    return render(request, "index.html",context)

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")

        contact = Contact(name=name, email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Form submitted successfully")

    return render(request, "contact.html")