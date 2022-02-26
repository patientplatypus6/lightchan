
from lightone.models import *
from . import utilities
import datetime

def every_request(get_response):
  # One-time configuration and initialization.

  def middleware(request):
    # Code to be execute  d for each request before
    # the view (and later middleware) are called.
    
    print('inside the every_request middleware')
    util = utilities.Utilites()
    
    past15 = datetime.datetime.now() - datetime.timedelta(minutes=15)
    
    comments = Comment.objects.all()
    print('value of comments: %s', comments)
    print('value of 15 minutes: %s', 15*60*1000)
    for comment in comments:
      timestamp_now = datetime.datetime.now().timestamp()
      timestamp_db = datetime.datetime.timestamp(comment.created_at)
      dif = timestamp_now - timestamp_db
      print("timestamp_now %s", timestamp_now)
      print("timestamp_db %s", timestamp_db)
      print("dif %s", dif)
      print(dif>10000)
      if dif > 10000:
        comment.delete()
    
    response = get_response(request)

    # Code to be executed for each request/response after
    # the view is called.

    return response

  return middleware