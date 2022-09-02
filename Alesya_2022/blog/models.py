from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=30)



class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)#создавать новую дату с экземпляром
    last_modified = models.DateField(auto_now=True)#дата последнего изменения поста
    # categories = models.ManyToManyField('Categories', related_name='post')


class Comment(models.Model):
    author = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)