from cgi import test
from distutils.command.clean import clean
from django.http import HttpResponse
from django.http.response import JsonResponse
import json    
import os
from lightone.models import *
from . import utilities

from django.core import serializers
from django.middleware.csrf import get_token


def cookie_tester(request): 
  print('inside cookie_tester')
  # request.session['some_cookie'] = 'test'
  # print("request.session.keys() %s", request.session.keys())
  print('request.session.session_key %s', request.session.session_key)
  some_cookie = request.session['some_cookie']
  print('value of some_cookie: %s', some_cookie)

def retrieve_comments_replies(index):
  comments = Comment.objects.all().order_by('-created_at')
  print("value of comments %s, ", comments)
  comment_data = json.loads(serializers.serialize('json', comments))
  print("value of comment_data: %s ", comment_data)
 
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
  return return_data;

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
  
  return return_data;

def write_file(image_property):
  util = utilities.Utilites()
  _, file_extension = os.path.splitext(image_property.name)
  file_name = str(util.getdatetime())+file_extension
  file_path = "../static/"+file_name
  image_path = os.path.join(os.path.dirname(__file__), file_path)
  
  with open(image_path, "wb") as f:
      f.write(image_property.file.read())
  return file_name

def index(request):
  cookie_tester(request)
  return HttpResponse("Hello light one.")

def reply(request, incoming_id):
  util = utilities.Utilites()
  cookie_tester(request)
  if request.method=="POST":
    
    all_comments = Comment.objects.all()
    parentuuid = ""
    for comment in all_comments: 
      parentuuid = comment.id if comment.clean_id == str(incoming_id) else ""

    print('value of parentuuid: %s', parentuuid)
    
    docjson = json.loads(request.FILES.get('document').read())
    title = docjson['title']
    content = docjson['content']
    
    file_name = write_file(request.FILES.get('image'))

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
  cookie_tester(request)
  print("inside comments")
  print("value of request %s", request)
  util = utilities.Utilites()

  if request.method == 'GET':
    print('inside GET')
    return_data = retrieve_comments_replies(3)
    return util.jsonresponse(return_data)
  
  return util.jsonresponse({"exception": "some error occurred"})


def comment(request, comment_id):
  cookie_tester(request)
  print("inside read_comment param")
  print("value of request %s", 
  request)
  util = utilities.Utilites()
  
  if request.method == 'PUT':
    body = json.loads(request.body)
    upvote = body['upvote']
    downvote = body['downvote']
    votedelta = upvote*1+downvote*-1
    
    # if request.session.test_cookie_worked():
    #     # request.session.delete_test_cookie()
    #   # return HttpResponse("You're logged in.")
    #   print('cookie worked')
    # else:
    #   print('cookie did not work')
    #   request.session.set_test_cookie()
    
    # print("request.session.keys() %s", request.session.keys())
    
    # try:
    #   vote_tally = request.session['vote_tally']
    #   print(vote_tally)
    # except KeyError:
    #   print("user has not started a session, now initializing: ")
    #   request.session['vote_tally'] = 'test'
      
    # request.session['vote_tally'] = 'test'
    # vote_tally = request.session['vote_tally']
    # print(vote_tally)
    
    comment = Comment.objects.all().filter(clean_id=comment_id)[0]
    comment.votes = comment.votes + votedelta
    comment.save()
    return util.jsonresponse({'votes': comment.votes})

  if request.method == 'GET':  
    return_data = retrieve_comment_replies(comment_id)
    return util.jsonresponse(return_data)

  elif request.method == 'POST':

    print('inside POST for comment')

    util = utilities.Utilites()

    files = request.FILES.get('document')
    print("value of files %s, ", files)
    docstring = request.FILES.get('document').read()
    docjson = json.loads(docstring)
    title = docjson['title']
    content = docjson['content']

    file_name = write_file(request.FILES.get('image'))

    comment = Comment.objects.create(title=title, content=content, file_name=file_name)
    comment.clean_id = int(util.filterid(str(comment.id)))
    comment.save()
    
    return_data = retrieve_comments_replies(3)

    return util.jsonresponse(return_data)

  return JsonResponse({'comment_id': comment_id}, safe=False, json_dumps_params={'ensure_ascii': False})