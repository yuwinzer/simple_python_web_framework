# my simple python framework is in development


## Starting with gunicorn
run command 
'''gunicorn app:app --bind 127.0.0.1:8010''' 

That helps to start localhost with port 8010, 
you can change it as you wish:
> --bind 127.0.0.1:8010


## Alternatives without gunicorn
run command 
'''python WSGI.py''' 
in framework dir and open 
'''http://localhost:8005/'''

for reversed response:
run command 
'''python WSGI_reverse.py''' 
in framework dir and open 
'''http://localhost:8006/'''