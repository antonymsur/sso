# sso
Sample SSO implementation.
This has 2 different applications 
	1. Using OpenID Connect sample provider 
	2. CAS protocol using python - needs more verification


This sample/poc is done using django-oidc-provider

Install the django-oidc-provider using pip

$pip install django-oidc-provider

Run the provider from oidc_idp/idp 

DATABASE.sqlite3 is the database file for the testing , this will be changed with the 
DB settings in settings.py using postgresql

$ python manage.py migrate
$ python manage.py creatersakey
#RUN login IDP server at login.example.com 
$ python manage.py runserver 8080 

http://login.example.com:8080/admin has admin portal this is  django administration console for IDP with django's auth framework

We can find links for client addition and RSA keys
Clients # here we should add single or group of apps(urls) which can be identified by single client_id once you add client_secret will be generated.	
RSA Keys # creatersakey generated key can be found here , we can add or modify the RSA key used for secure data transmission. This is assymetric(public/private key)	 	
The generated code/token can be monitored using below links:

Authorization Codes - AuthN&Z code  
Tokens 	 - ID Token


Run the sample helloservice from app1.example.com
$python manage.py runserver 80


Run the sample helloservice2 from app3.example.com:8081
$python manage.py runserver 8081



Run the sample helpservice from app2.example.com:8082
$python manage.py runserver 8082


