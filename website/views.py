from flask import Blueprint, render_template, session, request, redirect, url_for

views = Blueprint('views', __name__, static_folder="static", template_folder="templates")


@views.route('/')
def home():
    return render_template("index.html")

@views.route('/about')
def about():
    return render_template("about.html")


@views.route('/contact')
def contact():
    return render_template("contact.html")

@views.route('/thanks_contact')
def thanks_contact():
    return render_template("thanks_contact.html")
