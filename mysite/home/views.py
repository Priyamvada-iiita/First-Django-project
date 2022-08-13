from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def home(request):
    context = {
        "variable" :"MIIII channn"
    }
    messages.success(request, 'This is a text message')
    return render(request , 'index.html', context)
       # return HttpResponse("this is homepage")
def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(name =name, email =email, phone =email, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request , 'contact.html')
    #return HttpResponse("this is homepage")
 
def about(request):
    return render(request , 'about.html')
    #return HttpResponse("this is homepage")
def service(request):
    return render(request , 'services.html')
    #return HttpResponse("this is homepage")

def wallet(request):
    return HttpResponse("this is homepage")
def order(request):
    return HttpResponse("this is homepage")