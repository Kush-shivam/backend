from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request,'index.html')

def contact(request):

    return render(request,'contact.html')

def about(request):

    return render(request,'about.html')

def bike(request):

    return render(request,'bike.html')

def car(request):

    return render(request,'car.html')

def mahindra(request):

    return render(request,'mahindra.html')