from bottle import *
import base64
import os.path
debug(True)
BaseRequest.MEMFILE_MAX = 1024 * 1024
base_dir = os.path.dirname(os.path.abspath(__file__))


@get("/javascript/<filename>")
def javascript(filename):
    return static_file(filename, root="./javascript")


@get("/css/<filename>")
def css(filename):
    return static_file(filename, root="./css")


@get("/image/<filename>")
def image(filename):
    return static_file(filename, root="./image")


@get("/")
@view("index")
def index():
    return dict()


@get("/list")
@view("list")
def image_list():
    files = os.listdir(base_dir + "/thumbs/")
    return dict(files=filter(lambda x: x.endswith(".png"), files))


@get("/thumb/<filename>")
def thumb(filename):
    response = static_file(filename, root="./thumbs")
    response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
    return response


head = len("data:image/png;base64,")


@post("/save/<filename>")
def save(filename):
    with open(base_dir + "/thumbs/{}.png".format(filename), "wb") as f:
        f.write(base64.b64decode(request.forms.get("src")[head:]))
    return ""


@post("/delete")
def delete():
    filename = request.forms.get("filename")
    os.remove(base_dir + "/thumbs/{}.png".format(filename))
    return ""

run(host="0.0.0.0", port=5000, reloader=True)
