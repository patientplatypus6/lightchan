from ctypes import util
from distutils.cmd import Command
from pyexpat import model
from xml.etree.ElementTree import Comment
from django.shortcuts import render

from django.http import HttpResponse
from django.http.response import JsonResponse

import json
from lightone.models import Comment
from . import utilities
import re

def index(request):
  return HttpResponse("Hello light one.")

def comment(request, comment_id):
  print("inside read_comment param")
  print("value of request %s", 
  request)
  util = utilities.Utilites()

  if request.method == 'GET':

    print("inside GET")

    all_comments = Comment.objects.all()
    for comment in all_comments: 
       filteredid = re.sub('[abcdef-]', '', str(comment.id))
       print("value of filteredid: %s", filteredid)
       print("value of commentid: %s", comment_id)
       print("value of equality: ", filteredid == comment_id)
       if str(filteredid) == str(comment_id):

         return util.jsonresponse({
           "id": comment_id,
           "title": comment.title,
           "content": comment.content
         })
    return util.jsonresponse({"exception": "comment not found"})

  elif request.method == 'POST':

    print("inside POST")
    print("value of request.body %s", json.loads(request.body))

    jsonbody = json.loads(request.body)

    try:
      comment = Comment.objects.create(title=jsonbody['title'], content=jsonbody['content'])
      formid =  re.sub('[abcdef-]', '', str(comment.id))
      return util.jsonresponse({
          "formid": formid
        })
    except:  
      return util.jsonresponse({"exception": "there was some exception"})

  return JsonResponse({'comment_id': comment_id}, safe=False, json_dumps_params={'ensure_ascii': False})