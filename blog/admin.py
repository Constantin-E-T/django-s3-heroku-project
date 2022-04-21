from django.contrib import admin

#import BogPost model
from .models import BlogPost

# Register your models here to admin page
admin.site.register(BlogPost)