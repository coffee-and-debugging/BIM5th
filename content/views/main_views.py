from django.shortcuts import render
from ..models import Blogs
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'main/home.html')


@login_required
def create_blog(request):   
    if request.method=="POST":
        title= request.POST.get('title')
        subtitle= request.POST.get('subtitle')
        description= request.POST.get('description')
        image= request.FILES.get("image")
        
        blog= Blogs(title=title, subtitle=subtitle, description=description, image=image)
        blog.save()
        
        return render(request, 'main/create_blog.html')       
        
        

    return render(request, 'main/create_blog.html')

def edit_blog(request):
    return render(request, 'main/edit_blog.html')

def single_blog(request):
    return render(request, 'main/single_blog.html')