from rest_framework.generics import (
    ListAPIView, RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView) 
from .permissions import IsOwner   #Custom permission
from post.api.permissions import IsOwner
from post.models import Post
from post.api.serializers import PostSerializer
from rest_framework.permissions import (
    IsAuthenticated, 
    IsAdminUser
)


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all() 
    serializer_class = PostSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class PostDestroyAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        serializer.save(modified_by = self.request.user)  # düzenleme yapan userı göstermek için


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # Yetkili olmayan kullanıcıların girememesi için


    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    


 
