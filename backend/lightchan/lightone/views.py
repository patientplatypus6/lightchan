from cmath import exp
import doctest
from fileinput import filename
from unittest import expectedFailure
from django.http import HttpResponse
from django.http.response import JsonResponse
from jinja2 import Undefined
import multipart
import json    
import os
from requests_toolbelt.multipart import decoder
from lightone.models import *
from . import utilities

def index(request):
  return HttpResponse("Hello light one.")

def reply(request, reply_id):
  print("inside reply")
  print("value of request %s", 
  request)
  util = utilities.Utilites()
  if request.method=="POST":
    all_comments = Comment.objects.all()
    # jsonbody = json.loads(request.body)
    parentuuid = ""
    for comment in all_comments: 
       if str(util.filterid(comment.id)) == str(reply_id):
        parentuuid = comment.id

    print('value of parentuuid: %s', parentuuid)
    
    docstring = request.FILES.get('document').read()
    docjson = json.loads(docstring)
    title = docjson['title']
    content = docjson['content']
    _, file_extension = os.path.splitext(request.FILES.get('image').name)
    file_name = str(util.getdatetime())+file_extension
    file_path = "../static/"+file_name
    image_path = os.path.join(os.path.dirname(__file__), file_path)
    
    with open(image_path, "wb") as f:
        f.write(request.FILES.get('image').file.read())

    try:
      reply = Reply.objects.create(title=title, content=content, owner_id=parentuuid, file_name=file_name)
      try: 
        returnreplies = []
        replies = Reply.objects.all().filter(owner_id=parentuuid).order_by("-created_at")
        for reply in replies: 
          file_name = ""
          if len(reply.file_name)>0:
            file_name = reply.file_name
          returnreplies.append({
            'id': reply.id, 
            'title': reply.title,
            'content': reply.content,
            'created_at': reply.created_at, 
            'file_name': file_name
          })
        return util.jsonresponse(returnreplies)   
      except:
        return util.jsonresponse({"exception": "there was some exception"})   
    except:  
      return util.jsonresponse({"exception": "there was some exception"})
  if request.method=="GET":
    try: 
      reply = Reply.objects.all().filter(id=reply_id)
      return util.jsonresponse(reply)
    except:
      return util.jsonresponse({"exception": "there was some exception"}) 

def replies(request, reply_id):
  print("inside replies")
  print("value of request %s", 
  request)
  util = utilities.Utilites()
  if request.method=="GET":
    try: 
      returnreplies = []
      parentuuid = ""
      all_comments = Comment.objects.all()
      for comment in all_comments: 
        if str(util.filterid(comment.id)) == str(reply_id):
          parentuuid = comment.id
      replies = Reply.objects.all().filter(owner_id=parentuuid).order_by("-created_at")
      for reply in replies: 
        file_name = ""
        if len(reply.file_name)>0:
          file_name = reply.file_name
        returnreplies.append({
          'id': reply.id, 
          'title': reply.title,
          'content': reply.content,
          'created_at': reply.created_at,
          'file_name': file_name
        })
      return util.jsonresponse(returnreplies)   
    except:
      return util.jsonresponse({"exception": "there was some exception1"})
  return util.jsonresponse({"exception": "there was some exception2"})

def comments(request):
  print("inside comments")
  print("value of request %s", 
  request)
  util = utilities.Utilites()

  returncomments = []

  if request.method == 'GET':
    print('inside GET')
    all_comments = Comment.objects.all()
    ordered_comments = all_comments.order_by("-created_at")
    for comment in ordered_comments:
      file_name = ""
      if len(comment.file_name)>0:
        file_name = comment.file_name
      returncomments.append({
        "id": util.filterid(comment.id),
        "title": comment.title,
        "content": comment.content,
        "created_at": comment.created_at,
        "file_name": file_name
      })
    return util.jsonresponse(returncomments)  
  
  return util.jsonresponse({"exception": "some error occurred"})


def comment(request, comment_id):
  print("inside read_comment param")
  print("value of request %s", 
  request)
  util = utilities.Utilites()

  if request.method == 'GET':

    print("inside GET for comment")

    all_comments = Comment.objects.all()
    for comment in all_comments: 
       if str(util.filterid(comment.id)) == str(comment_id):
         file_name = ""
         if len(comment.file_name)>0:
           file_name = comment.file_name
         return util.jsonresponse({
           "id": comment_id,
           "title": comment.title,
           "content": comment.content, 
           "created_at": comment.created_at, 
           "file_name": file_name
         })
    return util.jsonresponse({"exception": "comment not found"})

  elif request.method == 'POST':

    util = utilities.Utilites()

    docstring = request.FILES.get('document').read()
    docjson = json.loads(docstring)
    title = docjson['title']
    content = docjson['content']
    _, file_extension = os.path.splitext(request.FILES.get('image').name)
    file_name = str(util.getdatetime())+file_extension
    file_path = "../static/"+file_name
    image_path = os.path.join(os.path.dirname(__file__), file_path)
    
    with open(image_path, "wb") as f:
        f.write(request.FILES.get('image').file.read())

    try:
      comment = Comment.objects.create(title=title, content=content, file_name=file_name)
      print("value of comment: %s", str(comment))
      return util.jsonresponse({
          "formid": util.filterid(comment.id)
        })
    except:  
      return util.jsonresponse({"exception": "there was some exception"})

  return JsonResponse({'comment_id': comment_id}, safe=False, json_dumps_params={'ensure_ascii': False})