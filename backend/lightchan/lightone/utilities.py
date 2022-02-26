import re
import datetime
from django.http.response import JsonResponse
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import ensure_csrf_cookie 

class Utilites():
  def getdatetime(self):  
    return int(datetime.datetime.now().timestamp()*1000000.0)
  def convertdbtime(self, dbtime):
    return int(dbtime.timestamp()*1000000.0)
  def convertid(self, ms):
    return datetime.datetime.fromtimestamp(ms/1000.0)
  # @method_decorator(ensure_csrf_cookie)
  def jsonresponse(self, obj):
    response = JsonResponse(obj, safe=False, json_dumps_params={'ensure_ascii': False})
    # response.set_cookie('some_cookie', 'cookie_val') 
    return response;
  def filterid(self, id):
    return re.sub('[abcdef()-]', '', str(id))
