
from lib2to3.pgen2 import token
from logging import handlers
from lightone.models import *
from . import utilities
import datetime
from django.contrib.sessions.backends.db import SessionStore
import random
import logging
from django.middleware.csrf import get_token
from django.http.response import JsonResponse
import requests


def token_handler(request):
  logging.info("inside token_handler")
  try:
    logging.info("csrftoken: %s", request.session['csrftoken'])
  except:
    logging.info("csrftoken not found now_setting")
    request.COOKIES['csrftoken'] = get_token(request)

def handle_clean():
  logging.info("inside handle_clean")
  comments = Comment.objects.all()
  for comment in comments:
    logging.info("value of comment: %s", comment)
    timestamp_now = datetime.datetime.now().timestamp()
    timestamp_db = datetime.datetime.timestamp(comment.created_at)
    dif = timestamp_now - timestamp_db
    logging.info(dif>10000)
    if dif > 10000:
      comment.delete()  

def inspect(request):
  logging.info("request.path: %s", request.path)
  # logging.info("request.pathinfo: %s", request.pathinfo)
  logging.info("request.method: %s", request.method)
  logging.info("request.content_type %s", request.content_type)
  logging.info("request.content_params %s", request.content_params)
  logging.info("request.COOKIES %s", request.COOKIES)
  logging.info("request.META %s", request.META)
  logging.info("request.headers %s", request.headers)

def every_request(get_response):

  def middleware(request):
  
    logging.info("MIDDLEWARE")
    logging.info('inside the every_request middleware')
    handle_clean()
    token_handler(request)
    # inspect(request)
    logging.info("MIDDLEWARE")
    response = get_response(request)

    return response

  return middleware