from cgitb import lookup
from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = 'post:detail',
        lookup_field = 'slug',
    )
    username = serializers.SerializerMethodField()   #Username'i almak için method 
    # username = serializers.SerializerMethodField(method_name='username_new')   #Username'i almak için method alernatif
    class Meta:
        model = Post
        fields = [
            'username',
            'title',
            'content',
            'image',
            'url',
            'created',
            'modified_by'
            
        ]

    def get_username(self,obj):  #Username'i almak için method tanımlandı
        return str(obj.user.username)

    # def username_new(self,obj):  #Username'i almak için method tanımlandı | Alternatif
    #     return str(obj.user.username)
    



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






    # def create(self, validated_data):
    #     print("başarılı")
    #     return Post.objects.create(**validated_data)


    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = 'değiştirildi'
    #     instance.image = "ornek resim.url"
    #     instance.save()
    #     return instance


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