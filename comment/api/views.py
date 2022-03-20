from cgitb import lookup
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from comment.api.serializers import CommentCreateSerializer, CommentListSerializer, CommentDeleteUpdateSerialier
from comment.models import Comment
from rest_framework.permissions import IsAuthenticated
from comment.api.permissions import IsOwner


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer 


class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteUpdateSerialier
    lookup_field = 'pk'
    permission_class = [IsOwner]


class CommentUpdateAPIView(UpdateAPIView):
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

