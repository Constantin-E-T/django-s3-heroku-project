from distutils.command.upload import upload
from django.db import models

# Create your models here.

# Blog post model
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.title