from django.urls import path
from post.api.views import PostListAPIView, PostDetailAPIView, PostDestroyAPIView, PostUpdateAPIView


urlpatterns = [
    path('list', PostListAPIView.as_view(), name='list'),
    path('detail/<slug>', PostDetailAPIView.as_view(), name='detail'),
    path('update/<slug>', PostUpdateAPIView.as_view(), name='update'),
    path('delete/<slug>', PostDestroyAPIView.as_view(), name='delete'),
]