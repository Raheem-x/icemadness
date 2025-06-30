from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import contact
from django.contrib import messages
# Create your views here.
def index(request):
  #messages.success(request,"this is a test message")
  return render(request,"index.html")
  #return HttpResponse("this is homepage")
def about(request):
  return render(request,"about.html")
def services(request):
  return render(request,"services.html")
def contact_view(request):
  if request.method == "POST":
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email =request.POST.get('email')
    desc =request.POST.get('desc')
    contact_entry = contact(name=name, phone=phone, email=email, desc=desc, date=datetime.today().date())
    contact_entry.save()
    messages.success(request, "your message has been sent .")
  return render(request,"contact.html")