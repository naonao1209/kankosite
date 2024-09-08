from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    def publish(self):
        """投稿を公開するためのメソッド"""
        self.published_date = timezone.now()
        self.is_published = True
        self.save()