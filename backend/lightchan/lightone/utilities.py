import re
import datetime
from django.http.response import JsonResponse
import os

class Utilites():
  def getdatetime(self):  
    return int(datetime.datetime.now().timestamp()*1000000.0)
  def convertdbtime(self, dbtime):
    return int(dbtime.timestamp()*1000000.0)
  def convertid(self, ms):
    return datetime.datetime.fromtimestamp(ms/1000.0)
  def jsonresponse(self, obj):
    response = JsonResponse(obj, safe=False, json_dumps_params={'ensure_ascii': False})
    return response;
  def filterid(self, id):
    return re.sub('[abcdef()-]', '', str(id))
  def write_file(self, request):
    image_property = request.FILES.get('image')
    _, file_extension = os.path.splitext(image_property.name)
    file_name = str(self.getdatetime())+file_extension
    file_path = "../static/" + file_name
    image_path = os.path.join(os.path.dirname(__file__), file_path)
    with open(image_path, "wb") as f:
      f.write(image_property.file.read())
    return file_name