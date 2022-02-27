
from logging import handlers
from lightone.models import *
from . import utilities
import datetime
from django.contrib.sessions.backends.db import SessionStore
import random

# def handle_votes(request):
#   request.COOKIE['test'] = 'some test'
#   return request
  
def handle_clean():
  comments = Comment.objects.all()
  for comment in comments:
    timestamp_now = datetime.datetime.now().timestamp()
    timestamp_db = datetime.datetime.timestamp(comment.created_at)
    dif = timestamp_now - timestamp_db
    # print("timestamp_now %s", timestamp_now)
    # print("timestamp_db %s", timestamp_db)
    # print("dif %s", dif)
    print(dif>10000)
    if dif > 10000:
      comment.delete()  



# def handle_session(request):
  # print('value of request.session %s', request.session)
  # try:
  #   user_id = request.session['start']
  #   print(user_id)
  # except KeyError:
  #   print("user has not started a session, now initializing: ")
  #   request.session['start'] = datetime.datetime.now().timestamp()
    
  # print('request.keys: %s', request.session.keys())

  # if request.method == 'POST' or request.method == 'PUT':
  # if request.session.test_cookie_worked():
  # # request.session.delete_test_cookie()
  # # return HttpResponse("You're logged in.")
  #   print('cookie worked')
  # else:
  #   print('cookie did not work')
  #   request.session.set_test_cookie()


def every_request(get_response):
  # One-time configuration and initialization.

  def middleware(request):
    # Code to be executed for each request before
    # the view (and later middleware) are called.
    
    print("MIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWARE")
    print("MIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWARE")
    print("MIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWARE")
    print('inside the every_request middleware')
    handle_clean()
    # request = handle_votes(request)
    # handle_session(request)
    print("MIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWARE")
    print("MIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWARE")
    print("MIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWAREMIDDLEWARE")
    response = get_response(request)

    # Code to be executed for each request/response after
    # the view is called.

    return response

  return middleware