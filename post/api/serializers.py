from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'user',
            'title',
            'content',
            'image',
            'slug',
            'created',
            'modified_by'
            
        ]