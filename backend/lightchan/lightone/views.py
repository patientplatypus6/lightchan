from ctypes import util
from distutils.cmd import Command
from email import utils
from pyexpat import model
from xml.etree.ElementTree import Comment
from django.shortcuts import render

from django.http import HttpResponse
from django.http.response import JsonResponse

import json
from lightone.models import Comment
from . import utilities


def index(request):
  return HttpResponse("Hello light one.")

def reply(request, reply_id):
  print("inside reply")
  print("value of request %s", 
  request)
  util = utilities.Utilites()

def replies(request):
  print("inside replies")
  print("value of request %s", 
  request)
  util = utilities.Utilites()

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
      returncomments.append({
        "id": util.filterid(comment.id),
        "title": comment.title,
        "content": comment.content,
        "created_at": comment.created_at
      })
    return util.jsonresponse(returncomments)  
  
  return util.jsonresponse({"exception": "some error occurred"})


def comment(request, comment_id):
  print("inside read_comment param")
  print("value of request %s", 
  request)
  util = utilities.Utilites()

  if request.method == 'GET':

    print("inside GET")

    all_comments = Comment.objects.all()
    for comment in all_comments: 
       if str(util.filterid(comment_id)) == str(comment_id):
         return util.jsonresponse({
           "id": comment_id,
           "title": comment.title,
           "content": comment.content, 
           "created": comment.created_at
         })
    return util.jsonresponse({"exception": "comment not found"})

  elif request.method == 'POST':

    print("inside POST")
    print("value of request.body %s", json.loads(request.body))

    jsonbody = json.loads(request.body)

    try:
      comment = Comment.objects.create(title=jsonbody['title'], content=jsonbody['content'])
      return util.jsonresponse({
          "formid": util.filterid(comment.id)
        })
    except:  
      return util.jsonresponse({"exception": "there was some exception"})

  return JsonResponse({'comment_id': comment_id}, safe=False, json_dumps_params={'ensure_ascii': False})