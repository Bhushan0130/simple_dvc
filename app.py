from flask import Flask, render_template, request, jsonify
import os
#import yaml
#import joblib
# import numpy as np

params_path =  "params.yaml"
webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder = static_dir, template_folder = template_dir)
@app.route("/", methods = [ "GET", "POST"])

def index():
    if request.method == "POST":
        pass
    else:
        return rendor_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 4444, debug = True)


