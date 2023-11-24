from django.urls import path
from .views import CollectionChangeView, CollectionCreateView, CommentChangeView, ItemListChangeView, TagListCreateView, CommentListCreateView, ItemListCreateView, TopicListView
urlpatterns = [
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('topics/', TopicListView.as_view(), name='topic-list'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentChangeView.as_view(), name='comment-change'),
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemListChangeView.as_view(), name='item-change'),
    path('collections/', CollectionCreateView.as_view(), name='collection-list-create'),
    path('collections/<int:pk>/', CollectionChangeView.as_view(), name='collection-change'),
]