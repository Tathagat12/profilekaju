from django.shortcuts import render,HttpResponse
from home.models import Contact

# Create your views here.
def index(request):
    if request.method =="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        print(name,email,subject,message)
        ins=Contact(name=name,email=email,subject=subject,message=message)
        ins.save()
        print("the data has in db")
        

    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def projects(request):
    return render(request,'projects.html')
def contact(request):
    return render(request,'contact.html')            

           