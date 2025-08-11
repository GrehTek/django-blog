from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class BlogPost(models.Model):
  blogpost_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
  blogpost_title = models.CharField(max_length=200)
  blogpost_text = models.TextField()
  blogpost_author = models.CharField(max_length=50)
  blogpost_likes = models.IntegerField(default=0)
  blogpost_comments = models.IntegerField(default=0)
  blogpost_shares = models.IntegerField(default=0)
  blogpost_created_at = models.DateTimeField(default=timezone.now)

  def __strt__(self):
    return self.blogpost_title


class BlogComment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
  post_id = models.CharField(max_length=10)
  comment = models.CharField(max_length=500)
  timestamp = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.comment


class BlogLike(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
  post_id = models.CharField(max_length=10)

  def __str__(self):
    return self.post_id