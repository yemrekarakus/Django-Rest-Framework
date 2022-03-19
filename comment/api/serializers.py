from rest_framework.serializers import ModelSerializer
from comment.models import Comment
from rest_framework import serializers

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