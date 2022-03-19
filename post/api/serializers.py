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

    
class PostUpdateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'slug',
            'image',
        ]


    def create(self, validated_data):
        print("başarılı")
        return Post.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = 'değiştirildi'
        instance.image = "ornek resim.url"
        instance.save()
        return instance


    # def validate_title(self,value):
    #     if value == "emre":
    #         print("çalışıyor")                                    
    #         raise serializers.ValidationError("Its not valid")   
    #     return value

                                                                        # Validation

    # def validate(self, attrs):
    #     if attrs['title'] == "emre":
    #         raise serializers.ValidationError("Its not valid")
    #     return attrs