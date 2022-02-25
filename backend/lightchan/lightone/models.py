from sqlite3 import Timestamp
from django.db import models
from . import utilities
import uuid

class Comment(models.Model): 
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  clean_id = models.TextField(default=0)
  title = models.TextField()
  content = models.TextField()
  file_name = models.TextField(default="")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  votes = models.IntegerField(default=1)

class Reply(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  clean_id = models.TextField(default=0)
  title = models.TextField()
  content = models.TextField()
  file_name = models.TextField(default="")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  votes = models.IntegerField(default=1)
  owner = models.ForeignKey("Comment", on_delete=models.CASCADE, null=True)