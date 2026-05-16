from django.contrib import admin
from django.urls import path, include
from todo import views as todo_views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('blog/', include('todo.urls')),   
    path('about_me/', todo_views.about_me), 
    path('', todo_views.landing),          
]