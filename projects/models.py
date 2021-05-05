from django.db import models
from django.utils import timezone
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class Project(models.Model):
    class PostProject(models.Manager):
        def get_query_set(self):
            return super().get_query_set.filter('-created_at')
       
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description= models.CharField(max_length=250)
    content= models.TextField()
    link = models.CharField(max_length=500)
    slug= models.SlugField(max_length=250, unique_for_date='published')
    author= models.ForeignKey(User, on_delete= models.CASCADE, related_name='author')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects =models.Manager()
    postProjects =PostProject()
