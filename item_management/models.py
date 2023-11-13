from django.db import models
from auth_api.models import CustomUser

class Topic(models.Model):
    id = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.id

class Collection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    image_link = models.URLField(null=True, blank=True)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Item(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    tags = models.ManyToManyField('Tag')
    comments = models.ManyToManyField('Comment', related_name='item_comments')
    likes = models.ManyToManyField('Like', related_name='liked_items')

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.text}"
    
class Like(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

