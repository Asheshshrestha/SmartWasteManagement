from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Blogs(models.Model):
    
    title= models.CharField(max_length=255)
    article = models.TextField()
    count = models.IntegerField(default=0)
    
    cover_image= models.ImageField(upload_to='uploads/blogs',null=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural ='Employee Blogs'
  