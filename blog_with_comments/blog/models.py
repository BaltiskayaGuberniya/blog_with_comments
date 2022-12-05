from django.db import models
    
class Blogpost(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    content = models.TextField(max_length=1024)
    
class Comment(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    content = models.TextField(max_length=1024)
    parent = models.ForeignKey(Blogpost, on_delete=models.CASCADE, null=True)
    