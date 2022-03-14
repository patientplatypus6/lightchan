from email.mime import image
from fileinput import filename
from importlib.metadata import files
from linecache import checkcache
from tabnanny import check
from django.http import HttpResponse
from django.http.response import JsonResponse
import json    
from lightone.models import *
from . import utilities

from django.core import serializers
from django.core.files.storage import FileSystemStorage
from django.conf import settings

import logging
import requests

def check_captcha(request):
  logging.info("inside check captcha")
  captcha = request.COOKIES.get("captcha")
  url = 'https://www.google.com/recaptcha/api/siteverify'
  myobj = {
    'secret': settings.RECAPTCHA_KEY,
    'response': captcha
  }
  x = requests.post(url, data = myobj)
  xjson = x.json()
  logging.info("value of xjson %s: ", xjson)
  return xjson['success']

def vote_handler(request, id, type_val):

  logging.info("inside vote_handler")

  util = utilities.Utilites()
  body = json.loads(request.body)

  upvote = body['upvote']
  downvote = body['downvote']
  votedelta = upvote*1+downvote*-1
  votename = "upvote" if upvote else "downvote"
  votedelta_sess = str(id)+"vote"
  votename_sess = str(id)+"votename"

  def set_votes(votedelta, votename):
    logging.info("inside set_votes")
    logging.info("value of type_val %s: ", type_val)
    request.session[votedelta_sess] = votedelta
    request.session[votename_sess] = votename
    request.session[str(id)+"/vote/"+votename] = votedelta

    if type_val == 'comment':
      type_obj = Comment.objects.all().filter(clean_id=id)[0]
    elif type_val == 'reply':
      type_obj = Reply.objects.all().filter(clean_id=id)[0]
    new_votes = type_obj.votes + votedelta
    type_obj.votes = new_votes
    type_obj.save()
    return new_votes

  try: 
    prev_name = request.session[votename_sess]
    
    if prev_name == "upvote" and upvote:
      logging.info("if 1")
      votename = "base"
      votedelta = -1
    elif prev_name == "upvote" and downvote:
      logging.info("if 2")
      votename = "downvote"
      votedelta = -2
    elif prev_name == "downvote" and upvote:
      logging.info("if 3")
      votename = "upvote"
      votedelta = 2
    elif prev_name == "downvote" and downvote:
      logging.info("if 4")
      votename = "base"
      votedelta = 1
    elif prev_name == "base" and upvote:
      logging.info("if 5")
      votename = "upvote"
      votedelta = 1
    elif prev_name == "base" and downvote:
      logging.info("if 6")
      votename = 'downvote'
      votedelta = -1

    logging.info("before return_comment_reply")
    new_votes = set_votes(votedelta, votename)
    logging.info("value of return_comment_reply: %s", new_votes)
    # return util.jsonresponse({'votes': new_votes})
    return new_votes
  except: 
    new_votes = set_votes(votedelta, votename)
    # return util.jsonresponse({'votes': new_votes})
    return new_votes

def retrieve_comments_replies(index, board_mnemonic):
  board_val = Board.objects.all().filter(mnemonic=board_mnemonic)[0]
  comments = Comment.objects.all().filter(owner=board_val).order_by('-created_at')
  comment_data = json.loads(serializers.serialize('json', comments))
 
  return_data = []
  count = 0
  for comment in comment_data:
    replies = Reply.objects.all().filter(owner_id=comment['pk']).order_by("-created_at")[:index]
    comment['pk'] = 'PRIVATE'
    replies_data = json.loads(serializers.serialize('json', replies))
    countr = 0
    for reply in replies_data:
      reply['pk'] = 'PRIVATE'
      countr+=1
    return_data.append({
      'comment': comment,
      'replies': replies_data 
    })
    count+=1
  return return_data

