from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        mail = request.POST['mail']
        uname = request.POST['username']
        pwd = request.POST['pwd']
        cpwd = request.POST['cpwd']
        if pwd == cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username taken")
                return render(request,'register.html')
            elif User.objects.filter(email=mail).exists():
                messages.info(request,"Email already exists")                
                return render(request,'register.html')
            else:    
                user = User.objects.create_user(password=pwd, first_name=fname, last_name=lname, email=mail, username=uname)
                user.save()
                messages.info(request,"Registered successfully")
                return redirect('/')
                #return render(request,'login.html')
        else:
            messages.error(request,"password not mathcing")

    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('usname')
        pwd = request.POST.get('pwd')
        user  = auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request, user)
            return render(request,'all.html')
        else:
            messages.info(request, 'Invalid Credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

    return render(request,'login.html')
