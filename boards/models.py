from django.db import models
from django.contrib.auth.models import User

class Board(models.Model) :
    name = models.CharField(max_length=50, unique = True)
    description = models.CharField(max_length=150)

class Topic(models.Model) :
    Subject = models.CharField(max_length=255)
    Board = models.ForeignKey(Board, related_name = 'topics', on_delete = models.CASCADE)
    created_by = models.ForeignKey(User, related_name = 'topic', on_delete = models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)

class Post(models.Model) :
    message = models.TextField(max_length=400)
    topic = models.ForeignKey(Topic, related_name='Posts', on_delete = models.CASCADE)
    created_by = models.ForeignKey(User, related_name = 'Posts', on_delete = models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)
    


# Create your models here.
