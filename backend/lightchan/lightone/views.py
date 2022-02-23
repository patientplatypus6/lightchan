from cmath import exp
import doctest
from unittest import expectedFailure
from django.http import HttpResponse
from django.http.response import JsonResponse
import multipart

import json
from requests_toolbelt.multipart import decoder
from lightone.models import *
from . import utilities

def index(request):
  return HttpResponse("Hello light one.")

def simple_app(request):
    ret = []

    # The following two callbacks just append the name to the return value.
    def on_field(field):
        ret.append("Parsed field named: %s" % (field.field_name,))

    def on_file(file):
        ret.append("Parsed file named: %s" % (file.field_name,))

    # Create headers object.  We need to convert from WSGI to the actual
    # name of the header, since this library does not assume that you are
    # using WSGI.
    headers = {'Content-Type': request['CONTENT_TYPE']}
    if 'HTTP_X_FILE_NAME' in request:
        headers['X-File-Name'] = request['HTTP_X_FILE_NAME']
    if 'CONTENT_LENGTH' in request:
        headers['Content-Length'] = request['CONTENT_LENGTH']

    # Parse the form.
    multipart.parse_form(headers, request['wsgi.input'], on_field, on_file)

    return ret

def reply(request, reply_id):
  print("inside reply")
  print("value of request %s", 
  request)
  util = utilities.Utilites()
  if request.method=="POST":
    all_comments = Comment.objects.all()
    jsonbody = json.loads(request.body)
    parentuuid = ""
    for comment in all_comments: 
       if str(util.filterid(comment.id)) == str(reply_id):
        parentuuid = comment.id

    print('value of parentuuid: %s', parentuuid)

    try:
      comment = Reply.objects.create(title=jsonbody['title'], content=jsonbody['content'], owner_id=parentuuid)
      try: 
        returnreplies = []
        replies = Reply.objects.all().filter(owner_id=parentuuid).order_by("-created_at")
        for reply in replies: 
          returnreplies.append({
            'id': reply.id, 
            'title': reply.title,
            'content': reply.content,
            'created_at': reply.created_at
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
        returnreplies.append({
          'id': reply.id, 
          'title': reply.title,
          'content': reply.content,
          'created_at': reply.created_at
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

    print("inside GET for comment")

    all_comments = Comment.objects.all()
    for comment in all_comments: 
       if str(util.filterid(comment.id)) == str(comment_id):
         return util.jsonresponse({
           "id": comment_id,
           "title": comment.title,
           "content": comment.content, 
           "created_at": comment.created_at
         })
    return util.jsonresponse({"exception": "comment not found"})

  elif request.method == 'POST':

    print("inside POST")
    # print("value of request.body %s", json.loads(request.body))
    print("value of request.body %s", request.body)
    
    # ret = simple_app(request)
    # print('value of ret %s, ', ret)
    
    # print("value of request.body %s", request.body.form['title'])
    # print("***********************************************************")
    # print('value of params: %s', request.POST.get("title"))
    # print("***********************************************************")
    
    # print("value of request: ", request.POST.get)
    
    # jsonbody = json.loads(request.body)

    # testEnrollResponse = requests.post(...)
    # multipart_data = decoder.MultipartDecoder.from_response(request.body)

    # for part in multipart_data.parts:
    #     print(part.content)  # Alternatively, part.text if you want unicode
    #     print(part.headers)
    
    # print("value of request.POST(...): ", request.POST(...))
    
    # testEnrollResponse = request.POST(...)
    # multipart_data = decoder.MultipartDecoder.from_response(testEnrollResponse)

    # for part in multipart_data.parts:
    #     print(part.content)  # Alternatively, part.text if you want unicode
    #     print(part.headers)

    print("value of request.FILES ", request.FILES)
    print("value of request.FILES['image'] ", request.FILES['image'])
    # print("value of request.FILES['document'] ", json.dumps(request.FILES['document']))

    docstring = request.FILES.get('document').read()
    
    print('docstring %s,', docstring);
    
    docjson = json.loads(docstring)
    
    print("docjson %s, ", docjson['title']);
    
    # print("value of request.FILES['document'] ", type(request.FILES['document']))    
    # print("value of request.POST.get('document') ", request.POST.get("document"))
    # print("value of request.POST.get('document') ", request.POST.get("document"))

    try:
      comment = Comment.objects.create(title=jsonbody['title'], content=jsonbody['content'])
      return util.jsonresponse({
          "formid": util.filterid(comment.id)
        })
    except:  
      return util.jsonresponse({"exception": "there was some exception"})

  return JsonResponse({'comment_id': comment_id}, safe=False, json_dumps_params={'ensure_ascii': False})