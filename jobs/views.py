from django.shortcuts import render
from .models import Job
from blog import views

# Create your views here.
def Home(request):
    jobs=Job.objects
    return render(request,'jobs/Home.html',{'jobs':jobs})

def login(request):
    return render(request,'jobs/login.html')

def bloglink(request):
    return render(request,'blog/Blogthan.html', name = "mudila")
