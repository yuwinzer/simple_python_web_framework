from api import API
from middleware import Middleware

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


@app.route("/book")
class BooksResource:
    def get(self, request, response):
        response.text = "Books page"

    def post(self, request, response):
        response.text = "Endpoint to create a book"


@app.route("/exception")
def exception_throwing_handler(request, response):
    raise AssertionError("This handler should not be used.")


def handler(req, resp):
    resp.text = "sample"


app.add_route("/sample", handler)


# @app.route("/template")
# def template_handler(req, resp):
#     resp.body = app.template(
#         "index.html", context={"name": "Bumbo", "title": "Best Framework"}).encode()


@app.route("/template")
def template_handler(req, resp):
    resp.html = app.template("index.html", context={"name": "Bumbo", "title": "Best Framework"})


@app.route("/json")
def json_handler(req, resp):
    resp.json = {"name": "data", "type": "JSON"}


@app.route("/text")
def text_handler(req, resp):
    resp.text = "This is a simple text"


def custom_exception_handler(request, response, exception_cls):
    response.text = str(exception_cls)


app.add_exception_handler(custom_exception_handler)


# custom middleware

class SimpleCustomMiddleware(Middleware):
    def process_request(self, req):
        print("Processing request", req.url)

    def process_response(self, req, res):
        print("Processing response", req.url)


app.add_middleware(SimpleCustomMiddleware)



# def app(environ, start_response):
#     response_body = b'Hello, World!'
#     status = '200 OK'
#     start_response(status, headers=[])
#     return iter([response_body])
