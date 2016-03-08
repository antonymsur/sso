from django.http import HttpResponse,HttpResponseRedirect 
import urllib

def helpservice(request):
    #loginurl = "http://login.example.com:8080/login?service="+request.build_absolute_uri()
    #authToken = 'ticket'
    oidpUrl = "http://localhost:8080/openid/authorize?response_type=code"; #code id_token token
    appId = 'client_id=091504' #Client Identifier
    redirectUrl = 'redirect_uri=http%3A%2F%2Fapp2.example.com%3A8082%2Fhelpservice' #+urllib.pathname2url(request.build_absolute_uri()) #where it needs to get redirected after succesful login/authN&Z
    scope = 'scope=openid%20profile' ##value must contain 'openid' and optiona(profile, email, address, phone) others
    stateOpaqueValue = 'af0ifjsldkj'
    state = 'state='+stateOpaqueValue #opaque value used to maintain state between request and call back
    nonceValue = 'n-0S6_WzA2Mkl'
    nonce = 'nonce='+nonceValue #associate Client session with an ID Token , this used to mitigate replay attack
    loginurl = oidpUrl + '&' + appId + '&' +redirectUrl + '&' + scope + '&' + state + '&' +nonce 
    authToken = 'code'
    try:
        if (request.GET.get(authToken)):
            return HttpResponse("Help "+request.GET.get(authToken)+" !")
    except (ValueError, AttributeError ):
            return HttpResponseRedirect(loginurl)
    else:
        return HttpResponseRedirect(loginurl)
        