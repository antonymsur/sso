from django.http import HttpResponse,HttpResponseRedirect 

def hello(request):
    loginurl = "http://login.example.com:8080/login?service="+request.build_absolute_uri()
    try:
        if (request.GET.get('ticket')):
            return HttpResponse("Hello "+request.GET.get('ticket')+" !")
    except (ValueError, AttributeError ):
            ticket = None
            return HttpResponseRedirect(loginurl)
    else:
        return HttpResponseRedirect(loginurl)
        