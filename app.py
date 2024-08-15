from flask import Flask, redirect, render_template, request
from cricmodules import *

# Global Variables
usropt = []

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=['GET', "POST"])
def index():
    return render_template("index.html")

'''@app.route("/instruction")
def instruction():
    return render_template("instruction.html")'''

@app.route("/toss", methods=["GET", "POST"])
def instruction():
    usropt[0] = request.form.get('toss')
    usropt[1] = request.form.get("play")
    tosswin = toss(usropt)
    return render_template("toss.html")