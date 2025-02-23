from django.shortcuts import render, get_object_or_404, redirect
from ..models import Blogs
from django.contrib.auth.decorators import login_required

def home(request):
    blogs= Blogs.objects.all()
    return render(request, 'main/home.html', {"blogs": blogs})


@login_required
def create_blog(request):   
    if request.method=="POST":
        title= request.POST.get('title')
        subtitle= request.POST.get('subtitle')
        description= request.POST.get('description')
        image= request.FILES.get("image")
        
        blog= Blogs(title=title, subtitle=subtitle, description=description, image=image, author=request.user)
        blog.save()
        
        return render(request, 'main/home.html')       
        
        

    return render(request, 'main/create_blog.html')

def edit_blog(request):
    return render(request, 'main/edit_blog.html')

def delete_blog(request, id):
    blog= get_object_or_404(Blogs, pk=id)
    if blog.author==request.user:
        blog.delete()
        return redirect("home")
    else:
        return redirect("single")
    

def single_blog(request, id):
    blog= get_object_or_404(Blogs, pk=id)
    return render(request, 'main/single_blog.html', {"blog": blog})