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

def ola(request):

    return render(request,'ola.html')

def revolt(request):

    return render(request,'revolt.html')

def royal(request):

    return render(request,'royal.html')

def tata(request):

    return render(request,'tata.html')

def tork(request):

    return render(request,'tork.html')

def tvs(request):

    return render(request,'tvs.html')
