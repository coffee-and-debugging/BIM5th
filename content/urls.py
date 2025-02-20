from django.contrib import admin
from django.urls import path
from .views.main_views import home, create_blog, edit_blog, single_blog, delete_blog
from .views.auth_views import login, register

urlpatterns = [
    path('', home, name="home"),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('create/', create_blog),
    path('edit/', edit_blog),
    path('<int:id>/delete/', delete_blog, name="delete"),
    path('<int:id>', single_blog),
]

