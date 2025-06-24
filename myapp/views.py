from django.shortcuts import render,redirect
from .models import*
# Create your views here.
def home(request):

    return render(request,'index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phoneno = request.POST['pno']
        email = request.POST['email']
        message = request.POST['message']
        ContactDetails.objects.create(
          name=name,
          phoneno=phoneno,
          email=email,
          messege=message  
        )
        return redirect('/')
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

def mahindra1(request):

    return redirect('/mahindra/#carousel1')

def mahindra2(request):

    return redirect('/mahindra/#carousel2')

def mahindra3(request):

    return redirect('/mahindra/#carousel3')

def mahindra4(request):

    return redirect('/mahindra/#carousel4')

def tata1(request):

    return redirect('/tata/#carousel1')

def tata2(request):

    return redirect('/tata/#carousel2')

def tata3(request):

    return redirect('/tata/#carousel3')

def tata4(request):

    return redirect('/tata/#carousel4')

def royal1(request):

    return redirect('/royal/#carousel1')

def royal2(request):

    return redirect('/royal/#carousel2')

def tvs1(request):

    return redirect('/tvs/#carousel1')

def tvs2(request):

    return redirect('/tvs/#carousel2')

def revolt1(request):

    return redirect('/revolt/#carousel1')

def revolt2(request):

    return redirect('/revolt/#carousel2')

def ola1(request):

    return redirect('/ola/#carousel1')

def tork1(request):

    return redirect('/tork/#carousel1')