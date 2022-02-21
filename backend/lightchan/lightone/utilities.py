import datetime
from django.http.response import JsonResponse



class Utilites():
  def getdatetime(self):  
    return int(datetime.datetime.now().timestamp()*1000000.0)
  def convertdbtime(self, dbtime):
    return int(dbtime.timestamp()*1000000.0)
  def convertid(self, ms):
    return datetime.datetime.fromtimestamp(ms/1000.0)
  def jsonresponse(self, obj):
    return JsonResponse(obj, safe=False, json_dumps_params={'ensure_ascii': False})