def retrieve_comment_replies(comment_id):
  parent_comment = Comment.objects.all().filter(clean_id=comment_id)
  replies = Reply.objects.all().filter(owner_id=parent_comment[0].id).order_by("-created_at")
  parent_comment_data = json.loads(serializers.serialize('json', parent_comment))
  replies_data = json.loads(serializers.serialize("json", replies))

  parent_comment_data[0]['pk'] = 'PRIVATE'
  count = 0
  for reply in replies_data:
    replies_data[count]['pk'] = 'PRIVATE'
    count+=1
  
  return_data = {
    "comment": parent_comment_data[0], 
    "replies": replies_data
  }
  
  return return_data

def reply(request, incoming_id):
  util = utilities.Utilites()
  if request.method == 'PUT':
    new_votes = vote_handler(request, incoming_id, "reply")
    logging.info('value of new_votes before return: %s', new_votes)
    return util.jsonresponse({'votes': new_votes})
  if request.method=="POST":
    logging.info("inside reply before captcha_bool")
    captcha_bool = check_captcha(request)
    if captcha_bool: 
      all_comments = Comment.objects.all()
      parentuuid = ""
      for comment in all_comments: 
        if comment.clean_id == str(incoming_id):
          parentuuid = comment.id
          break
      
      docjson = json.loads(request.FILES.get('document').read())
      title = docjson['title']
      content = docjson['content']

      file_name = util.write_file(request)

      try:
        reply = Reply.objects.create(title=title, content=content, owner_id=parentuuid, file_name=file_name)
        reply.clean_id = int(util.filterid(str(incoming_id)))
        reply.save()
        try: 
          return_replies = retrieve_comment_replies(incoming_id)
          return util.jsonresponse(return_replies)   
        except:
          return util.jsonresponse({"exception": "there was some exception"})   
      except:  
        return util.jsonresponse({"exception": "there was some exception"})
    else:
      return util.jsonresponse({'error': 'captcha invalid'})
def comments(request, board_mnemonic):
  util = utilities.Utilites()

  if request.method == 'GET':
    return_data = retrieve_comments_replies(3, board_mnemonic)
    return util.jsonresponse(return_data)
  
  return util.jsonresponse({"exception": "some error occurred"})

def boards(request):
  util = utilities.Utilites()
  if request.method == "GET":
    boards = Board.objects.all()
    boards_data = json.loads(serializers.serialize('json', boards))
    return util.jsonresponse(boards_data)

def comment(request, comment_id):
  util = utilities.Utilites()

  if request.method == 'PUT':
    new_votes = vote_handler(request, comment_id, "comment")
    logging.info('value of new_votes before return: %s', new_votes)
    return util.jsonresponse({'votes': new_votes})
  if request.method == 'GET':  
    return_data = retrieve_comment_replies(comment_id)
    return util.jsonresponse(return_data)

  elif request.method == 'POST':

    util = utilities.Utilites()
    logging.info("inside POST for comment before captcha bool")
    captcha_bool = check_captcha(request)
    if captcha_bool:
      logging.info("inside comment POST")

      files = request.FILES.get('document')
      docstring = request.FILES.get('document').read()
      docjson = json.loads(docstring)
      title = docjson['title']
      content = docjson['content']
      board_mnemonic = docjson['board_mnemonic']

      logging.info("before writefile handler")
      image_property = request.FILES.get('image')
      logging.info("value of image_property: %s", image_property)
      logging.info("value of image_property.name: %s", image_property.name)

      file_name = util.write_file(request)    
      board_val = Board.objects.all().filter(mnemonic=board_mnemonic)[0]
      comment = Comment.objects.create(title=title, content=content, file_name=file_name, owner=board_val)

      logging.info("value of comment %s; ", comment)

      comment.clean_id = int(util.filterid(str(comment.id)))
      comment.save()
      
      return_data = retrieve_comments_replies(3, board_mnemonic)

      return util.jsonresponse(return_data)
    else:
      return util.jsonresponse({'error': 'captcha invalid'})

  return JsonResponse({'comment_id': comment_id}, safe=False, json_dumps_params={'ensure_ascii': False})