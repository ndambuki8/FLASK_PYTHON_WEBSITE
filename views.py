from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name="Flo")

@views.route("/profile")
def profile():
    return render_template("profile.html")

#sending json to be displayed/rendered on a webpage
@views.route("/json")
def get_json():
    return jsonify({'name':'tim', 'coolness':10})

#Getting json from a route
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

#Redirect
@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))
