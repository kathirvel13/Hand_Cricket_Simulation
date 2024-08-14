from flask import Flask, redirect, render_template, request

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

@app.route("/play", methods=["GET", "POST"])
def instruction():
    return render_template("play.html")