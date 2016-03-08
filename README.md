# sso
Sample SSO implementation.

This has 2 different applications

1. Using OpenID Connect sample provider 
2. CAS(mama-cas) protocol using python - TODO verify more


This sample/poc is done using django-oidc-provider

Install the django-oidc-provider using pip

$pip install django-oidc-provider

Run the provider from oidc_idp/idp 

DATABASE.sqlite3 is the database file for the testing , this will be changed with the 
DB settings in settings.py using postgresql

$ python manage.py migrate
$ python manage.py creatersakey
## RUN login IDP server at login.example.com 
$ python manage.py runserver 8080 

http://login.example.com:8080/admin has admin portal this is  django administration console for IDP with django's auth framework
Find links for client addition and RSA keys in the admin page:

Clients # here we should add single or group of apps(urls) which can be identified by single client_id once you add client_secret will be generated.	
RSA Keys # creatersakey generated key can be found here , we can add or modify the RSA key used for secure data transmission. This is assymetric(public/private key)	 	
The generated code/token can be monitored using below links:

Authorization Codes - AuthN&Z code  
Tokens 	 - ID Token

## APP servers at apps.example.com 
Run the sample helloservice from app1.example.com
$python manage.py runserver 80


Run the sample helloservice2 from app3.example.com:8081
$python manage.py runserver 8081



Run the sample helpservice from app2.example.com:8082
$python manage.py runserver 8082

## Constants used for APPS in settings
APP_ID = '454662'  #Client Identifier

APP_SECRET = 'efdde43d201207c66a76251da9a5e48b'

LOGIN_URL = 'http://login.example.com:8080/openid/authorize?response_type=code'

APP_URL = 'http%3A%2F%2Fapp3.example.com%3A8081%2Fhello2' #where it needs to get redirected after succesful login/authN&Z

OID_TOKEN_URL = 'http://login.example.com:8080/openid/token'

AUTH_TYPE = 'code' #code id_token token , currently supports only code

AUTH_SCOPE = 'openid%20profile%20email' ##value must contain 'openid' and optional(profile, email, address, phone) others

AUTH_PROTO = 'OIDC' #OR 'CAS' with LOGIN_URL  = "http://login.example.com:8080/login?service="+request.build_absolute_uri()


