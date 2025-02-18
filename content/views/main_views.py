from django.shortcuts import render, get_object_or_404
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
        
        blog= Blogs(title=title, subtitle=subtitle, description=description, image=image)
        blog.save()
        
        return render(request, 'main/create_blog.html')       
        
        

    return render(request, 'main/create_blog.html')

def edit_blog(request):
    return render(request, 'main/edit_blog.html')

def single_blog(request, id):
    blog= get_object_or_404(Blogs, pk=id)
    return render(request, 'main/single_blog.html', {"blog": blog})