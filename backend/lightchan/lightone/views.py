from django.http import HttpResponse
from django.http.response import JsonResponse
from jinja2 import Undefined
import multipart
import json    
import os
from requests_toolbelt.multipart import decoder
from lightone.models import *
from django.db import transaction
from . import utilities

from django.core import serializers


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
       if comment.clean_id == str(reply_id):
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
      reply.clean_id = int(util.filterid(str(reply_id)))
      reply.save()
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
            'clean_id': reply.clean_id,
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

def replies(request, comment_id):
  util = utilities.Utilites()
  if request.method=="GET":
    try: 
      returnreplies = []
      parent_comment = Comment.objects.get(clean_id=comment_id)
      replies = Reply.objects.all().filter(owner_id=parent_comment.id).order_by("-created_at")

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
  
  if request.method == 'PUT':
    print('inside the PUT method for get')

  if request.method == 'GET':
    
    print("inside comment request.method is GET")

    parent_comment = Comment.objects.all().filter(clean_id=comment_id)
    replies = Reply.objects.all().filter(owner_id=parent_comment[0].id)
    parent_comment_data = json.loads(serializers.serialize('json', parent_comment))
    replies_data = json.loads(serializers.serialize("json", replies))

    parent_comment_data[0]['pk'] = 'PRIVATE'
    for reply, key in replies_data:
      replies_data[key]['pk'] = 'PRIVATE'
    
    return_data = {
      "comment": parent_comment_data[0], 
      "replies": replies_data
    }
    
    print("value of return_data before response: %s", return_data)
    
    return util.jsonresponse(return_data)

  elif request.method == 'POST':

    util = utilities.Utilites()

    docstring = request.FILES.get('document').read()
    docjson = json.loads(docstring)
    title = docjson['title']
    content = docjson['content']
    _, file_extension = os.path.splitext(request.FILES.get('image').name)
    
    if file_extension=='.jpg' or file_extension=='.jpeg' or file_extension=='.gif' or file_extension=='.svg' or file_extension=='.png':
    
      file_name = str(util.getdatetime())+file_extension
      file_path = "../static/"+file_name
      image_path = os.path.join(os.path.dirname(__file__), file_path)
    
      with open(image_path, "wb") as f:
          f.write(request.FILES.get('image').file.read())

      try:
        comment = Comment.objects.create(title=title, content=content, file_name=file_name)
        comment.clean_id = int(util.filterid(str(comment.id)))
        comment.save()
        return util.jsonresponse({
            "formid": util.filterid(comment.id)
          })
      except:  
        return util.jsonresponse({"exception": "there was some exception"})
    else: 
      return util.jsonresponse({"exception": "file format not valid"})

  return JsonResponse({'comment_id': comment_id}, safe=False, json_dumps_params={'ensure_ascii': False})