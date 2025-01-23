from django.shortcuts import render
from ..models import Blogs

def home(request):
    return render(request, 'main/home.html')

def create_blog(request):   
    if request.method=="POST":
        title= request.POST.get('title')
        subtitle= request.POST.get('subtitle')
        description= request.POST.get('description')
        
        blog= Blogs(title=title, subtitle=subtitle, description=description)
        blog.save()
        
        return render(request, 'main/create_blog.html')       
        
        

    return render(request, 'main/create_blog.html')

def edit_blog(request):
    return render(request, 'main/edit_blog.html')

def single_blog(request):
    return render(request, 'main/single_blog.html')