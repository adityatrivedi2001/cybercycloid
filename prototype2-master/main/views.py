from django.shortcuts import render,redirect
from .models import contactus, Teammates

# Create your views here.

def homepage(request):
     teammate = Teammates.objects.all()
     return render(request,'main/index.html',{'teammate':teammate})

def services(request):
     return render(request,'main/services.html')

def about(request):
     return render(request,'main/about.html')

def contact12(request):
     if request.method == 'POST':
          email1 = request.POST['email1']
          mess = request.POST['message1']

          cont_obj = contactus(email = email1, text=mess)
          cont_obj.save()
          return redirect('/')
     else:
          return redirect('/')

def contact1(request):
     if request.method == 'POST':
          email1 = request.POST['email1']

          cont_obj = contactus(email = email1)
          cont_obj.save()
          return redirect('/')
     else:
          return redirect('/')

