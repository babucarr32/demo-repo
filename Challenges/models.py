from distutils.command.upload import upload
import profile
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=1500)
    description = models.TextField(max_length=6000000)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=100)
    comments = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    pubDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comments