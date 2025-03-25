from pprint import pprint

from flask import Flask, render_template, request

app = Flask(__name__)


# API/Endpoint
@app.get("/")
def hello_world():
    return "<h1>Super, Cool 😁</h1>"


name = "Jamie"
hobbies = ["Gaming", "Reading", "Soccer", "Ballet", "Gyming", "Yoga"]


@app.get("/about")
def about_page():
    return render_template("about.html", name=name, hobbies=hobbies)


from routes.movies_bp import movies_bp

app.register_blueprint(movies_bp, url_prefix="/movies")

if __name__ == "__main__":
    app.run(debug=True)
