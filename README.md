# my simple python framework is in development


## Starting simple framework
run command 
```gunicorn app:app --bind 127.0.0.1:8010``` 
"--bind" helps to start localhost with port 8010, 
you can change port, if it already is used

Here are the links, that are implemented:
[http://127.0.0.1:8010/home]_
[http://127.0.0.1:8010/about]_
[http://127.0.0.1:8010/hello/yourname]_
[http://127.0.0.1:8010/tell/100]_

## Just testing WSGI files
run command 
```python WSGI.py``` 
in framework dir and open 
```http://localhost:8005/```

for reversed response:
run command 
```python WSGI_reverse.py``` 
in framework dir and open 
```http://localhost:8006/```