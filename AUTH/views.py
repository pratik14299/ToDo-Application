from django.http import HttpResponse
from django.shortcuts import render,redirect
from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def registratiomform(request):
    form = UserCreationForm
    template_name = "auth/register.html"
    context = {'form':form}
    print(request.method)
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User Created...")
        else:
            return HttpResponse("Not Valid")
    
    return render(request,template_name,context)


def loginUser(request):
    template_name = "auth/login.html"
    print(request.method)
    if request.method == "POST":
        un = request.POST.get("un")
        password = request.POST.get("password")
        user = authenticate(username = un,password=password)   
        print(f'{user}')
        if user is not None: 
            login(request, user)      
            return redirect('show_url')  
        # print("Values are : ",un," and ",password)
    context = {}
    return render(request,template_name,context)


def logoutView(request):
    logout(request)
    return redirect("login_url")

