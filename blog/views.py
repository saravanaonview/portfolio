from django.shortcuts import render
from .models import Blog
# Create your views here.

def Home(request):
    blogs=Blog.objects
    return render(request,'blog/Home.html',{"Blog":blogs})
