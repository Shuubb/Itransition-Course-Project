from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Collection, Item, Tag, Comment, Topic
from .serializers import CollectionSerializer, ItemSerializer, TagSerializer, CommentSerializer, TopicSerializer

class TopicListView(ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class TagListCreateView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class CommentListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# Item Handlers
class ItemListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemListChangeView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Item.objects.all()
    serializer_class = ItemSerializer



# Collection Handlers
class CollectionCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class CollectionChangeView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

