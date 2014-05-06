from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  author = models.ForeignKey(User, editable=False)
  title = models.CharField(max_length = 100)
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  slug = models.SlugField(unique=True)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ['-created_at']
