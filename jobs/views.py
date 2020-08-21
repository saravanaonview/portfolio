from django.shortcuts import render
from .models import Job

# Create your views here.
def Home(request):
    jobs=Job.objects
    return render(request,'jobs/Home.html',{'jobs':jobs})

def login(request):
    return render(request,'jobs/login.html')
