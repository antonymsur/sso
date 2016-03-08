from django.http import HttpResponse,HttpResponseRedirect 
import urllib
import json
import requests
from django.conf import settings

def hello2(request):
    if settings.AUTH_PROTO == 'OIDC':
	authType = settings.AUTH_TYPE
	oidpUrl = settings.LOGIN_URL 
	appId = 'client_id='+ settings.APP_ID 
	redirectUrl = 'redirect_uri='+ settings.APP_URL 
	scope = 'scope=' + settings.AUTH_SCOPE
	stateOpaqueValue = 'af0ifjsldkj'  #currenly hardcoded. This needs to be generated 
	state = 'state='+stateOpaqueValue #opaque value used to maintain state between request and call back
	nonceValue = 'n-0S6_WzA2Mj'       #currenly hardcoded. This needs to be generated 
	nonce = 'nonce='+nonceValue       #associate Client session with an ID Token , this used to mitigate replay attack
	loginurl = oidpUrl + '&' + appId + '&' +redirectUrl + '&' + scope + '&' + state + '&' +nonce 
    else:
	loginurl = settings.LOGIN_URL
    try:
	code = request.GET.get(authType)
	state = request.GET.get('state')
        if (code and state == stateOpaqueValue):
	    value = post_message(code)
	    return HttpResponse("Hello Again ! <br> "+ value )
    except (ValueError, AttributeError ):
            return HttpResponseRedirect(loginurl)
    else:
        return HttpResponseRedirect(loginurl)
       
def post_message(code):
    params = 'grant_type=authorization_code&code='+code+'&client_id='+settings.APP_ID+'&redirect_uri='+settings.APP_URL+'&client_secret='+settings.APP_SECRET
    response = requests.post(settings.OID_TOKEN_URL,params,headers={'Content-Type': 'application/x-www-form-urlencoded'})
    return response.text


