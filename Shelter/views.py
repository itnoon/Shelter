
from atexit import register
from timeit import repeat
from django.shortcuts import render
from django.http import HttpResponse
from Shelter.models import Contact
from Shelter.models import About
from Shelter.models import Register
from Shelter.models import Login
def home(request):
    return render(request,'home.html')
def about(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        about=About()
        about.username=username
        about.password=password
        about.save()
        return HttpResponse('<h1>Thanks for visit</h1>')
    return render(request,'about.html')
def contact(request):
    if request.method =='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        contact=Contact()
        contact.name=name
        contact.phone=phone
        contact.email=email
        contact.save()
        return HttpResponse('<h1>Thanks for contact</h1>')
    return render(request,'contact.html')
def login(request):
    if request.method =='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        comments=request.POST.get('comments')
        login=Login()
        login.name=name
        login.phone=phone
        login.email=email
        login.comments=comments
        login.save()
        return HttpResponse('<h1>Thanks for Login</h1>')
    return render(request,'login.html')
def register(request):
     if request.method =='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        repeatpassword=request.POST.get('repeatpassword')
        register=Register()
        
        register.email=email
        register.password=password
        register.repeatpassword=repeatpassword
        register.save()
        return HttpResponse('<h1>Thanks for your registration</h1>')
     return render(request,'register.html')
def showdata(request):
    contacts=Contact.objects.all()
    registers=Register.objects.all()
    #for i in contacts:
       # print(i.name,i.phone,i.email)
    data={'Contact':contacts}
   
    return render(request,'showdata.html',data)

    
    #for i in contacts:
       # print(i.name,i.phone,i.email)
    
    
# Create your views here.
