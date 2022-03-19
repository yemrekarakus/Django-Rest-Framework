from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView) 
from .permissions import IsOwner   #Custom permission
from post.api.permissions import IsOwner
from post.models import Post
from post.api.serializers import PostSerializer, PostUpdateCreateSerializer
from rest_framework.permissions import (
    IsAuthenticated, 
    IsAdminUser
)


class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title','content']

    def get_queryset(self):       #Filtreleme                        
        query_set = Post.objects.filter(draft=False)
        return query_set 

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
    serializer_class = PostUpdateCreateSerializer   
    lookup_field = 'slug'
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        serializer.save(modified_by = self.request.user)  # düzenleme yapan userı göstermek için


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateCreateSerializer
    permission_classes = [IsAuthenticated]  # Yetkili olmayan kullanıcıların girememesi için

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

 
