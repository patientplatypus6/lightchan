
from lib2to3.pgen2 import token
from logging import handlers
from lightone.models import *
from . import utilities
import datetime
from django.contrib.sessions.backends.db import SessionStore
import random

from django.middleware.csrf import get_token


def token_handler(request):
  print("inside token handler")
  try:
    print("csrftoken: %s", request.session['csrftoken'])
  except:
    print("csrftoken not found now_setting")
    request.COOKIES['csrftoken'] = get_token(request)

def handle_clean():
  comments = Comment.objects.all()
  for comment in comments:
    timestamp_now = datetime.datetime.now().timestamp()
    timestamp_db = datetime.datetime.timestamp(comment.created_at)
    dif = timestamp_now - timestamp_db
    print(dif>10000)
    if dif > 10000:
      comment.delete()  

def every_request(get_response):

  def middleware(request):
    
    print("MIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWARE")
    print("MIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWARE")
    print("MIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWARE")
    print('inside the every_request middleware')
    handle_clean()
    token_handler(request)
    print("MIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWARE")
    print("MIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWARE")
    print("MIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWARE")
    response = get_response(request)

    # Code to be executed for each request/response after
    # the view is called.

    return response

  return middleware