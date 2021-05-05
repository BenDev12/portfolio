from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model =Post
        fields = ['id','title', 'description', 'content','slug', 'published','author', 'status','updated_at', 'created_at']
