from sqlite3 import Timestamp
from time import monotonic
from django.db import models
from . import utilities
import uuid

class Board(models.Model):
  id = models.TextField(primary_key=True, unique=True)
  board_name = models.TextField()
  board_description = models.TextField()
  nsfw = models.BooleanField()
  mnemonic = models.TextField(unique=True)
    
class Comment(models.Model): 
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
  clean_id = models.TextField(default=0)
  title = models.TextField()
  content = models.TextField()
  file_name = models.TextField(default="")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  votes = models.IntegerField(default=1)
  mnemonic = models.TextField()
  owner = models.ForeignKey("Board", on_delete=models.CASCADE, null=True, to_field='mnemonic')

class Reply(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
  clean_id = models.TextField(default=0)
  title = models.TextField()
  content = models.TextField()
  file_name = models.TextField(default="")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  votes = models.IntegerField(default=1)
  owner = models.ForeignKey("Comment", on_delete=models.CASCADE, null=True)  