from sqlite3 import Timestamp
from django.db import models
from . import utilities
import uuid

class Comment(models.Model): 
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.TextField()
  content = models.TextField()
  file_name = models.TextField(default="")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Reply(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.TextField()
  content = models.TextField()
  file_name = models.TextField(default="")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  owner = models.ForeignKey("Comment", on_delete=models.SET_NULL, null=True)