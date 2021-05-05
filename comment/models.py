from django.db import models
from user.models import User

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    body = models.TextField()
    slug =models.SlugField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering=('-created_at')

    def __str__(self):
        return self.body

    
