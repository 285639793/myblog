from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class BlogArticles(models.Model):
    title = models.CharField(mx_length=300)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,related_name="blog_posts")
    body = models.TextField()
    publish_time = models.DateTimeField(default= timezone.now)

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return  self.title