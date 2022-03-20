from pyexpat import model
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from comment.models import Comment
from post.models import Post
from rest_framework import serializers
from django.contrib.auth.models import User


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created_date']   # exclude haricinde ki tüm fieldları alır.
        # fields = ['user','post','content'] | Alternatif

    def validate(self, attrs):
        if(attrs["parent"]):
            if attrs["parent"].post != attrs["post"]:
                raise serializers.ValidationError("Something went wrong")
        return attrs



class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            ]
        # exclude = ['password']


class PostCommentSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [ 
            'id',
            'title',
            'slug',
        ]





class CommentListSerializer(ModelSerializer):
    replies = SerializerMethodField()
    user = UserSerializer()
    post = PostCommentSerializer()
    class Meta:
        model = Comment
        fields = '__all__'

    def get_replies(self,obj):
        if obj.any_children:
            return CommentListSerializer(obj.children(), many=True).data


class CommentDeleteUpdateSerialier(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'content'
            ]
