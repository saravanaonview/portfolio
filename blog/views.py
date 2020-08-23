from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.

def Home(request):
    blogs=Blog.objects
    return render(request,'blog/Blogthan.html',{"Blogdf":blogs})

def sepview(request, blog_id):
    sep_view_ob= get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/sep_number_view.html',{"single_sep_view":sep_view_ob})
