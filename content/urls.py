from django.contrib import admin
from django.urls import path
from .views.main_views import home, create_blog, edit_blog, single_blog, delete_blog, about_us
from .views.auth_views import login, register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('create/', create_blog, name='create'),
    path('edit/<int:id>/', edit_blog, name='edit_blog'),
    path('<int:id>/delete/', delete_blog, name="delete"),
    path('<int:id>', single_blog, name="single"),
    path('about/', about_us, name='about'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

