from rest_framework import serializers
from .models import Collection, Item, Tag, Comment, Topic

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
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
    collection_name = serializers.ReadOnlyField(source='collection.name')

    def create(self, validated_data):
        collection_id = self.context['request'].data['collection']
        validated_data['collection'] = Collection.objects.get(id=collection_id)
        return super().create(validated_data)

    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ['collection']

class CollectionSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    def create(self, validated_data):
        validated_data['creator'] = self.context['request'].user

        topic = self.context['request'].data['topic']
        validated_data['topic'] = Topic.objects.get(id=topic)
        return super().create(validated_data)

    class Meta:
        model = Collection
        fields = '__all__'
        read_only_fields = ['creator', 'topic']
