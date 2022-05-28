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


@app.route("/book")
class BooksResource:
    def get(self, request, response):
        response.text = "Books page"

    def post(self, request, response):
        response.text = "Endpoint to create a book"


def handler(req, resp):
    resp.text = "sample"


app.add_route("/sample", handler)


@app.route("/template")
def template_handler(req, resp):
    resp.body = app.template(
        "index.html", context={"name": "Bumbo", "title": "Best Framework"}).encode()



# def app(environ, start_response):
#     response_body = b'Hello, World!'
#     status = '200 OK'
#     start_response(status, headers=[])
#     return iter([response_body])
