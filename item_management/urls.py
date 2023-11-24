from django.urls import path
from .views import CollectionChangeView, CollectionCreateView, ItemListChangeView, TagListCreateView, CommentListCreateView, ItemListCreateView, TopicListView
from rest_framework.permissions import IsAuthenticated

urlpatterns = [
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('topics/', TopicListView.as_view(), name='topic-list'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemListChangeView.as_view(), name='item-change'),
    path('collections/', CollectionCreateView.as_view(), name='collection-list-create'),
    path('collections/<int:pk>/', CollectionChangeView.as_view(), name='collection-change'),
]