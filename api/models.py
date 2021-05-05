from django.db import models
from django.utils import timezone
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Post(models.Model):

    class PostObjects(models.Manager):
        def get_query_set(self):
            return super().get_query_set.filter(status='published')
    options=[
        ('draft', 'draft'),
        ('published', 'published')
    ]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description= models.CharField(max_length=250)
    content= models.TextField()
    slug= models.SlugField(max_length=250, unique_for_date='published')
    published= models.DateTimeField(default= timezone.now)
    author= models.ForeignKey(User, on_delete= models.CASCADE, related_name='api')
    status = models.CharField(max_length=10, choices=options, default='published')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects =models.Manager()
    postObjects =PostObjects()

    # class Meta:
    #     ordering=('-published')

    def __str__(self):
        return self.title
