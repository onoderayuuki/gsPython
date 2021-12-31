from flask import Flask,request
app = Flask("app")

@app.route("/")
def index():
    return "Hello from flask"


@app.route("/api/hello")
def api_hello():
    return "api_hello"

@app.route("/api/items/<int:item_id>")
def api2(item_id):
    return "item_id is %d" % item_id

@app.route("/api/users",methods=["GET"])
def api_users_get():
    search_key = request.args.get("user_id")
    return "user_id is %s" % search_key

@app.route("/api/users",methods=["POST"])
def api_users_update():
    user_name = request.form.get("user_name")
    return "user_name = %s" % user_name


app.run()