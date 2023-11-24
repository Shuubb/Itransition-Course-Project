import json
from rest_framework import serializers
from .models import Collection, Item, OptionalField, Tag, Comment
from rest_framework.exceptions import PermissionDenied


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class OptionalFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionalField
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    optional_fields = OptionalFieldSerializer(many=True, read_only=True)
    collection_name = serializers.ReadOnlyField(source='collection.name')

    def create(self, validated_data):
        collection_id = self.context['request'].data['collection']
        collection = Collection.objects.get(id=collection_id)
        if collection.creator != self.context['request'].user:
            raise PermissionDenied("You do not have permission to add items to this collection.")
        validated_data['collection'] = collection

        validated_data['creator'] = self.context['request'].user

        tags_data_json = self.context['request'].data['tags']
        tags_data = json.loads(tags_data_json)

        validated_data['tags'] = []
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_data)
            validated_data['tags'] += [tag]
        
        return super().create(validated_data)

    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ['collection', 'creator']

class CollectionSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    def create(self, validated_data):
        validated_data['creator'] = self.context['request'].user
        return super().create(validated_data)

    class Meta:
        model = Collection
        fields = '__all__'
        read_only_fields = ['creator']
