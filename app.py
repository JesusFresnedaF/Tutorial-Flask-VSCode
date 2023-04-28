from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

@app.route("/hola")
def hello_there():
    return render_template("layout.html")

# Replace the existing home function with the one below
@app.route("/")
def home():
    return render_template("home.html")

# New functions
@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

if __name__ == "__main__":
    app.run(debug=False)