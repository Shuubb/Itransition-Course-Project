import json
from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Collection, Item, Tag, Comment
from .serializers import CollectionSerializer, ItemSerializer, TagSerializer, CommentSerializer
from django.db.models import Q


class TopicListView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        topic_touples = Collection.TOPIC_CHOICES
        topics = [topic_touple[0] for topic_touple in topic_touples]
        return JsonResponse(topics, safe=False)

class TagListCreateView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_permissions(self):
        return [AllowAny()] if self.request.method == 'GET' else [IsAuthenticated()]

class CommentListCreateView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        return [AllowAny()] if self.request.method == 'GET' else [IsAuthenticated()]

# Item Handlers
class ItemListCreateView(ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        params = self.request.query_params

        if 'search' in params:
            search_text = params.get('search')
            query = Q()

            query |= Q(tags__name__icontains=search_text)
            query |= Q(name__icontains=search_text)
            query |= Q(collection__name__icontains=search_text)

            queryset = queryset.filter(query).distinct()
        if 'collection' in params:
            collection = params.get('collection')
            queryset = queryset.filter(collection=collection)
        if 'subset' in params:
            start, end = json.loads(params.get('subset'))
            queryset = queryset.order_by('-id')
            print(queryset)
            queryset = queryset[start:end]

        return queryset

    def get_permissions(self):
        return [AllowAny()] if self.request.method == 'GET' else [IsAuthenticated()]

class ItemListChangeView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    def perform_destroy(self, instance):
        if self.request.user == instance.creator or self.request.user.is_admin:
            super().perform_destroy(instance)
        else:
            raise PermissionDenied("You do not have permission to delete this collection.")

    def perform_update(self, serializer):
        if self.request.user == serializer.instance.creator or self.request.user.is_admin:
            serializer.save()
        else:
            raise PermissionDenied("You do not have permission to modify this collection.")
        
    def get_permissions(self):
        return [AllowAny()] if self.request.method == 'GET' else [IsAuthenticated()]




# Collection Handlers
class CollectionCreateView(ListCreateAPIView):
    serializer_class = CollectionSerializer

    def get_queryset(self):
        queryset = Collection.objects.all()
        params = self.request.query_params

        
        if 'user' in params:
            user = params.get('user')
            queryset = queryset.filter(creator_id=user)
        if 'subset' in params:
            start, end = json.loads(params.get('subset'))
            queryset = queryset.order_by('-id')
            queryset = queryset[start:end]

        return queryset

    def get_permissions(self):
        return [AllowAny()] if self.request.method == 'GET' else [IsAuthenticated()]


class CollectionChangeView(RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def perform_destroy(self, instance):
        if self.request.user == instance.creator or self.request.user.is_admin:
            super().perform_destroy(instance) 
        else:
            raise PermissionDenied("You do not have permission to delete this collection.")

    def perform_update(self, serializer):
        if self.request.user == serializer.instance.creator or self.request.user.is_admin:
            serializer.save()
        else:
            raise PermissionDenied("You do not have permission to modify this collection.")
        
    def get_permissions(self):
        return [AllowAny()] if self.request.method == 'GET' else [IsAuthenticated()]

