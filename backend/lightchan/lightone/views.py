from email.mime import image
from fileinput import filename
from importlib.metadata import files
from django.http import HttpResponse
from django.http.response import JsonResponse
import json    
from lightone.models import *
from . import utilities

from django.core import serializers
from django.core.files.storage import FileSystemStorage

import logging

def vote_handler(request, id, type_val):
  util = utilities.Utilites()
  body = json.loads(request.body)

  upvote = body['upvote']
  downvote = body['downvote']
  votedelta = upvote*1+downvote*-1
  votename = "upvote" if upvote else "downvote"
  votedelta_sess = str(id)+"vote"
  votename_sess = str(id)+"votename"

  def set_votes(votedelta, votename):
    request.session[votedelta_sess] = votedelta
    request.session[votename_sess] = votename
    request.session[str(id)+"/vote/"+votename] = votedelta
    if type_val == 'comment':
      comment = Comment.objects.all().filter(clean_id=id)[0]
      comment.votes = comment.votes + votedelta
      comment.save()
      return comment
    elif type_val == 'reply':
      reply = Reply.objects.all().filter(clean_id=id)[0]
      reply.votes = reply.votes + votedelta
      reply.save()
      return reply

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
    
    return_comment_reply = set_votes(votedelta, votename)
    return util.jsonresponse({'votes': return_comment_reply.votes})
  except: 
    return_comment_reply = set_votes(votedelta, votename)
    return util.jsonresponse({'votes': return_comment_reply.votes})

def retrieve_comments_replies(index, board_mnemonic):
  # parent_board = Board.objects.all().filter(mnemonic=board_mnemonic)
  comments = Comment.objects.all().filter(owner_id=board_mnemonic).order_by('-created_at')
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
    vote_handler(request, incoming_id, "reply")

  if request.method=="POST":
    
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
    
def comments(request, board_mnemonic):
  util = utilities.Utilites()

  if request.method == 'GET':
    return_data = retrieve_comments_replies(3, board_mnemonic)
    return util.jsonresponse(return_data)
  
  return util.jsonresponse({"exception": "some error occurred"})


def comment(request, comment_id):
  util = utilities.Utilites()

  if request.method == 'PUT':
    vote_handler(request, comment_id, "comment")

  if request.method == 'GET':  
    return_data = retrieve_comment_replies(comment_id)
    return util.jsonresponse(return_data)

  elif request.method == 'POST':

    util = utilities.Utilites()

    files = request.FILES.get('document')
    docstring = request.FILES.get('document').read()
    docjson = json.loads(docstring)
    title = docjson['title']
    content = docjson['content']
    board_mnemonic = docjson['board_mnemonic']

    file_name = util.write_file(request)

    # parent_board = Reply.objects.all().filter(mnemonic=board_mnemonic)

    comment = Comment.objects.create(title=title, content=content, file_name=file_name, owner_id=board_mnemonic)
    comment.clean_id = int(util.filterid(str(comment.id)))
    comment.save()
    
    return_data = retrieve_comments_replies(3)

    return util.jsonresponse(return_data)

  return JsonResponse({'comment_id': comment_id}, safe=False, json_dumps_params={'ensure_ascii': False})