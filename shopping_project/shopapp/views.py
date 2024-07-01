from pyexpat.errors import messages
from urllib import request
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate,login,logout
# Create your views here.



from django.shortcuts import render
from django.views import View
from shopapp.models import Useregister
from django.http import HttpResponse
# Create your views here.

class home(View):
    def get(self,request):
        return render(request,'home.html')
    




class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')
    

    def post(self,request):
        name=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        Useregister.objects.create(user_name=name,email=email,password=password)
        return HttpResponse("registered")
        




class Loginview(View):
    def get(self,request):
        return render(request,'login.html')
    

    def post(self,request):
        uname=request.POST.get("username")
        psw=request.POST.get("password")
        user=authenticate(request,username=uname,password=psw)
        
        if user:
              login(user)
              
              return redirect('main')
        else:
              
              return redirect('home')
        


class Mainpage(View):
    def get(self,request):
        return render(request,'mainpage.html')        