from django.shortcuts import render,HttpResponse,redirect
from .forms import ToDoForm
from .models import TodoTask 
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login_url')
def AddTask(request):
    print(request.user)
    form = ToDoForm()
    print(request.method)
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
        else:
            return HttpResponse("<h1>From Not Valid</h1>")    
    template_name =  "app/AddTask.html"
    context = { 'form' : form}
    return render(request,template_name,context)

@login_required(login_url='login_url') 
def ShowTask(request):
    obj = TodoTask.objects.all()
    template_name = "app/ShowTask.html"
    context = {"data":obj}
    # print(context)
    return render(request,template_name,context)

# def updateTask(request,id):
#     print(id)
#     print(request.method)
#     obj = TodoTask.objects.get( id = id)
#     form = ToDoForm(instance=obj)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#     template_name = 'app/AddTask.html'
#     context = {'form' : form}
#     return render(request,template_name,context)

@login_required(login_url='login_url') 
def updateTask(request, id):
    print(request.user)
    obj = TodoTask.objects.get(id=id)
    form = ToDoForm(instance=obj)

    if request.method == "POST":
        form = ToDoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
        else:
            # Form is not valid, render the template with the form and errors
            template_name = "app/AddTask.html"
            context = {"form": form}
            return render(request, template_name, context)

    # Render the template with the form for both GET and valid POST requests
    template_name = "app/AddTask.html"
    context = {"form": form}
    return render(request, template_name, context)

@login_required(login_url='login_url') 
def DeleteTask(request,id):
    obj = TodoTask.objects.get(id = id)
    print(obj)
    print(request.method)
    obj.delete()
    return redirect("show_url")