from django.http import HttpResponse,HttpResponseRedirect 
import urllib

def helpservice(request):
    loginurl = "http://login.example.com:8080/login?service="+request.build_absolute_uri()
    try:
        if (request.GET.get('ticket')):
            #validate the ticket using cas url once validation successful then redirect to sp
            return HttpResponse("Hello "+request.GET.get('ticket')+" !")
    except (ValueError, AttributeError ):
            ticket = None
            return HttpResponseRedirect(loginurl)
    else:
        return HttpResponseRedirect(loginurl)
        