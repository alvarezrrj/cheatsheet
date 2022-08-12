# TO DO
# Delete Cache control lines
# Replace Images/blabla.png for /static/Images/blabla.png on all html files

import os

# from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
# app.jinja_env.filters["usd"] = usd


# List of languages
langs = []
with os.scandir('templates') as iterator:
    for entry in iterator:
        if entry.is_file() and not entry.name.startswith('.') and not "layout" in entry.name:
            langs.append(entry.name.split('.')[0])

# Global variables available to every template
app.jinja_env.globals["languages"] = langs

# Function grabs all sections in a file
def sections(filename):
    sections = []
    with open(f"templates/{filename}", 'r') as file:
        for line in file:
            if 'section id=' in line:
                section_id = line.split('"')[1]
                section_name = ' '.join(section_id.split("-"))
                sections.append({'id': section_id, 'name': section_name})
    return sections


# DELETE WHEN DONE
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("HTML.html", sections=sections("HTML.html"))

@app.route("/<lang>")
def lang(lang):
    return render_template(lang, sections=sections(lang))
