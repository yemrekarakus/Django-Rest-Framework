from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView)
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from post.api.paginations import PostPagination 
from .permissions import IsOwner   #Custom permission
from post.api.permissions import IsOwner
from post.models import Post
from post.api.serializers import PostSerializer, PostUpdateCreateSerializer
from rest_framework.permissions import (
    IsAuthenticated, 
    IsAdminUser
)


class PostListAPIView(ListAPIView, CreateModelMixin):
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title','content']
    pagination_class = PostPagination

    def get_queryset(self):       #Filtreleme                        
        query_set = Post.objects.filter(draft=False)
        return query_set 

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class PostUpdateAPIView(RetrieveUpdateAPIView, DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostUpdateCreateSerializer   
    lookup_field = 'slug'
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        serializer.save(modified_by = self.request.user)  # düzenleme yapan userı göstermek için

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateCreateSerializer
    permission_classes = [IsAuthenticated]  # Yetkili olmayan kullanıcıların girememesi için


    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

 
