from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    Title = models.CharField(max_length=200)
    description = models.TextField()
    blog_image = models.ImageField(upload_to='blog_images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



    
