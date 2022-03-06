from email.mime import image
from fileinput import filename
from importlib.metadata import files
from django.http import HttpResponse
from django.http.response import JsonResponse
import json    
import os
from lightone.models import *
from . import utilities

from django.core import serializers
from django.core.files.storage import FileSystemStorage

import logging

def retrieve_comments_replies(index):
  comments = Comment.objects.all().order_by('-created_at')
  logging.info("value of comments %s, ", comments)
  comment_data = json.loads(serializers.serialize('json', comments))
  logging.info("value of comment_data: %s ", comment_data)
 
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

def write_file(request):
  util = utilities.Utilites()
  image_property = request.FILES.get('image')
  _, file_extension = os.path.splitext(image_property.name)
  file_name = str(util.getdatetime())+file_extension
  file_path = "../static/" + file_name
  image_path = os.path.join(os.path.dirname(__file__), file_path)
  logging.info("value of image_path: %s", image_path)
  logging.info("value of file_name: %s", file_name)
  with open(image_path, "wb") as f:
    f.write(image_property.file.read())
  return file_name

# def write_file(request):
#   logging.info("inside the write_file_test def")
#   fs = FileSystemStorage()
#   image_file = request.FILES.get('image')
#   logging.info("inside the write_file_test def %s", image_file.name)
#   image_bytes = image_file.file.read()
#   # logging.info("value of image_bytes: %s", image_bytes)
#   # fs.location()
#   image_saved = fs.save(image_file.name, image_file)
#   logging.info("value of image_saved: %s", image_saved)
#   return image_file.name
  

def index(request):
  return HttpResponse("Hello light one.")

def reply(request, incoming_id):
  util = utilities.Utilites()
  if request.method=="POST":
    
    all_comments = Comment.objects.all()
    parentuuid = ""
    for comment in all_comments: 
      parentuuid = comment.id if comment.clean_id == str(incoming_id) else ""

    logging.info('value of parentuuid: %s', parentuuid)
    
    docjson = json.loads(request.FILES.get('document').read())
    title = docjson['title']
    content = docjson['content']

    file_name = write_file(request)

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
    
def comments(request):
  logging.info("inside comments")
  logging.info("value of request %s", request)
  util = utilities.Utilites()

  if request.method == 'GET':
    logging.info('inside GET')
    return_data = retrieve_comments_replies(3)
    return util.jsonresponse(return_data)
  
  return util.jsonresponse({"exception": "some error occurred"})


def comment(request, comment_id):

  logging.info("inside read_comment param")
  logging.info("value of request %s", 
  request)
  util = utilities.Utilites()

  if request.method == 'PUT':

    body = json.loads(request.body)
    
    upvote = body['upvote']
    downvote = body['downvote']
    votedelta = upvote*1+downvote*-1
    votename = "upvote" if upvote else "downvote"
    
    votedelta_sess = str(comment_id)+"vote"
    votename_sess = str(comment_id)+"votename"
    
    def set_votes(votedelta, votename):
      request.session[votedelta_sess] = votedelta
      request.session[votename_sess] = votename
      request.session[str(comment_id)+"/vote/"+votename] = votedelta
      comment = Comment.objects.all().filter(clean_id=comment_id)[0]
      comment.votes = comment.votes + votedelta
      comment.save()
      return comment
    
    try: 
      prev_name = request.session[votename_sess]
      
      logging.info("value of prev_name: %s", prev_name)
      logging.info("value of upvote: %s", upvote)
      logging.info("value of downvote: %s", downvote)
      
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
      
      comment = set_votes(votedelta, votename)
      
      return util.jsonresponse({'votes': comment.votes})
    except: 
      logging.info('User has not voted yet - ')
      comment = set_votes(votedelta, votename)
      return util.jsonresponse({'votes': comment.votes})

  if request.method == 'GET':  
    return_data = retrieve_comment_replies(comment_id)
    return util.jsonresponse(return_data)

  elif request.method == 'POST':

    logging.info('inside POST for comment')

    util = utilities.Utilites()

    files = request.FILES.get('document')
    logging.info("value of files %s, ", files)
    docstring = request.FILES.get('document').read()
    docjson = json.loads(docstring)
    title = docjson['title']
    content = docjson['content']

    logging.info("~~~NOW WRITING IMAGE TO FILE~~~")
    x = 3
    logging.info("~~~NOW WRITING IMAGE TO FILE~~~")
    logging.info("testy test; %s", x)
    file_name = write_file(request)

    comment = Comment.objects.create(title=title, content=content, file_name=file_name)
    comment.clean_id = int(util.filterid(str(comment.id)))
    comment.save()
    
    return_data = retrieve_comments_replies(3)

    return util.jsonresponse(return_data)

  return JsonResponse({'comment_id': comment_id}, safe=False, json_dumps_params={'ensure_ascii': False})