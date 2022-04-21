from django.shortcuts import render

# import Blog Post model
from .models import BlogPost

# Create your views here.

# Home page function
def home(request):
    return render(request, 'home.html', {'posts': BlogPost.objects.all()})