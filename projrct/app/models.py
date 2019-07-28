from django.db import models

class Board(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField(null = True)

class Comment(models.Model):
    board = models.ForeignKey('app.Board', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()