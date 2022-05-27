# my simple python framework is in development


## Starting simple framework
run command 
```gunicorn app:app --bind 127.0.0.1:8010``` 
"--bind" helps to start localhost with port 8010, 
you can change port, if it already is used

Here are the links, that are implemented:<br/>
[http://127.0.0.1:8010/home]()<br/>
[http://127.0.0.1:8010/about]()<br/>
[http://127.0.0.1:8010/hello/yourname]()<br/>
[http://127.0.0.1:8010/tell/100]()

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