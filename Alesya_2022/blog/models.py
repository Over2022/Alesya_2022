from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=30)



class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_on = models.DataField(auto_now_add=True)
    last_modified = models.DataField(auto_now=True)
    categories = models.ManyToManyField('Categories', related_name='post')

