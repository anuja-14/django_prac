from django.http import HttpResponse,Http404
import datetime

def hello(request):
    return HttpResponse("Hell World")

def current_datetime(request):
    now=datetime.datetime.now()
    html="<html><body>It is now %s. </body></html>" %now
    return HttpResponse(html)

def offset_time(request,offset):
    try:
        diff=int(offset)
    except:
        raise Http404()
    dt=datetime.datetime.now()+datetime.timedelta(hours=diff)
    html="<html>It will be %s after %s</html>" %(dt,diff)
    return HttpResponse(html)

