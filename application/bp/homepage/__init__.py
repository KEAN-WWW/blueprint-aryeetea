from flask import Blueprint, render_template

# MUST be named 'homepage' so the import works
homepage = Blueprint("homepage", __name__, template_folder="templates")

@homepage.route("/")
def home():
    return render_template("homepage.html")

@homepage.route("/about")
def about():
    return render_template("about.html")
