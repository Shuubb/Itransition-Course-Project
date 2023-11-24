from django.db import models
from auth_api.models import CustomUser

class Collection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_link = models.URLField(null=True, blank=True)
    TOPIC_CHOICES = [
        ('Books', 'Books'),
        ('Whiskeys', 'Whiskeys'),
        ('Watches', 'Whatches'),
        ('Jewelary', 'Jewelary'),   
        ]
    topic = models.CharField(max_length=10, choices=TOPIC_CHOICES)

    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Item(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    tags = models.ManyToManyField('Tag')
    
    optional_fields = models.ManyToManyField('OptionalField')

    likes = models.ManyToManyField('Like', related_name='liked_items')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class OptionalField(models.Model):
    name = models.CharField(max_length=50, unique=True)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.text}"
    
class Like(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
