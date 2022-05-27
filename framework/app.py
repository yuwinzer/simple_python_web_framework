from api import API

app = API()


@app.route("/home")
def home(request, response):
    response.text = "Hello from Home page"


@app.route("/about")
def about(request, response):
    response.text = "Hello from About page"


@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello, {name}"


@app.route("/tell/{age:d}")
def greeting(request, response, age):
    response.text = f"Your age is {age}"



# def app(environ, start_response):
#     response_body = b'Hello, World!'
#     status = '200 OK'
#     start_response(status, headers=[])
#     return iter([response_body])
