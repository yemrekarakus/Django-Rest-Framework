from cgitb import lookup
from rest_framework.generics import (
                                    CreateAPIView,
                                    ListAPIView,
                                    DestroyAPIView,
                                    UpdateAPIView,
                                    RetrieveAPIView,
                                    )   
from comment.api.serializers import (
                                    CommentCreateSerializer,
                                    CommentListSerializer,
                                    CommentDeleteUpdateSerialier,
                                    )
from comment.models import Comment
from rest_framework.permissions import IsAuthenticated
from comment.api.permissions import IsOwner
from comment.api.pagination import CommentPagination


class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer 
    pagination_class = CommentPagination

    def get_queryset(self):
        queryset = Comment.objects.filter(parent = None)
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(post = query)
        return queryset


class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteUpdateSerialier
    lookup_field = 'pk'
    permission_class = [IsOwner]


class CommentUpdateAPIView(UpdateAPIView, RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteUpdateSerialier
    lookup_field = 'pk'
    permission_class = [IsOwner]


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer 
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

