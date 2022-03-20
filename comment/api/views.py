from cgitb import lookup
from urllib import request
from rest_framework.mixins import DestroyModelMixin
from rest_framework.generics import (
                                    CreateAPIView,
                                    ListAPIView,                                    
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


# #class CommentDeleteAPIView(DestroyAPIView, UpdateModelMixin, RetrieveModelMixin):  #ModelMixin Alternatif
#     queryset = Comment.objects.all()
#     serializer_class = CommentDeleteUpdateSerialier
#     lookup_field = 'pk'
#     permission_class = [IsOwner]

#     # def put(self, request, *args, **kwargs):
#     #     return self.update(request, *args, **kwargs)
#                                                                     #ModelMixin Alternatif
#     # def get(self, request, *args, **kwargs):
#     #     return self.retrieve(request, *args, **kwargs)


class CommentUpdateAPIView(UpdateAPIView, RetrieveAPIView, DestroyModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteUpdateSerialier
    lookup_field = 'pk'
    permission_class = [IsOwner]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer 
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

